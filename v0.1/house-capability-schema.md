# House Capability Schema

## Purpose

Describe the physical equipment and response capabilities present at a parcel, independent of whether that equipment is currently active.

## Stage placement

House capability is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/house-capability-schema.md`.

## Core fields

- `parcel_id`
- `effective_at`
- `capabilities` -- object with optional booleans and enums:
  - `recirculation_available`
  - `portable_purifier_present`
  - `backup_power_present`
  - `motorized_shades_present`
  - `pump_or_sump_present`
  - `higher_merv_supported` -- enum: `yes`, `no`, `unknown`
- `equipment_state` -- optional snapshot object with `hvac_mode`, `fan_state`, `air_source_mode`, `purifier_state`

## Design rules

- capability records describe what a dwelling can do, not what it is doing right now
- equipment state is included as an optional convenience snapshot but should not replace dedicated equipment-state-observation records for time-series tracking
- unknown capability values are acceptable and expected during early enrollment

## Related docs

- `../v1.5/house-capability-schema.md`
- `equipment-state-observation-schema.md`
- `intervention-event-schema.md`
