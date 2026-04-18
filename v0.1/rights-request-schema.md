# Rights Request Schema

## Purpose

Define the canonical request object for parcel operator export and deletion workflows.

## Core fields

- `request_id`
- `parcel_id`
- `account_id`
- `request_type`
- `status`
- `created_at`
- `scope`
- `requested_from_surface`

## Minimum rights-request object

```json
{
  "request_id": "rights_01HT000001",
  "parcel_id": "parcel_123",
  "account_id": "acct_123",
  "request_type": "export",
  "status": "submitted",
  "created_at": "2026-03-30T20:20:00Z",
  "scope": [
    "private_parcel_data",
    "derived_parcel_state"
  ],
  "requested_from_surface": "parcel_settings_ui"
}
```

## Design rules

- rights requests should be trackable by status rather than treated as ad hoc support tickets
- request scope should identify the affected data classes
- deletion and export should share a common tracking model where practical
- this object should support audit and user-visible status updates

## Related docs

- `../../legal/privacy/retention-export-deletion-revocation.md`
- `../../software/parcel-platform/interfaces.md`
