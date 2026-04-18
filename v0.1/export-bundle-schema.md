# Export Bundle Schema

## Purpose

Define the machine-readable export bundle produced by the reference parcel rights workflow.

## Core fields

- `generated_at`
- `parcel_id`
- `sharing`
- `rights_requests`
- `access_events`
- `parcel_state`
- `house_state`
- `house_capability`
- `control_compatibility`
- `intervention_events`
- `verification_outcomes`

## Minimum object

```json
{
  "generated_at": "2026-03-30T20:50:00Z",
  "parcel_id": "parcel_001",
  "sharing": {},
  "rights_requests": [],
  "access_events": [],
  "parcel_state": {},
  "house_state": null,
  "house_capability": null,
  "control_compatibility": null,
  "intervention_events": [],
  "verification_outcomes": []
}
```

## Design rules

- exports should include parcel-linked data and governance records relevant to the request scope
- exports should be machine-readable JSON in the reference implementation
- administrative evidence may remain even after deletion processing, but the export should clearly label what is included
- `v1.5` support objects remain private parcel data by default and should be exported with the same owner-facing rights posture as other parcel-linked records
