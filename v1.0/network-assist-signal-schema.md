# Network-Assist Signal Schema (`v1.0`)

## Purpose

Define the output contract for data that flows from a parcel to the platform
operator under the network-assist sharing mode. This signal is used exclusively
for internal model improvement and calibration. It must never be published,
attributed to a specific parcel in any user-facing surface, or used to influence
the contributing parcel's own state evaluation.

## Core fields

- `signal_id`
- `parcel_ref`
- `generated_at`
- `batch_id`
- `consent_verified`
- `hazard_bands`
- `evidence_mode`
- `confidence_band`
- `node_families`

### `hazard_bands`

An object with coarsened hazard classification per domain:

- `smoke_band` -- enum: `low`, `medium`, `high`, `unknown`
- `flood_band` -- enum: `low`, `medium`, `high`, `unknown`
- `heat_band` -- enum: `low`, `medium`, `high`, `unknown`

Bands replace exact probabilities. The coarsening threshold table is an internal
platform configuration, not part of this contract.

### Optional fields

- `installation_context` -- enum: `indoor_only`, `sheltered_outdoor`, `mixed`
- `siting_limitations` -- array of strings describing known installation
  constraints (e.g. `"north_facing_only"`, `"near_hvac_exhaust"`)

## Minimum object

```json
{
  "signal_id": "nas_20260413_batch01_parcel_ref_001",
  "parcel_ref": "parcel_ref_parcel_001",
  "generated_at": "2026-04-13T04:00:00Z",
  "batch_id": "nightly_20260413",
  "consent_verified": true,
  "hazard_bands": {
    "smoke_band": "medium",
    "flood_band": "low",
    "heat_band": "low"
  },
  "evidence_mode": "live",
  "confidence_band": "medium",
  "node_families": ["bench_air", "weather_pm_mast"]
}
```

## Design rules

- Signals are extracted on a nightly batch cycle, not in real time. The
  `batch_id` field identifies the extraction run.
- `consent_verified` must be `true` at extraction time. If consent has been
  revoked or a revocation is pending, the signal must not be generated.
- `parcel_ref` is an opaque internal reference. It must never appear in any
  user-facing output, shared-map layer, or external report.
- Custody is internal only: the platform operator holds these signals for model
  retraining and calibration. They must not be shared with third parties,
  research programs, or neighborhood surfaces.
- Retention follows a 90-day rolling window. Signals older than 90 days must be
  deleted or irreversibly aggregated.
- Network-assist signals must not be used to modify the contributing parcel's own
  inferred state. The signal flows outward for collective model quality; it must
  not create a feedback loop that changes the contributor's hazard view.
- Exact probabilities, raw sensor readings, and parcel geometry must not appear
  in this contract. The coarsened band structure is the maximum precision that
  leaves the private parcel context under this mode.
- If the platform later needs finer-grained internal signals, a new contract
  version and a new consent scope are required.

## Related docs

- `governance-operational-model.md`
- `consent-store-schema.md`
- `sharing-settings-schema.md`
- `../../legal/privacy/permissions-matrix.md`
- `../../software/inference-engine/architecture.md`
