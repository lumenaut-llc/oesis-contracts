# Rights Request Store Schema

## Purpose

Define the envelope object that holds the complete set of rights requests for an operator or deployment, providing a single queryable store for export and deletion request tracking.

## Core fields

- `updated_at` -- timestamp of the last modification to the store
- `requests` -- array of rights-request objects (each validated against `rights-request.schema.json`)

## Minimum rights-request-store object

```json
{
  "updated_at": "2026-03-30T20:30:00Z",
  "requests": [
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
  ]
}
```

## Design rules

- the store is a governance object in the v0.1 baseline and should be treated as administrative evidence
- `updated_at` must reflect the last time any request in the store was added or changed
- an empty requests array is valid and represents a deployment with no pending or historical rights requests
- the store references individual rights-request objects by composition, not by ID lookup; each request is inline
- this store should be exportable and auditable without requiring access to other system state

## Related docs

- `rights-request-schema.md`
- `../../legal/privacy/retention-export-deletion-revocation.md`
- `../../software/parcel-platform/interfaces.md`
