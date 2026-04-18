# Operator Access Event Schema

## Purpose

Define an audit event for parcel-linked data access in the reference services.

## Core fields

- `event_id`
- `occurred_at`
- `actor`
- `action`
- `parcel_id`
- `data_classes`
- `justification`

## Minimum object

```json
{
  "event_id": "access_01HT000001",
  "occurred_at": "2026-03-30T20:40:00Z",
  "actor": "parcel-platform-api",
  "action": "view_parcel_state",
  "parcel_id": "parcel_123",
  "data_classes": [
    "private_parcel_data",
    "derived_parcel_state"
  ],
  "justification": "parcel_view_request"
}
```

## Design rules

- access events should identify the parcel-linked data classes touched
- justification should be explicit enough to distinguish normal product operation from unusual access
- this object is for audit and review, not user-facing product display
