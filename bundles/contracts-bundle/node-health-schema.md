# Node Health Schema

## Purpose

Define a draft companion object for device-health reporting that can grow beyond the minimal health block currently embedded in observation packets.

## Status

Draft deployment-maturity extension.
This is not yet the implemented machine-readable contract of the current reference path.

## Why this exists

The current observation contracts carry a minimal health block.
That is enough for the reference pipeline, but it is not enough for stronger deployment maturity, device operations, or measurement trust.

## Suggested core fields

- `node_id`
- `recorded_at`
- `uptime_s`
- `power`
- `storage`
- `connectivity`
- `boot`
- `buffer`
- `health_flags`

## Minimum draft object

```json
{
  "node_id": "mast-lite-01",
  "recorded_at": "2026-04-05T19:10:00Z",
  "uptime_s": 1820,
  "power": {
    "power_source_state": "external_dc",
    "supply_voltage_v": 5.02
  },
  "storage": {
    "storage_state": "ok",
    "buffer_fill_pct": 12
  },
  "connectivity": {
    "wifi_connected": true,
    "signal_quality": "moderate"
  },
  "boot": {
    "boot_reason": "power_on"
  },
  "buffer": {
    "buffer_drop_count": 0
  },
  "health_flags": []
}
```

## Design rules

- keep this object separate from parcel-state outputs
- use it to explain trust and service posture, not to imply parcel hazard truth
- allow node-family-specific additions while preserving a recognizable envelope
- do not treat this doc as proof that the current reference code already persists this object

## Related docs

- `node-observation-schema.md`
- `node-registry-schema.md`
- `device-event-schema.md`
