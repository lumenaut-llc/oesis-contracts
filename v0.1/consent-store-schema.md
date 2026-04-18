# Consent Store Schema

## Purpose

Define the append-only consent lifecycle store used by reference services to enforce active sharing eligibility at query time.

## Core fields

- `updated_at`
- `consents`

Each consent entry includes:
- `consent_id`
- `parcel_id`
- `parcel_ref`
- `granted_at`
- `revoked_at`
- `sharing_scope`
- `data_classes`
- `custody_tier`
- `recipient_type`
- `temporal_resolution`
- `spatial_precision`

## Minimum object

```json
{
  "updated_at": "2026-04-13T12:00:00Z",
  "consents": [
    {
      "consent_id": "consent_demo_active",
      "parcel_id": "parcel_001",
      "parcel_ref": "parcel_ref_parcel_001",
      "granted_at": "2026-04-13T11:00:00Z",
      "revoked_at": null,
      "revocation_reason": null,
      "sharing_scope": "neighborhood_pm25",
      "data_classes": ["outdoor_pm25"],
      "custody_tier": "shared",
      "recipient_type": "neighborhood_pool",
      "recipient_id": null,
      "temporal_resolution": "hourly",
      "spatial_precision": "parcel",
      "consent_version": 1,
      "ui_surface": "settings_sharing_tab",
      "user_agent": "reference",
      "ip_hash": "demo_hash"
    }
  ]
}
```

## Design rules

- consent records are appended for grant and updated only to set `revoked_at` and reason
- `revoked_at: null` is the active-state signal used by query eligibility logic
- sharing eligibility is determined by consent scope + data classes + recipient + custody tier
- this is administrative governance state and must not be mixed with parcel telemetry

## Related docs

- `consent-record-schema.md`
- `sharing-store-schema.md`
- `../../legal/privacy/retention-export-deletion-revocation.md`
