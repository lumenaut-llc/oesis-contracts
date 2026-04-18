# Contracts v1.0

## Purpose

Provide the additive `v1.0` contract lane without mutating the frozen
`../v0.1/` contract surface.

## How to use this lane

- Put future-lane schema deltas in `schemas/`
- Put future-lane example deltas in `examples/`
- Put future-lane contract-document deltas beside this README when the narrative
  contract needs stronger wording than the frozen `../v0.1/` lane docs
- Keep `../v0.1/schemas/` and `../v0.1/examples/` as the accepted `v0.1`
  baseline

## Current deltas in this lane

- `parcel-context-schema.md` frames stronger parcel-intelligence context while
  keeping bridge-stage house-state and intervention semantics in the `v1.5`
  lane
- `control-compatibility-schema.md` keeps bounded-controls compatibility inventory
  posture visible in an additive lane while remaining staged primarily for `v2.5`
- `schemas/equipment-state-observation.schema.json` adds a `v1.0` lane variant
  for adapter/read-side operating posture snapshots
- `schemas/source-provenance-record.schema.json` adds a `v1.0` lane variant for
  per-signal confidence and freshness metadata
- `governance-operational-model.md` sets `v1.0` as the first lane where
  governance execution is treated as a runtime contract surface rather than only
  policy framing
- `consent-record-schema.md`
- `consent-store-schema.md`
- `sharing-settings-schema.md`
- `sharing-store-schema.md`
- `schemas/consent-record.schema.json`
- `schemas/consent-store.schema.json`
- `schemas/sharing-settings.schema.json`
- `schemas/sharing-store.schema.json`
- `examples/equipment-state-observation.example.json`
- `examples/source-provenance-record.example.json`
- `network-assist-signal-schema.md` defines the output contract for internal
  model-improvement signals extracted under the network-assist sharing mode
- `research-data-export-schema.md` defines the framework contract for
  program-scoped data exports under the research/pilot sharing mode
- `schemas/network-assist-signal.schema.json`
- `schemas/research-data-export.schema.json`
- `examples/consent-record.example.json`
- `examples/consent-store.example.json`
- `examples/sharing-settings.example.json`
- `examples/sharing-store.example.json`
- `examples/network-assist-signal.example.json`
- `examples/research-data-export.example.json`
- `trust-score-schema.md`
- `deployment-metadata-schema.md`
- `schemas/trust-score.schema.json`
- `schemas/deployment-metadata.schema.json`
- `examples/trust-score.example.json`
- `examples/deployment-metadata.example.json`
- `circuit-monitor-observation-schema.md` — formal contract for circuit-monitor
  packets and `equipment.circuit.snapshot` normalized observations
- `schema-migration-v0.1-to-v1.0.md` — migration guide for additive field
  changes between v0.1 and v1.0 schemas

## Current posture

This directory is ready for explicit `v1.0` additions. If a required schema or
example is not yet overridden here, the current `v0.1` artifact remains the
baseline reference until a real `v1.0` delta is added.

House-state, intervention-event, and verification-outcome bridge contracts
belong primarily in `../v1.5/`.

## Version boundary (governance)

- `v0.1`: governance objects may exist as baseline/docs-compatible assets, but
  claims should remain implementation-honest.
- `v1.0`: governance is an enforced contract surface (consent, revocation,
  custody tier gating, and governance status/history/private-summary views).
- `v1.5+`: extend governance classification and enforcement for additional
  bridge-stage support objects and later controls-adjacent surfaces.
