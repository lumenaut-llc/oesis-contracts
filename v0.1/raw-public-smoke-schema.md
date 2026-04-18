# Raw Public Smoke Context Schema

## Purpose

Define the raw adapter input for regional smoke context before it is merged into
a public-context object. This contract describes what the public smoke adapter
produces from external feeds.

## Status

Implemented as an adapter input in the reference pipeline.

## Required fields

- `source_name`
- `observed_at`
- `parcel_id`
- `regional_pm25_ugm3`
- `smoke_advisory_level`

## Field notes

- `regional_pm25_ugm3`
  Regional PM2.5 concentration in micrograms per cubic meter from the public
  source. Not a parcel-level measurement.
- `smoke_advisory_level`
  Coarse severity enum: `none`, `low`, `moderate`, `high`, `very_high`.

## Design rules

- Raw public smoke data should be traceable in provenance and reasons when it
  contributes to a parcel-state output.
- This object feeds into the public-context merge path; it is not consumed
  directly by the inference engine.

## Related docs

- `public-context-schema.md`
- `../../software/ingest-service/public-smoke-adapter.md`
