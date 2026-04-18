# Data Model Examples

This directory contains the accepted `v0.1` baseline examples plus a small set
of transitional compatibility examples that belong to later lanes conceptually.

## Frozen `v0.1` baseline examples

- `node-observation.example.json`
  Example of a raw node packet from `oesis.bench-air.v1`.
- `node-registry.example.json`
  Example of a parcel-scoped registry binding nodes into one parcel system.
- `normalized-observation.example.json`
  Example of the canonical observation object emitted by ingest.
- `parcel-context.example.json`
  Example of parcel installation context and parcel priors.
- `parcel-state.example.json`
  Example of a dwelling-facing parcel-state snapshot.
- `public-context.example.json`
  Example of optional public external context supplied to inference.
- `raw-public-weather.example.json`
  Example of a source-shaped public weather payload before normalization.
- `raw-public-smoke.example.json`
  Example of a source-shaped public smoke payload before normalization.
- `sharing-settings.example.json`
- `consent-record.example.json`
- `rights-request.example.json`
- `shared-neighborhood-signal.example.json`
- `sharing-store.example.json`
- `consent-store.example.json`
- `operator-access-event.example.json`
- `rights-request-store.example.json`
- `export-bundle.example.json`
- `retention-cleanup-report.example.json`

## Transitional compatibility examples (non-baseline)

These files may remain temporarily for migration and compatibility, but they
are not part of the frozen `v0.1` acceptance surface:

- `house-state.example.json`
- `house-capability.example.json`
- `equipment-state-observation.example.json`
- `source-provenance-record.example.json`
- `intervention-event.example.json`
- `intervention-event-flood.example.json`
- `intervention-event-heat.example.json`
- `verification-outcome.example.json`
- `verification-outcome-flood.example.json`
- `verification-outcome-heat.example.json`
- `control-compatibility.example.json`

Treat these as later-lane material (`v1.5` bridge support, and `v2.5` for full
controls-compatibility inventory), even when copies exist here.

## Lane rule

Keep examples aligned with prose contracts and matching JSON Schemas in
`../schemas/`.

If a future lane needs a changed or additive example, add it under
`../v1.0/examples/` or `../v1.5/examples/` instead of rewriting baseline files
in this directory.
