# Intervention Event Schema

## Purpose

Define the action-log record used to capture what the house, household, or
system did in response to a parcel condition.

## Stage placement

This is a **`v1.5`** bridge support object.

It is one of the minimum pieces needed to move from "what is happening?" to
"what did we do, and did it help?"

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "event_id": "intv_0001",
  "occurred_at": "2026-04-14T19:35:00Z",
  "action_type": "hvac_recirculate_on",
  "action_source": "operator_manual",
  "details": {
    "target_surface": "main_hvac",
    "notes": "Recirculate enabled during smoke event."
  }
}
```

## Minimum fields

- `parcel_id`
- `event_id`
- `occurred_at`
- `action_type`
- `action_source`

Optional useful fields:

- `details`
- `linked_house_state_ref`
- `linked_capability_ref`

## Design rules

- Intervention records should describe the action, not whether it worked.
- They should be easy to link to later response windows and verification
  outcomes.
- Keep manual and system-initiated actions distinguishable.

## Related docs

- `house-state-schema.md`
- `verification-outcome-schema.md`
- `../../architecture/v1.5/house-state-and-verification-model.md`
