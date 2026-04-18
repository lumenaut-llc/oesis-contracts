# Deployment Metadata Schema

## Purpose

Define a draft companion object for installation quality, mounting context, and maintenance posture without overloading the current parcel-context baseline.

## Status

Draft deployment-maturity extension.
This is not yet the implemented machine-readable contract of the current reference path.

## Why this exists

The current parcel-context schema intentionally stays small.
That keeps the reference pipeline honest, but it leaves many field-operations facts implied rather than explicit.

## Suggested core fields

- `parcel_id`
- `node_id`
- `install_record_id`
- `installed_at`
- `mount`
- `exposure`
- `enclosure`
- `power`
- `storage`
- `maintenance`

## Minimum draft object

```json
{
  "parcel_id": "parcel_123",
  "node_id": "flood-node-01",
  "install_record_id": "install_001",
  "installed_at": "2026-04-05T18:00:00Z",
  "mount": {
    "mount_type": "fixed_bracket",
    "mount_height_m": 0.62,
    "orientation_class": "runoff_low_point",
    "field_marker_present": true
  },
  "exposure": {
    "sun_exposure_class": "partial",
    "airflow_exposure_class": "low",
    "splash_exposure_class": "high"
  },
  "enclosure": {
    "enclosure_revision": "flood-enclosure-r1"
  },
  "power": {
    "power_source_type": "external_dc_protected"
  },
  "storage": {
    "storage_type": "micro_sd"
  },
  "maintenance": {
    "maintenance_status": "provisional",
    "last_maintenance_at": null
  }
}
```

## Design rules

- treat deployment context as part of measurement trust, not just as a note to humans
- keep it editable without rewriting raw observations
- store richer field-ops facts here rather than silently stuffing them into parcel-state or node-observation
- do not present this draft as implemented behavior until a machine-readable contract and code path exist

## Related docs

- `parcel-context-schema.md`
- `node-registry-schema.md`
- [`parcel-kit/parcel-installation-checklist.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/parcel-installation-checklist.md)
