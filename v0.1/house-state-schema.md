# House State Schema

## Purpose

Capture a point-in-time snapshot of indoor environmental response and power state for a parcel, used to evaluate whether a dwelling is maintaining functional conditions during an environmental event.

## Stage placement

House state is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/house-state-schema.md`.

## Core fields

- `parcel_id`
- `captured_at`
- `indoor_response` -- required object containing `pm25_ugm3`, `temperature_c`, `relative_humidity_pct`
- `power_state` -- required object containing `mains_state`, `backup_power_present`, `backup_power_active`
- `source_summary` -- optional object with `node_ids` and `source_kind`

## Design rules

- indoor response values must be explicit; missing readings should not be silently omitted
- power state uses a simple enum (`up`, `down`, `unknown`) rather than attempting detailed grid modeling
- this object records observed state, not inferred state or recommendations

## Related docs

- `../v1.5/house-state-schema.md`
- `../../architecture/system/node-taxonomy.md`
- `parcel-state-schema.md`
