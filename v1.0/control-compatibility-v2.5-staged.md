# Control Compatibility Schema

## Purpose

Define the parcel-scoped compatibility inventory used when the product moves
from response measurement into bounded controls.

## Stage placement

This is primarily a **`v2.5`** object.

Draft records may exist earlier for experimentation, but they should not be
treated as proof that compatibility mapping or bounded-control policy is
operationally complete in **`v1.5`**.

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "effective_at": "2026-04-14T19:30:00Z",
  "endpoints": [
    {
      "label": "main_thermostat",
      "endpoint_type": "thermostat",
      "integration_class": "matter",
      "local_control_available": true,
      "advisory_only": false,
      "soft_integration": true,
      "harder_integration": false,
      "override_required": false
    }
  ]
}
```

## Minimum fields

- `parcel_id`
- `effective_at`
- `endpoints`

Each endpoint should minimally carry:

- `label`
- `endpoint_type`
- `integration_class`
- `local_control_available`

Useful early flags:

- `advisory_only`
- `soft_integration`
- `harder_integration`
- `override_required`

## Design rules

- This object belongs to bounded-controls work, not to the current parcel-state
  baseline.
- Compatibility inventory should always be paired with override and verification
  posture in later stages.
- Do not imply that because a thermostat or plug is known, it is automatically
  safe to actuate.

## Related docs

- `../v1.5/house-capability-schema.md`
- `../v1.5/intervention-event-schema.md`
- `../v1.5/verification-outcome-schema.md`
- `../../architecture/system/version-and-promotion-matrix.md`
