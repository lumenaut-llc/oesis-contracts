# Circuit Monitor Observation Schema

## Purpose

Define the contract for circuit-monitor hardware packets and their normalized
observation output (`equipment.circuit.snapshot`).

## Lane placement

This contract lives in `v1.0/` because the circuit-monitor is a **v1.5 bridge**
hardware family (see `../../architecture/system/node-taxonomy.md`). It is placed
here rather than `v1.5/` because the normalizer and ingest path are implemented
in the current runtime and the schema evolution should follow the v1.0 baseline.

## Raw packet contract

The hardware serial-json-contract is the authoritative source for packet shape:
[`circuit-monitor/serial-json-contract.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/circuit-monitor/serial-json-contract.md)

### Discriminator

```
"schema_version": "oesis.circuit-monitor.v1"
```

All node families use `schema_version` as the discriminator field. The runtime
also accepts `schema_id` for backward compatibility with early firmware.

### Required top-level fields

| Field | Type | Description |
| --- | --- | --- |
| `schema_version` | string | `"oesis.circuit-monitor.v1"` |
| `node_id` | string | Stable device identifier |
| `firmware_version` | string | Firmware build version |
| `uptime_s` | integer | Seconds since boot |
| `observed_at` | string | RFC 3339 UTC timestamp |
| `circuits` | array | One entry per monitored circuit |
| `health` | object | Device health telemetry |

### Circuit object fields

| Field | Type | Description |
| --- | --- | --- |
| `circuit_id` | string | Operator-assigned circuit name |
| `current_a` | number | RMS current in amperes |
| `power_w` | number | Active power in watts |
| `voltage_v` | number | Line voltage in volts |
| `power_factor` | number | Power factor (0.0–1.0) |
| `energy_kwh` | number | Cumulative energy since counter reset |
| `inferred_state` | string | Firmware-classified state (see enumerations below) |
| `cycle_active` | boolean | Whether equipment is in an active cycle |
| `cycle_duration_s` | number or null | Seconds since cycle start |

### Inferred state enumerations

**HVAC:** `off`, `fan_only`, `compressor_running`, `heating_active`, `overload`, `unknown`

**Sump:** `standby`, `starting`, `running`, `overload`, `unknown`

## Normalized observation

The normalizer produces `observation_type: "equipment.circuit.snapshot"`.

### Output shape

| Field | Type | Description |
| --- | --- | --- |
| `observation_id` | string | Generated unique ID |
| `node_id` | string | From raw packet |
| `parcel_id` | string or null | Bound at ingest |
| `observed_at` | string | From raw packet |
| `ingested_at` | string | Server-side receipt time |
| `observation_type` | string | `"equipment.circuit.snapshot"` |
| `values.circuits` | array | Cleaned circuit readings |
| `health` | object | Extracted device health |
| `provenance` | object | Source kind, schema, firmware version |
| `versioning` | object | Runtime lane metadata |
| `raw_packet` | object | Original packet for audit |

## Inference integration

The inference engine auto-derives an `equipment_state_observation` from circuit
snapshots via `circuit_observation_to_equipment_state()`. This maps:

- `compressor_running` → `hvac_mode: "cool"`, `equipment_running: true`
- `fan_only` → `hvac_mode: "fan_only"`, `fan_state: "on"`
- `heating_active` → `hvac_mode: "heat"`, `equipment_running: true`
- Sump `running` → `sump_state: "running"`, `equipment_running: true`
- Sump `standby` → `sump_state: "standby"`

The derived equipment-state observation feeds into the evidence contribution
pipeline at HIGH confidence (`source_kind: "direct_measurement"`).

## Related docs

- [`circuit-monitor/serial-json-contract.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/circuit-monitor/serial-json-contract.md) — authoritative packet shape
- [`circuit-monitor/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/circuit-monitor/README.md) — build guide entry point
- `../../architecture/system/node-taxonomy.md` — taxonomy placement
- `schemas/equipment-state-observation.schema.json` — equipment-state schema
