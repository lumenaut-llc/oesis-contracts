# Contracts v0.1

`v0.1` is the frozen baseline contract lane.

## Quick navigation

- `schemas/README.md` — baseline machine-readable schema index
- `examples/README.md` — baseline and transitional examples
- `../v0.2/README.md`, `../v0.3/README.md`, `../v0.4/README.md`, `../v0.5/README.md` — promotion-marker lanes that currently inherit this baseline
- `../v1.0/README.md`, `../v1.5/README.md` — additive lanes for explicit deltas

## Purpose

Canonical contract definitions for parcels, nodes, observations, states,
permissions, provenance, and baseline sharing surfaces.

## Lane contract

- **Baseline lane**: `v0.1/schemas/` and `v0.1/examples/` are the frozen
  `v0.1` contract surface.
- **Promotion-marker lanes**: `v0.2/` through `v0.5/` currently inherit this baseline unless explicit lane-specific overrides are accepted.
- **Additive lanes**: `v1.0/` and `v1.5/` hold forward contract deltas by lane.
- **Compatibility policy**: when contract docs move, keep redirect stubs for
  high-traffic old links until migration is complete.
- **Canonical mapping**: contract lanes must align with
  `../../architecture/system/version-and-promotion-matrix.md`.

## Minimum contents

- packet schemas from hardware and external feeds
- normalized observation objects
- parcel-state outputs
- provenance and freshness fields
- identity and permission linkages

## Current status

The current center of gravity remains the `current v1` observation, parcel-context, and parcel-state contracts.
Those machine-readable contracts describe the current implemented reference path.

The repo also now carries draft deployment-maturity companion docs for node health, deployment metadata, and device lifecycle events.
Those draft docs are intentionally separate from the current schemas so the docs do not imply the reference code already persists them.

For version lanes in this repository:

- `v0.1/schemas/` and `v0.1/examples/` are the frozen `v0.1` default contract
  surface
- `v1.0/` is the additive target lane for future schema/example deltas
- `v1.5/` is the additive bridge-stage lane for measurement-to-intervention
  contract deltas

Do not silently replace the `v0.1/schemas/` or `v0.1/examples/` files when
proposing future-lane changes. Add new or overridden assets under `v1.0/` or `v1.5/`
instead, depending on which version lane the change belongs to.

`v1.5` adds separate support objects for:
- house state
- indoor-response and outage evidence surfaces
- coarse house capability and **read-side** equipment-state signals
- equipment-state observation snapshots
- per-signal source provenance records
- intervention events
- verification outcomes
- building/site metadata extensions needed for response interpretation

**`v2.5`** is the primary stage for a full **controls-compatibility inventory** (interface classes, integration tiers, control-policy versioning). Draft `control-compatibility` schema files may exist for forward compatibility; they should not be read as “compatibility mapping is operationally complete” in `v1.5`.

Those support objects should not be mistaken for a breaking change to the current parcel-state contract.

See `../../architecture/system/node-taxonomy.md` and `../../architecture/system/version-and-promotion-matrix.md`.

Machine-readable starter artifacts for the frozen `v0.1` lane include:
- `schemas/node-observation.schema.json`
- `schemas/node-registry.schema.json`
- `schemas/parcel-context.schema.json`
- `schemas/parcel-state.schema.json`
- `schemas/sharing-settings.schema.json`
- `schemas/consent-record.schema.json`
- `schemas/consent-store.schema.json`
- `schemas/rights-request.schema.json`
- `schemas/shared-neighborhood-signal.schema.json`
- `schemas/sharing-store.schema.json`
- `schemas/operator-access-event.schema.json`
- `schemas/rights-request-store.schema.json`
- `schemas/export-bundle.schema.json`
- `schemas/retention-cleanup-report.schema.json`
- `examples/node-observation.example.json`
- `examples/node-registry.example.json`
- `examples/normalized-observation.example.json`
- `examples/parcel-context.example.json`
- `examples/parcel-state.example.json`
- `examples/sharing-settings.example.json`
- `examples/consent-record.example.json`
- `examples/consent-store.example.json`
- `examples/rights-request.example.json`
- `examples/shared-neighborhood-signal.example.json`
- `examples/sharing-store.example.json`
- `examples/operator-access-event.example.json`
- `examples/rights-request-store.example.json`
- `examples/export-bundle.example.json`
- `examples/retention-cleanup-report.example.json`

## Baseline narrative docs

Canonical baseline contract docs in this lane:

- `node-observation-schema.md`
- `node-registry-schema.md`
- `parcel-context-schema.md`
- `parcel-state-schema.md`
- `public-context-schema.md`
- `evidence-mode-and-observability.md`
- `evidence-summary-schema.md`
- `explanation-payload-schema.md`
- `sharing-settings-schema.md`
- `consent-record-schema.md`
- `rights-request-schema.md`
- `consent-store-schema.md`
- `sharing-store-schema.md`
- `operator-access-event-schema.md`
- `export-bundle-schema.md`
- `retention-cleanup-report-schema.md`
- `shared-neighborhood-signal-schema.md`

Bridge-stage artifacts for house state, intervention, and verification belong in
`../v1.5/` and should not be treated as part of the frozen `v0.1` default
contract lane.

If compatibility copies of those artifacts remain in `v0.1/` paths during
migration, they are explicitly non-baseline and should not gate `v0.1`
acceptance checks.

Draft controls-compatibility artifacts should be treated as forward-lane
material staged primarily for `v2.5`, even if compatibility files temporarily
exist in baseline paths for transition reasons.

The current parcel-first baseline now also includes:

- auditable parcel priors in `parcel-context`
- structured divergence records in `parcel-state`
- public-only foil outputs and contrastive explanations in `parcel-state`

## Parallel lane rule

Use the `v0.1/` paths when you mean the accepted `v0.1` baseline.

Use `v1.0/` when you need broader target-lane notes, schema deltas, or example
deltas that must remain separate from the frozen default contract set.

Use `v1.5/` when the delta is specific to the bridge from hazard description
into house-state, action, and measured outcome reasoning.

## Deployment-maturity companion schemas

Draft deployment-maturity companion docs live under `artifacts/contracts-bundle/`:

- `../../artifacts/contracts-bundle/node-health-schema.md`
- `../../artifacts/contracts-bundle/deployment-metadata-schema.md`
- `../../artifacts/contracts-bundle/device-event-schema.md`

## Related workstreams

- hardware node design
- ingest service contracts
- inference engine inputs
- privacy and governance

## Next docs to add

- provenance summary model
