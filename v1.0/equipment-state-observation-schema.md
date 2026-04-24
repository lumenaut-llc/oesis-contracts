# Equipment State Observation Schema (v1.0 lane variant)

## Purpose

Document the v1.0 lane variant of `equipment-state-observation` — adds the `fusion_hint` field for adapter/read-side operating posture snapshots.

This is **not** a replacement for the v0.1 baseline schema. It is an additive lane variant per the additive-lane pattern in [`README.md`](README.md).

## What v1.0 adds

The v1.0 schema (`schemas/equipment-state-observation.schema.json`) extends v0.1's 5 baseline fields (`captured_at`, `confidence_band`, `parcel_id`, `signals`, `source`) with one additional field:

| Field | Type | Purpose |
| --- | --- | --- |
| `fusion_hint` | enum | Adapter-derived hint about how this signal should be fused with other equipment-state evidence |

The `fusion_hint` enum values are defined in the schema JSON. This field is optional; absence does not invalidate the observation.

## Lane divergence note

v1.0 and v1.5 evolve `equipment-state-observation` independently along **parallel** axes:

- **v1.0** adds `fusion_hint` for adapter/read-side operating posture
- **v1.5** adds `bridge_role` for the house-state bridge purposes documented in [`../v1.5/equipment-state-observation-schema.md`](../v1.5/equipment-state-observation-schema.md)

Neither lane inherits from the other. This is intentional per the lane contract in [`../v0.1/README.md`](../v0.1/README.md):

> Use `v1.0/` when you need broader target-lane notes, schema deltas, or example deltas that must remain separate from the frozen default contract set.
> Use `v1.5/` when the delta is specific to the bridge from hazard description into house-state, action, and measured outcome reasoning.

A consumer choosing which schema to validate against should pick the lane that matches their use case (adapter integration → v1.0; house-state bridge → v1.5). The v0.1 baseline remains a valid superset that both lanes are compatible with.

## Related

- [`../v0.1/equipment-state-observation-schema.md`](../v0.1/equipment-state-observation-schema.md) — baseline (5 fields)
- [`../v1.5/equipment-state-observation-schema.md`](../v1.5/equipment-state-observation-schema.md) — v1.5 lane variant with `bridge_role`
- `schemas/equipment-state-observation.schema.json` — v1.0 schema JSON
- `examples/equipment-state-observation.example.json` — v1.0 example
