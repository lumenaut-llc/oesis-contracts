# House Capability Schema

## Purpose

Define the coarse parcel / household capability support object used in the
**`v1.5`** bridge for what the house can do and what operational surfaces exist,
without treating that as a full controls-compatibility inventory.

## Stage placement

This is a **`v1.5`** support object for coarse capability and read-side
equipment-state hints.

Full interface-class inventory and bounded-controls policy belong primarily to
**`v2.5`** and are described separately in `../v1.0/control-compatibility-schema.md`.

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "effective_at": "2026-04-14T19:25:00Z",
  "capabilities": {
    "recirculation_available": true,
    "portable_purifier_present": true,
    "backup_power_present": true,
    "motorized_shades_present": false,
    "pump_or_sump_present": false,
    "higher_merv_supported": "unknown"
  },
  "equipment_state": {
    "hvac_mode": "cool",
    "fan_state": "auto",
    "air_source_mode": "recirculate",
    "purifier_state": "off"
  }
}
```

## Minimum fields

- `parcel_id`
- `effective_at`
- `capabilities`

Optional early fields:

- `equipment_state`

## Design rules

- Keep this object coarse and practical.
- Treat it as a support object for recommendations and verification, not as a
  complete integration graph.
- Do not use this object to imply that the product already supports bounded
  controls.

## Related docs

- `house-state-schema.md`
- `../v1.0/control-compatibility-schema.md`
- `intervention-event-schema.md`
- `../../architecture/system/architecture-gaps-by-stage.md`
