# Retention Cleanup Report Schema

## Purpose

Define the machine-readable report produced by the reference retention cleanup runner.

## Core fields

- `ran_at`
- `access_events_removed`
- `rights_requests_removed`
- `notes`

## Minimum object

```json
{
  "ran_at": "2026-03-30T21:00:00Z",
  "access_events_removed": 0,
  "rights_requests_removed": 0,
  "notes": [
    "Completed export requests older than the retention window were removed."
  ]
}
```
