# Verification Outcome Schema

## Purpose

Record whether an intervention at a parcel produced a measurable change in environmental conditions, closing the observe-act-verify loop.

## Stage placement

Verification outcome is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/verification-outcome-schema.md`.

## Core fields

- `parcel_id`
- `verification_id`
- `verified_at`
- `intervention_ref` -- optional reference to the triggering intervention event
- `hazard_type` -- enum: `smoke`, `heat`, `flood`, `outage`, `other`
- `response_window_minutes` -- optional integer indicating the evaluation window
- `result_class` -- enum: `improved`, `unchanged`, `worsened`, `inconclusive`
- `before` -- optional freeform snapshot of conditions before the intervention
- `after` -- optional freeform snapshot of conditions after the intervention
- `summary` -- optional human-readable explanation

## Design rules

- result class should be conservative; use `inconclusive` when evidence is ambiguous
- before and after snapshots are intentionally freeform during early piloting but should converge toward structured house-state references
- this record is evidence, not a guarantee of causation

## Related docs

- `../v1.5/verification-outcome-schema.md`
- `intervention-event-schema.md`
- `house-state-schema.md`
