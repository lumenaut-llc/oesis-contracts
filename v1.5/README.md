# Contracts v1.5

## Purpose

Provide the additive `v1.5` bridge-stage contract lane without mutating the
frozen root `v0.1` contract surface or overloading the additive `v1.0` lane.

## How to use this lane

- Put `v1.5` schema deltas in `schemas/`
- Put `v1.5` example deltas in `examples/`
- Put `v1.5` bridge-specific contract notes beside this README
- Keep `../v0.1/schemas/` and `../v0.1/examples/` as the accepted `v0.1`
  baseline
- Keep `../v1.0/` for broader target-lane contract deltas that are not specific
  to the measurement-to-intervention bridge

## Expected `v1.5` surfaces

- house-state support objects
- read-side equipment-state and coarse house-capability surfaces
- source-provenance support objects for per-signal confidence/freshness
- intervention-event records
- verification-outcome records
- bridge metadata needed for response interpretation

## Initial contents

Narrative docs:
- `house-state-schema.md`
- `house-capability-schema.md`
- `equipment-state-observation-schema.md`
- `source-provenance-record-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`

JSON schemas:
- `schemas/house-state.schema.json`
- `schemas/house-capability.schema.json`
- `schemas/equipment-state-observation.schema.json`
- `schemas/source-provenance-record.schema.json`
- `schemas/intervention-event.schema.json`
- `schemas/verification-outcome.schema.json`

Examples:
- `examples/house-state.example.json`
- `examples/house-capability.example.json`
- `examples/equipment-state-observation.example.json`
- `examples/source-provenance-record.example.json`
- `examples/intervention-event.example.json`
- `examples/verification-outcome.example.json`

## Guardrail

`v1.5` is the minimum bridge from hazard description into response reasoning.
It is not the home for a full controls-compatibility inventory or bounded
controls execution semantics.

Governance baseline for private/shared/public custody, consent lifecycle, and
revocation behavior is established in `../v1.0/`. `v1.5` should extend that
taxonomy for bridge support objects rather than redefining governance posture.
