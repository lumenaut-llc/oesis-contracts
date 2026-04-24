#!/usr/bin/env python3
"""
Validate each example file against its schema for lanes v0.1, v1.0, v1.5.

Schemas reference each other via relative $ref (e.g. "sharing-settings.schema.json"),
so we build a referencing.Registry per lane with every schema pre-loaded. Without
that, jsonschema raises Unresolvable on the first cross-schema $ref.

Exits 0 when all examples validate, 1 on any validation failure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

REPO_ROOT = Path(__file__).resolve().parent.parent
# Each lane is either a version dir (v0.1, v1.0, v1.5) OR the published bundle.
# The bundle is a v0.1 snapshot for downstream consumers; adding it here
# catches future drift between bundle content and its manifest without
# requiring a separate generator.
LANES = ["v0.1", "v1.0", "v1.5", "bundles/contracts-bundle"]


def build_registry(schemas_dir: Path) -> Registry:
    """Pre-load every *.schema.json in the lane under its bare filename."""
    registry = Registry()
    for schema_path in schemas_dir.glob("*.schema.json"):
        contents = json.loads(schema_path.read_text(encoding="utf-8"))
        resource = Resource(contents=contents, specification=DRAFT202012)
        # Schemas reference siblings by bare filename, so register under that URI.
        registry = registry.with_resource(uri=schema_path.name, resource=resource)
    return registry


def main() -> int:
    failures: list[str] = []

    for lane in LANES:
        lane_dir = REPO_ROOT / lane
        schemas_dir = lane_dir / "schemas"
        examples_dir = lane_dir / "examples"
        if not examples_dir.is_dir() or not schemas_dir.is_dir():
            continue

        registry = build_registry(schemas_dir)

        for example_path in sorted(examples_dir.glob("*.example.json")):
            base = example_path.name[: -len(".example.json")]
            schema_path = schemas_dir / f"{base}.schema.json"
            if not schema_path.is_file():
                continue  # schema-example coverage job catches this

            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            data = json.loads(example_path.read_text(encoding="utf-8"))

            validator = Draft202012Validator(schema, registry=registry)
            errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
            if errors:
                rel = example_path.relative_to(REPO_ROOT)
                failures.append(str(rel))
                print(f"Invalid: {rel}")
                for e in errors:
                    path = ".".join(str(p) for p in e.path) or "<root>"
                    print(f"  {path}: {e.message}")

    if failures:
        print(f"\n{len(failures)} example(s) failed validation", file=sys.stderr)
        return 1
    print("All examples validate against their schemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
