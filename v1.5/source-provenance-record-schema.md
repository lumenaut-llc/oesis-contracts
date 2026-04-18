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

## Guardrails

- Keep this object private by default.
- Preserve source quality and freshness; do not convert this into recommendation
  output.
- Do not claim certainty beyond the evidence path captured in records.

## Related

- `equipment-state-observation-schema.md`
- `verification-outcome-schema.md`
- `../../evidence-mode-and-observability.md`
