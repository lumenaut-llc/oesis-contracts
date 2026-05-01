# Source Provenance Record Schema (`v1.5`)

## Purpose

Capture per-signal provenance needed for honest bridge-stage verification
without forcing detailed confidence internals into baseline parcel-state.

## Why this belongs in `v1.5`

The first serious closed loops depend on measured before/after outcomes.
Outcomes are not interpretable without knowing where equipment-state inputs came
from and how fresh they were.

## Minimum fields

- `parcel_id`
- `captured_at`
- `records`

Per-record minimum:

- `signal_key`
- value payload
- `confidence_band`
- `source_kind`
- `source_name`
- `method`
- `observed_at`
- `ttl_seconds`
- `stale`

## Adapter-trust facts (G18 — when `source_kind == "adapter_derived"`)

Per [ADR 0009](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/meta/adr/0009-admissibility-schema-split-facts-vs-decision.md) and [`adapter-trust-program.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/adapter-trust-program.md) §C, every record with `source_kind == "adapter_derived"` carries five adapter-trust facts that runtime needs to compute the §C admissibility decision:

| Field | Type | Purpose |
| --- | --- | --- |
| `adapter_source_ref` | string | Pointer to the source authority file under adapter-trust-program §A |
| `adapter_contract_version` | string | Version string the reading was produced against |
| `adapter_onboarding_ref` | string | Pointer to the parcel's initial verification record for this adapter |
| `adapter_credential_last_verified_at` | timestamp | Most recent credential / contract-version verification |
| `adapter_tier` | enum | One of `tier_1_passive` / `tier_2_adapter` / `tier_3_direct` per node-taxonomy.md |

These are **conditionally required** — the schema enforces their presence only when `source_kind == "adapter_derived"`. Records with `source_kind` of `direct_measurement`, `inferred`, or `manual_entry` neither require nor populate them.

This is the v1.5 parallel to G17's calibration-program §C facts on v1.0 `node-observation`. Runtime branches on `adapter_tier`:

- absent or `tier_3_direct` → calibration-program §C rules apply (use the v1.0 node-observation facts on the producing node)
- `tier_1_passive` or `tier_2_adapter` → adapter-trust-program §C rules apply (use these adapter facts)

The admissibility **decision** fields (`admissible_to_calibration_dataset`, `admissibility_reasons`) do NOT live in this schema — they are runtime outputs on normalized observations only.

## Guardrails

- Keep this object private by default.
- Preserve source quality and freshness; do not convert this into recommendation
  output.
- Do not claim certainty beyond the evidence path captured in records.

## Related

- [ADR 0009 — schema-carries-facts decision](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/meta/adr/0009-admissibility-schema-split-facts-vs-decision.md)
- [Adapter-trust program §C](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/adapter-trust-program.md)
- [`../v1.0/node-observation-schema.md`](../v1.0/node-observation-schema.md) — calibration-program §C parallel (G17)
- `equipment-state-observation-schema.md`
- `verification-outcome-schema.md`
- `../v0.1/evidence-mode-and-observability.md`
