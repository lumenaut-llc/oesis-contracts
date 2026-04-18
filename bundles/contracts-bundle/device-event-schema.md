# Device Event Schema

## Purpose

Define a draft companion object for node lifecycle, maintenance, boot, and service events.

## Status

Draft deployment-maturity extension.
This is not yet the implemented machine-readable contract of the current reference path.

## Why this exists

The current docs talk about device identity, install state, and health, but they do not yet have a first-class event model for what happened to a node over time.

## Suggested core fields

- `event_id`
- `node_id`
- `occurred_at`
- `event_type`
- `severity`
- `payload`

## Minimum draft object

```json
{
  "event_id": "dev_evt_001",
  "node_id": "bench-air-01",
  "occurred_at": "2026-04-05T19:15:00Z",
  "event_type": "boot",
  "severity": "info",
  "payload": {
    "boot_reason": "power_on",
    "firmware_version": "0.1.0",
    "config_version": "config_v1"
  }
}
```

## Event classes to support later

- `boot`
- `heartbeat`
- `buffer_overflow`
- `config_applied`
- `maintenance_performed`
- `replacement`
- `retired`

## Design rules

- use events for lifecycle and service traceability, not for dwelling-facing hazard statements
- keep event types explicit and versionable
- link device events to trust and maintenance posture without pretending the current reference path already stores them

## Related docs

- `node-health-schema.md`
- `node-registry-schema.md`
- `../../architecture/system/deployment-maturity-ladder.md`
