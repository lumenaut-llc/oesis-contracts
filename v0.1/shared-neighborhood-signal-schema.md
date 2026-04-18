# Shared Neighborhood Signal Schema

## Purpose

Define a coarse shared-input contract for neighborhood aggregation that avoids exact parcel identifiers and supports suppression rules.

## Core fields

- `generated_at`
- `min_participants`
- `sharing_settings`
- `contributions`

Each sharing-settings entry includes:
- `parcel_ref`
- `neighborhood_aggregate`
- `revocation_pending`

Each contribution includes:
- `cell_id`
- `source_class`
- `parcel_ref`
- `delayed_minutes`
- `hazards`

## Minimum object

```json
{
  "generated_at": "2026-03-30T20:30:00Z",
  "min_participants": 3,
  "sharing_settings": [
    {
      "parcel_ref": "parcel_ref_001",
      "neighborhood_aggregate": true,
      "revocation_pending": false
    }
  ],
  "contributions": [
    {
      "cell_id": "cell_demo_001",
      "source_class": "shared_data",
      "parcel_ref": "parcel_ref_001",
      "delayed_minutes": 15,
      "hazards": {
        "smoke_probability": 0.62,
        "flood_probability": 0.05,
        "heat_probability": 0.21
      }
    }
  ]
}
```

## Design rules

- contributions must use coarse spatial identifiers rather than exact parcel geometry
- this contract must not carry exact parcel identifiers
- if internal linkage is needed for eligibility checks, use an opaque `parcel_ref`, not a public parcel identifier
- shared-data visibility should be suppressed when the minimum participant threshold is not met
- shared-data contributions should only be counted when the corresponding sharing settings allow neighborhood aggregation and no revocation is pending
- public-context contributions may remain visible if they do not expose household-linked information

## Related docs

- `../../legal/privacy/public-map-policy.md`
- `../../software/shared-map/interfaces.md`
