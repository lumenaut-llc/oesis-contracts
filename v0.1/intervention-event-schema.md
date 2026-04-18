# Intervention Event Schema

## Purpose

Record a discrete action taken at a parcel in response to an environmental condition, whether initiated manually by an operator or suggested by the system.

## Stage placement

Intervention event is a bridge-stage object. The schema exists in v0.1 for structural validation and early integration testing, but the primary design documentation and operational context live in `v1.5/intervention-event-schema.md`.

## Core fields

- `parcel_id`
- `event_id`
- `occurred_at`
- `action_type`
- `action_source` -- enum: `operator_manual`, `system_advisory`, `system_bounded_control`, `unknown`
- `details` -- optional freeform object
- `linked_house_state_ref` -- optional reference to the house-state snapshot that prompted the action
- `linked_capability_ref` -- optional reference to a house-capability record

## Design rules

- every intervention should be attributed to an action source so the system can distinguish operator actions from automated responses
- references to house state and capability are optional but strongly encouraged for auditability
- the details object is intentionally open to accommodate diverse action types during early piloting

## Related docs

- `../v1.5/intervention-event-schema.md`
- `house-state-schema.md`
- `house-capability-schema.md`
