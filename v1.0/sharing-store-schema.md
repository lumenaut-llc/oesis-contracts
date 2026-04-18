# Sharing Store Schema (`v1.0`)

## Purpose

Define a file-backed internal store for parcel sharing posture that can be reused
across reference services without exposing exact parcel identifiers in shared-map
outputs.

## Core fields

- `updated_at`
- `parcels`

Each parcel entry includes:
- `parcel_id`
- `parcel_ref`
- `sharing`

## Minimum object

```json
{
  "updated_at": "2026-03-30T20:30:00Z",
  "parcels": [
    {
      "parcel_id": "parcel_001",
      "parcel_ref": "parcel_ref_parcel_001",
      "sharing": {
        "parcel_id": "parcel_001",
        "updated_at": "2026-03-30T20:15:00Z",
        "private_only": false,
        "network_assist": false,
        "neighborhood_aggregate": true,
        "research_or_pilot": false,
        "notice_version": "sharing-notice.v1",
        "revocation_pending": false
      }
    }
  ]
}
```

## Design rules

- `parcel_ref` is an opaque internal reference for cross-service eligibility checks
- the store may contain exact parcel identifiers, but shared-map outputs must not
- this store should mirror user-facing posture, not replace consent-based query gating

## Version note

In `v1.0`, consent-store state should be considered canonical for active sharing
eligibility decisions; sharing-store remains a useful UI/operational projection.

## Related docs

- `governance-operational-model.md`
- `sharing-settings-schema.md`
- `consent-store-schema.md`

