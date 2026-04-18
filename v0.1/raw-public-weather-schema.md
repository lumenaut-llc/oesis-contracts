# Raw Public Weather Context Schema

## Purpose

Define the raw adapter input for regional weather context before it is merged
into a public-context object. This contract describes what the public weather
adapter produces from external feeds.

## Status

Implemented as an adapter input in the reference pipeline.

## Required fields

- `source_name`
- `observed_at`
- `parcel_id`
- `regional_temperature_c`
- `regional_relative_humidity_pct`

## Optional fields

- `advisories` — array of string advisory labels (e.g. `warm_afternoon`)

## Design rules

- Raw public weather data should be traceable in provenance when it contributes
  to a parcel-state output.
- This object feeds into the public-context merge path; it is not consumed
  directly by the inference engine.

## Related docs

- `public-context-schema.md`
- `../../software/ingest-service/public-weather-adapter.md`
