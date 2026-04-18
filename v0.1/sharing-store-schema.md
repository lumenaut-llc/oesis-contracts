# Sharing Store Schema

## Purpose

Define a file-backed internal store for parcel sharing eligibility that can be reused across reference services without exposing exact parcel identifiers in shared-map outputs.

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
- shared-map eligibility should be derived from the `sharing` object, not inferred from raw contributions alone

## Related docs

- `sharing-settings-schema.md`
- `shared-neighborhood-signal-schema.md`
