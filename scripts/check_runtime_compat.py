#!/usr/bin/env python3
"""
Pre-fanout breaking-change check.

Before contract changes merge to oesis-contracts/main and trigger
release-fanout, validate that oesis-runtime's hand-coded validators
will still accept every contract example. If a schema change tightens
a constraint that runtime can't yet honor (or vice versa), this catches
it at the contracts PR — not after fanout opens broken sync PRs in
every downstream repo.

Strategy:
- Discover every example under oesis-contracts/v*/examples/
- For each example, derive the runtime validator function name:
    <basename-with-hyphens-replaced>.example.json -> validate_<name>
  Variant examples (e.g. intervention-event-flood.example.json) collapse
  to the base type (validate_intervention_event) — they exercise the same
  validator with a different payload shape.
- Import the matching runtime lane's validate_examples module and call
  the validator with the contract example payload.
- Report pass/fail per example. Exit 1 if any fail.

Lane mapping (contracts lane -> runtime module):
  v0.1 -> oesis.ingest.v0_1.validate_examples
  v1.0 -> oesis.ingest.v1_0.validate_examples (inherits v0.1 validators)
  v1.5 -> oesis.ingest.v1_0.validate_examples (no v1_5 module yet; gap G18)

Usage:
  RUNTIME_PATH=/path/to/oesis-runtime python3 scripts/check_runtime_compat.py
  # or:
  python3 scripts/check_runtime_compat.py --runtime /path/to/oesis-runtime

Designed to run in the oesis-contracts CI after cloning runtime into a
sibling directory.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
from pathlib import Path
from typing import Callable

REPO_ROOT = Path(__file__).resolve().parent.parent

# Each contracts lane maps to a runtime ingest lane module. v1.5 falls back
# to the v1.0 runtime validators because no v1_5 ingest module exists yet
# (tracked as gap G18 in oesis-runtime).
LANE_TO_RUNTIME_MODULE = {
    "v0.1": "oesis.ingest.v0_1.validate_examples",
    "v1.0": "oesis.ingest.v1_0.validate_examples",
    "v1.5": "oesis.ingest.v1_0.validate_examples",
}

# Explicit routing for variant examples whose basename doesn't naively map
# to the right validator. Format: example basename -> base type to validate as.
# Use cases:
#   - Different schema entirely (node-observation-flood is actually a flood-node packet)
#   - Variant payloads of same schema (node-observation-mast-lite still bench-air)
EXPLICIT_VARIANT_ROUTING = {
    # node-observation-flood uses oesis.flood-node.v1 schema, not bench-air;
    # it duplicates flood-observation.example.json's validator coverage.
    "node-observation-flood": "flood-observation",
    # node-observation-mast-lite is a bench-air variant payload.
    "node-observation-mast-lite": "node-observation",
}

# Variant examples (e.g. intervention-event-flood) reuse the base validator.
# Map a variant suffix that should NOT be stripped to itself; everything else
# falls through to the longest-match strip-from-end logic.
KNOWN_BASE_TYPES = {
    "node-observation",
    "normalized-observation",
    "intervention-event",
    "verification-outcome",
    "circuit-monitor-observation",
    "normalized-circuit-observation",
    "weather-pm-observation",
    "normalized-weather-pm-observation",
    "flood-observation",
    "normalized-flood-observation",
    "consent-record",
    "consent-store",
    "control-compatibility",
    "deployment-metadata",
    "equipment-state-observation",
    "evidence-summary",
    "export-bundle",
    "house-capability",
    "house-state",
    "network-assist-signal",
    "node-registry",
    "operator-access-event",
    "parcel-context",
    "parcel-state",
    "public-context",
    "raw-public-smoke",
    "raw-public-weather",
    "research-data-export",
    "retention-cleanup-report",
    "rights-request",
    "rights-request-store",
    "shared-neighborhood-signal",
    "sharing-settings",
    "sharing-store",
    "source-provenance-record",
    "trust-score",
}


def base_type_for(example_basename: str) -> str:
    """
    Collapse a variant example basename to its base type.

    e.g. 'intervention-event-flood' -> 'intervention-event'
         'node-observation' -> 'node-observation'
         'node-observation-flood' -> 'flood-observation' (via explicit override)

    Strategy: explicit overrides win, then longest known base type that is a prefix.
    """
    if example_basename in EXPLICIT_VARIANT_ROUTING:
        return EXPLICIT_VARIANT_ROUTING[example_basename]
    for candidate in sorted(KNOWN_BASE_TYPES, key=len, reverse=True):
        if example_basename == candidate or example_basename.startswith(candidate + "-"):
            return candidate
    # Fall back to the basename itself; runtime will report "no validator" if missing.
    return example_basename


def validator_func_name(base_type: str) -> str:
    return "validate_" + base_type.replace("-", "_")


def load_runtime_module(module_path: str):
    return importlib.import_module(module_path)


def discover_examples(lane: str) -> list[Path]:
    examples_dir = REPO_ROOT / lane / "examples"
    if not examples_dir.is_dir():
        return []
    return sorted(examples_dir.glob("*.example.json"))


def check_lane(lane: str, runtime_module_path: str) -> list[str]:
    """Return list of failure messages for this lane."""
    failures: list[str] = []
    try:
        module = load_runtime_module(runtime_module_path)
    except ImportError as exc:
        return [f"[{lane}] cannot import {runtime_module_path}: {exc}"]

    for example_path in discover_examples(lane):
        basename = example_path.name[: -len(".example.json")]
        base_type = base_type_for(basename)
        func_name = validator_func_name(base_type)
        validator: Callable | None = getattr(module, func_name, None)

        if validator is None:
            # Runtime hasn't implemented this validator yet. Not a regression
            # caused by this PR — flag as info, don't fail.
            print(f"SKIP [{lane}] {basename}: no {func_name} in {runtime_module_path}")
            continue

        try:
            payload = json.loads(example_path.read_text(encoding="utf-8"))
            validator(payload)
            print(f"PASS [{lane}] {basename}")
        except Exception as exc:  # ValidationError or KeyError or unexpected
            rel = example_path.relative_to(REPO_ROOT)
            msg = f"FAIL [{lane}] {rel} via {func_name}: {exc}"
            failures.append(msg)
            print(msg, file=sys.stderr)

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--runtime",
        default=os.environ.get("RUNTIME_PATH"),
        help="Path to oesis-runtime checkout (or set RUNTIME_PATH env var)",
    )
    args = parser.parse_args()

    if not args.runtime:
        print(
            "ERROR: --runtime <path> or RUNTIME_PATH env var required",
            file=sys.stderr,
        )
        return 2

    runtime_path = Path(args.runtime).expanduser().resolve()
    if not (runtime_path / "oesis").is_dir():
        print(
            f"ERROR: {runtime_path} does not look like an oesis-runtime checkout "
            "(no oesis/ package found)",
            file=sys.stderr,
        )
        return 2

    sys.path.insert(0, str(runtime_path))

    all_failures: list[str] = []
    for lane, runtime_module in LANE_TO_RUNTIME_MODULE.items():
        all_failures.extend(check_lane(lane, runtime_module))

    if all_failures:
        print(
            f"\n{len(all_failures)} contract example(s) rejected by runtime "
            "validators. This PR would break downstream runtime sync.",
            file=sys.stderr,
        )
        return 1

    print("\nAll contract examples accepted by runtime validators.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
