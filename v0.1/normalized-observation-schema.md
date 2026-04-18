# Normalized Observation Schema

## Purpose

Define the canonical ingest output object produced after a raw node packet is
validated and normalized. This is the primary downstream input to the inference
engine and the bridge between hardware packet contracts and parcel-state
derivation.

## Status

Implemented in the reference path for `oesis.bench-air.v1` packets.

## Required fields

- `observation_id`
- `node_id`
- `parcel_id`
- `observed_at`
- `ingested_at`
- `observation_type`
- `values`
- `health`
- `provenance`

## Field notes

- `observation_type`
  Identifies the normalized observation family. Current implemented value:
  `air.node.snapshot`. Planned families include `flood.low_point.snapshot`,
  `air.pm_weather.snapshot`, and `thermal.scene.snapshot`.
- `values`
  Sensor-derived values after normalization. Schema is intentionally open to
  accommodate different observation families.
- `provenance`
  Links back to the raw packet: `source_kind`, `schema_version`,
  `firmware_version`, `raw_packet_ref`.
- `raw_packet`
  Optional embedded copy of the original hardware packet for audit.

## Design rules

- Normalized observations should carry temporal integrity fields (`observed_at`,
  `ingested_at`) as first-class architecture, not optional metadata.
- One normalized observation per ingest event per node.
- Health and provenance must survive normalization so downstream consumers can
  assess trust without re-reading raw packets.

## Related docs

- `node-observation-schema.md`
- `../../software/ingest-service/architecture.md`
- `../../architecture/current/architecture-object-map.md` (§4)
