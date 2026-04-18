# Sharing Settings Schema

## Purpose

Define the canonical parcel-linked sharing settings object used by the parcel platform to show, update, and audit sharing choices.

## Core fields

- `parcel_id`
- `updated_at`
- `private_only`
- `network_assist`
- `neighborhood_aggregate`
- `research_or_pilot`
- `notice_version`
- `revocation_pending`

## Minimum sharing-settings object

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

- `private_only` should be true when no outbound sharing mode is enabled.
- activation of any non-private mode should reference the notice version shown to the parcel operator
- settings should be understandable in the parcel UI without legal translation
- revocation state should be visible so users do not think a prior setting is still active

## Related docs

- `../../legal/privacy/permissions-matrix.md`
- `../../legal/privacy/user-consent-and-sharing-notice.md`
