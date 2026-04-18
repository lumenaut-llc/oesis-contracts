# Deployment Metadata Schema v1.0

## Purpose

Define a per-node installation record that captures mount context, exposure
conditions, enclosure, power source, and maintenance posture as structured
measurement-trust inputs.

## Status

Specified. Promoted from draft (`artifacts/contracts-bundle/deployment-metadata-schema.md`)
into the v1.0 contract lane as a formal machine-readable contract.

## Why this object exists

The node-registry tells the system **what** is installed and **where**. It does
not capture **how** — the physical installation context that affects measurement
quality. A bench-air node sitting on a kitchen counter produces different
evidence quality than one properly mounted in the primary living space away from
cooking sources.

Without deployment metadata:

- trust scoring cannot distinguish bench-only from field-validated installs
- operators cannot audit whether a node's mounting meets minimum quality
- the system cannot apply install-quality penalties or bonuses to inference
- field teams have no structured record of what they installed and how

## Scope

This object describes **physical installation context** — facts about how a
node is deployed that affect measurement trust. It does not describe the node
itself (that's node-registry) or the parcel (that's parcel-context).

One deployment-metadata record exists per node per installation event. If a
node is reinstalled or moved, a new record is created with a new
`install_record_id`.

## Core fields

### Required

| Field | Type | Description |
|-------|------|-------------|
| `parcel_id` | string | Parcel where the node is installed |
| `node_id` | string | Node this record describes |
| `install_record_id` | string | Unique ID for this installation event |
| `installed_at` | datetime | When this installation occurred |
| `installed_by` | string | Operator or role who performed the install |
| `install_status` | enum | `provisional`, `field_validated`, `needs_review` |

### Mount context

| Field | Type | Description |
|-------|------|-------------|
| `mount_type` | enum | `fixed_bracket`, `adhesive`, `shelf_placed`, `clamp`, `magnetic`, `other` |
| `mount_height_m` | number | Height of sensor above floor or ground (meters) |
| `orientation_class` | string | Deployment context (e.g., `living_area`, `runoff_low_point`, `panel_interior`) |
| `field_marker_present` | boolean | Whether a physical marker identifies this install location |

### Exposure conditions

| Field | Type | Description |
|-------|------|-------------|
| `sun_exposure_class` | enum | `none`, `partial`, `full` |
| `airflow_exposure_class` | enum | `low`, `moderate`, `high` |
| `splash_exposure_class` | enum | `none`, `low`, `high` |
| `proximity_to_sources` | array of strings | Nearby contamination sources (e.g., `cooking`, `hvac_vent`, `garage`, `smoking_area`) |

### Enclosure

| Field | Type | Description |
|-------|------|-------------|
| `enclosure_revision` | string | Enclosure version or identifier |
| `enclosure_sealed` | boolean | Whether the enclosure is properly sealed |

### Power

| Field | Type | Description |
|-------|------|-------------|
| `power_source_type` | enum | `usb_c_mains`, `ac_adapter`, `poe`, `battery`, `solar_assist`, `external_dc_protected` |
| `power_reliability_class` | enum | `continuous`, `intermittent`, `battery_limited` |

### Storage

| Field | Type | Description |
|-------|------|-------------|
| `storage_type` | enum | `none`, `micro_sd`, `flash_internal` |
| `storage_capacity_gb` | number or null | Storage capacity when applicable |

### Maintenance

| Field | Type | Description |
|-------|------|-------------|
| `maintenance_status` | enum | `provisional`, `current`, `overdue`, `needs_service` |
| `last_maintenance_at` | datetime or null | Last maintenance visit |
| `maintenance_interval_days` | integer or null | Expected maintenance cadence |
| `maintenance_notes` | string or null | Free-text operator notes |

## Install quality scoring

The trust-score contract (`trust-score-schema.md`) uses deployment metadata to
compute the `install_quality` factor:

| install_status | Exposure flags | Score |
|---------------|----------------|-------|
| `field_validated` + no proximity sources | — | 1.0 |
| `field_validated` + some proximity sources | — | 0.8 |
| `provisional` (standard install, no validation) | — | 0.7 |
| `provisional` + proximity sources flagged | — | 0.5 |
| `needs_review` | — | 0.3 |
| No deployment metadata record exists | — | 0.5 (neutral) |

The `proximity_to_sources` array directly informs whether indoor air quality
readings may be biased. A bench-air node near a cooking source or HVAC vent
should trigger a trust penalty.

## Lifecycle

- Created at installation time by operator or field team
- Updated when maintenance occurs (maintenance fields only)
- Superseded (not deleted) when node is reinstalled — new `install_record_id`
- Referenced by trust-score computation on each inference cycle

## Design rules

- Deployment metadata is an **input** to trust scoring, not a gate on data
  ingestion — nodes without deployment records still ingest normally
- `proximity_to_sources` is an open array, not a closed enum — field teams may
  encounter sources not anticipated at schema design time
- `install_status: provisional` is the default for any install without explicit
  field validation — this is the normal starting state
- Maintenance fields are operator-maintained, not automatically derived
- One record per node per installation event; historical records are retained
  but only the latest `install_record_id` per `node_id` is active

## Related

- `trust-score-schema.md` (consumes install_quality factor)
- `../v0.1/node-registry-schema.md` (what is installed; deployment-metadata
  says how)
- `../../artifacts/contracts-bundle/deployment-metadata-schema.md` (original
  draft this contract formalizes)
- [`parcel-kit/parcel-installation-checklist.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/parcel-installation-checklist.md) (field
  procedure that produces deployment metadata)
