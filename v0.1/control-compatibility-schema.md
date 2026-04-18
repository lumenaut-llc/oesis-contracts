# Control Compatibility Schema

## Purpose

Describe the controllable endpoints available at a parcel and their integration characteristics, establishing whether local control is possible and what integration class each endpoint belongs to.

## Stage placement

Control compatibility is primarily a capability-stage (v2.5) object per the node taxonomy in `architecture/system/node-taxonomy.md`. The schema exists in v0.1 for structural validation and forward-looking design, but operational use is not expected until the system reaches the capability stage where bounded automated control becomes relevant.

## Core fields

- `parcel_id`
- `effective_at`
- `endpoints` -- array (minimum one entry), each containing:
  - `label` -- human-readable name for the endpoint
  - `endpoint_type` -- device or system type (e.g., thermostat, purifier, smart plug)
  - `integration_class` -- enum: `matter`, `home_assistant`, `bacnet`, `smart_plug`, `local_api`, `cloud_only`, `unknown`
  - `local_control_available` -- boolean indicating whether the endpoint can be controlled without cloud dependency
  - `advisory_only` -- optional boolean; true if the system can only advise, not actuate
  - `soft_integration` -- optional boolean; true if integration uses a soft adapter (e.g., Home Assistant webhook)
  - `harder_integration` -- optional boolean; true if integration requires protocol-level work (e.g., BACnet binding)
  - `override_required` -- optional boolean; true if operator override is needed before the system can actuate

## Minimum control-compatibility object

```json
{
  "parcel_id": "parcel_123",
  "effective_at": "2026-04-01T12:00:00Z",
  "endpoints": [
    {
      "label": "Living room thermostat",
      "endpoint_type": "thermostat",
      "integration_class": "home_assistant",
      "local_control_available": true
    }
  ]
}
```

## Design rules

- integration class should reflect the actual protocol path, not the brand name
- local control availability is the key distinction for resilience during connectivity loss
- advisory-only endpoints are valid entries; the system should be able to reason about equipment it can recommend but not actuate
- this record describes integration posture, not current equipment state; use equipment-state-observation for live readings
- the optional boolean flags (`advisory_only`, `soft_integration`, `harder_integration`, `override_required`) should be omitted rather than set to false when not applicable

## Related docs

- `../../architecture/system/node-taxonomy.md`
- `house-capability-schema.md`
- `equipment-state-observation-schema.md`
- `intervention-event-schema.md`
