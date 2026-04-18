# v1.0 Schema Deltas

This directory holds additive `v1.0` schema files or schema overrides.

The canonical baseline `../../v0.1/schemas/` directory remains the frozen
`v0.1` default schema surface. Add files here only when a future-lane contract
must differ from that baseline.

Current `v1.0` additive schema files:

- `consent-record.schema.json`
- `consent-store.schema.json`
- `sharing-settings.schema.json`
- `sharing-store.schema.json`

**Forward-compatibility placements** (narratively assigned to capability-stage
`v1.5`, placed here for schema evolution continuity — not `v1.0` deliverables):

- `equipment-state-observation.schema.json`
- `source-provenance-record.schema.json`

The v1.0 product surface and scope docs do not require these schemas. They are
here so the v1.5 bridge lane can evolve them additively from a v1.0 baseline
rather than forking from v0.1. See `../../v1.5/README.md` for their primary
architectural home.

**Governance-layer contracts** (v1.0 deliverables — these support the sharing
and research participation modes defined in `../../legal/privacy/permissions-matrix.md`):

- `network-assist-signal.schema.json`
- `research-data-export.schema.json`

**Measurement-trust contracts** (v1.0 deliverables — these compose per-signal
quality factors into parcel-level trust assessment):

- `trust-score.schema.json`
- `deployment-metadata.schema.json`
