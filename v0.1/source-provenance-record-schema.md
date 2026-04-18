# Source Provenance Record Schema

## Purpose

Provide a per-signal audit trail that tracks where each value in a parcel's state came from, how confident the system is in it, and whether it is stale.

## Stage placement

Source provenance record is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/source-provenance-record-schema.md`.

## Core fields

- `parcel_id`
- `captured_at`
- `records` -- array of provenance entries, each containing:
  - `signal_key`
  - `value_type` -- enum: `string`, `number`, `boolean`, `null`
  - typed value field (`string_value`, `number_value`, `boolean_value`, or `null_value`) matching `value_type`
  - `confidence_band` -- enum: `high`, `medium`, `low`, `none`
  - `source_kind` -- enum: `direct_measurement`, `adapter_derived`, `inferred`, `manual_entry`
  - `source_name`
  - `method`
  - `observed_at`
  - `ttl_seconds`
  - `stale` -- boolean
  - `raw_ref` -- optional reference to the underlying raw record

## Design rules

- each record entry describes exactly one signal so provenance can be evaluated per-value rather than per-object
- value type and the corresponding typed field are enforced together via conditional validation
- staleness is a computed boolean that consumers can use directly without recalculating TTL

## Related docs

- `../v1.5/source-provenance-record-schema.md`
- `equipment-state-observation-schema.md`
- `node-observation-schema.md`
