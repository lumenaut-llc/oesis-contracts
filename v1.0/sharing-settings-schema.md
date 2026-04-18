# Sharing Settings Schema (`v1.0`)

## Purpose

Define the canonical parcel-linked sharing settings object used by the parcel
platform to show and update high-level sharing choices.

## Core fields

- `parcel_id`
- `updated_at`
- `private_only`
- `network_assist`
- `neighborhood_aggregate`
- `research_or_pilot`
- `notice_version`
- `revocation_pending`

## Minimum object

```json
{
  "parcel_id": "parcel_123",
  "updated_at": "2026-03-30T20:15:00Z",
  "private_only": true,
  "network_assist": false,
  "neighborhood_aggregate": false,
  "research_or_pilot": false,
  "notice_version": "sharing-notice.v1",
  "revocation_pending": false
}
```

## Design rules

- `private_only` should be true when no outbound sharing mode is enabled
- activation of any non-private mode should reference the notice version shown
- settings should be understandable in the parcel UI without legal translation
- revocation state should be visible so users do not assume prior consent is active

## Version note

In `v1.0`, sharing settings are UI posture and summary state, while consent
stores remain the canonical query-time eligibility source.

## Related docs

- `governance-operational-model.md`
- `sharing-store-schema.md`
- `consent-store-schema.md`
- `../../legal/privacy/permissions-matrix.md`

