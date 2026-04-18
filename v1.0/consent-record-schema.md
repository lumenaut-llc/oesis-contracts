# Consent Record Schema (`v1.0`)

## Purpose

Define the canonical administrative record created when a parcel operator enables
or revokes a sharing mode tied to parcel-linked data.

## Core fields

- `consent_record_id`
- `parcel_id`
- `account_id`
- `sharing_mode`
- `action`
- `effective_at`
- `notice_version`
- `source_surface`

## Minimum consent-record object

```json
{
  "consent_record_id": "consent_01HT000001",
  "parcel_id": "parcel_123",
  "account_id": "acct_123",
  "sharing_mode": "neighborhood_aggregate",
  "action": "enabled",
  "effective_at": "2026-03-30T20:15:00Z",
  "notice_version": "sharing-notice.v1",
  "source_surface": "parcel_settings_ui"
}
```

## Design rules

- every non-private sharing activation should create a consent record
- revocation should also create a record rather than editing history in place
- the notice version should preserve what the user actually saw
- this record is administrative evidence, not product telemetry

## Version note

`v1.0` treats this as operational evidence tied to runtime consent and revocation
flows. `v0.1` records remain valid baseline artifacts.

## Related docs

- `governance-operational-model.md`
- `consent-store-schema.md`
- `../../legal/privacy/user-consent-and-sharing-notice.md`
- `../../legal/privacy/retention-export-deletion-revocation.md`

