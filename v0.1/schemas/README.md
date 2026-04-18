# Machine-Readable Schemas

## Purpose

Index the canonical JSON Schema files used for validation, examples, and
runtime-adjacent smoke checks.

## Frozen baseline (`v0.1`)

- `node-observation.schema.json`
- `node-registry.schema.json`
- `parcel-context.schema.json`
- `parcel-state.schema.json`
- `sharing-settings.schema.json`
- `consent-record.schema.json`
- `consent-store.schema.json`
- `rights-request.schema.json`
- `shared-neighborhood-signal.schema.json`
- `sharing-store.schema.json`
- `operator-access-event.schema.json`
- `rights-request-store.schema.json`
- `export-bundle.schema.json`
- `retention-cleanup-report.schema.json`

## Bridge support objects (`v1.5`)

- `house-state.schema.json`
- `house-capability.schema.json`
- `equipment-state-observation.schema.json`
- `source-provenance-record.schema.json`
- `intervention-event.schema.json`
- `verification-outcome.schema.json`

These schemas define the minimum house-state, action, and verification surfaces
needed to move from parcel sensing toward measured response. They are support
objects, not a change to the frozen baseline parcel-state contract.

The current parcel-state schema is now additive rather than minimal-only: it
includes divergence records, parcel-prior application details, a public-only
counterfactual path, and contrastive explanation objects used for verification.

## Later bounded-controls surface (`v2.5`)

- `control-compatibility.schema.json`

This schema may exist early for forward compatibility, but full
control-compatibility inventory is primarily a later bounded-controls surface.

## Compatibility note

If bridge or later-stage schema files temporarily exist under this directory for
migration compatibility, treat them as non-baseline and non-gating for `v0.1`
acceptance.

## Related docs

- `../README.md`
- `../examples/README.md`
- `../../architecture/system/version-and-promotion-matrix.md`
