# v1.0 Governance Operational Model

## Purpose

Make governance enforceable as contract and runtime behavior in the additive
`v1.0` lane, without rewriting `v0.1` history.

## Core rule

For every parcel-linked data flow, the system must be able to answer:

1. who owns the source data,
2. who can see derived/shared output,
3. under what consent conditions sharing is allowed, and
4. how revocation changes future visibility.

## Enforcement surfaces in this lane

- consent lifecycle records (`consent-record`, `consent-store`)
- sharing posture records (`sharing-settings`, `sharing-store`)
- query-time eligibility checks against active consent
- explicit runtime governance UX surfaces:
  - sharing status
  - consent history
  - private summary

## Version boundaries

### `v0.1` baseline

- governance language and baseline artifacts may exist
- implementation may remain partial or docs-first
- avoid backfilling new required enforcement fields that would change accepted
  `v0.1` behavior

### `v1.0` target lane

- governance is treated as a required contract surface
- consent + revocation must gate shared eligibility in reference services
- structurally private classes must fail sharing attempts

### `v1.5+` follow-on

- extend governance taxonomy for bridge-stage support objects and later
  control-adjacent surfaces
- preserve the same private/shared/public enforcement posture

## Related contracts

- `consent-record-schema.md`
- `consent-store-schema.md`
- `sharing-settings-schema.md`
- `sharing-store-schema.md`
- `../v1.5/README.md`

