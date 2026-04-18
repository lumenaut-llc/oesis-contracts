# Equipment State Observation Schema

## Purpose

Capture a point-in-time read of HVAC and related equipment signals at a parcel, including the source method and confidence level of the observation.

## Stage placement

Equipment state observation is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/equipment-state-observation-schema.md`.

## Core fields

- `parcel_id`
- `captured_at`
- `confidence_band` -- enum: `high`, `medium`, `low`, `none`
- `source` -- required object containing `source_kind`, `source_name`, `method`, `ttl_seconds`, and optional `raw_ref`
- `signals` -- object with optional keys: `hvac_mode`, `fan_state`, `air_source_mode`, `purifier_state`, `sump_state`, `outdoor_air_intake`, `equipment_running`, `setpoint_f`

## Design rules

- confidence band and source kind must be explicit so downstream consumers can weight the observation appropriately
- TTL expresses how long this observation should be considered current before it becomes stale
- signals are all optional because equipment inventories vary widely across parcels

## Related docs

- `../v1.5/equipment-state-observation-schema.md`
- `house-capability-schema.md`
- `house-state-schema.md`
