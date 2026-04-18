# Equipment State Observation Schema (`v1.5`)

## Purpose

Capture read-side operating posture for bridge-stage response loops while
keeping `house-state` compact and stable.

## Why this belongs in `v1.5`

`v1.5` is where OESIS needs enough measured operating-state evidence to connect:

`hazard -> house state -> action -> measured outcome`

without pretending controls automation is complete.

## Minimum fields

- `parcel_id`
- `captured_at`
- `confidence_band`
- `source`
- `signals`

## Bridge-stage signal targets

- HVAC mode
- fan state
- recirculation versus fresh-air posture
- purifier state
- sump or pump state

## Acquisition tiers and source_kind mapping

Equipment operating state reaches the system through three acquisition tiers.
The `source_kind` field in the `source` object identifies which tier produced a
given observation.

| Tier | `source_kind` | Description | Confidence |
| --- | --- | --- | --- |
| Tier 3 (direct measurement) | `"direct_measurement"` | CT clamp or panel-level sensing via circuit-monitor node. Highest fidelity, no cloud dependency. | HIGH |
| Tier 2 (adapter integration) | `"adapter_derived"` | Cloud API or local integration with smart thermostats (Ecobee, Nest, Sensibo, Honeywell) or home automation platforms. | HIGH (cloud-dependent) |
| Tier 1 (passive inference) | `"inferred"` | Thermal slope analysis or other passive inference from existing indoor temperature sensors. Zero additional hardware. | LOW or MEDIUM |
| Manual | `"manual_entry"` | Operator or occupant input via UI or checklist. | Varies |

The inference engine adapter registry evaluates available sources in descending
tier order (Tier 3 first, then Tier 2, then Tier 1). If a higher-tier source is
fresh within its TTL, lower-tier results are suppressed in the output but may
still run for calibration. See
`../../software/inference-engine/thermal-slope-inference.md` for the Tier 1
passive inference method.

## Guardrails

- Read-side state first; do not imply guaranteed actuation.
- Preserve source kind and freshness metadata for every snapshot.
- Keep this object private by default unless explicit sharing policy applies.

## Related

- `house-state-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- [`v1.5/equipment-state-adapter.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/v1.5/equipment-state-adapter.md)
