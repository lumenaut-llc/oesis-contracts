# Verification Outcome Schema

## Purpose

Define the outcome / verification record used to capture whether measured
conditions improved after an intervention or bounded action.

## Stage placement

This is a **`v1.5`** bridge support object and one of the key pieces in the
first serious smoke closed loop.

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "verification_id": "verify_0001",
  "verified_at": "2026-04-14T20:10:00Z",
  "intervention_ref": "intv_0001",
  "hazard_type": "smoke",
  "response_window_minutes": 45,
  "result_class": "improved",
  "before": {
    "indoor_pm25_ugm3": 38.0
  },
  "after": {
    "indoor_pm25_ugm3": 12.0
  },
  "summary": "Indoor PM2.5 fell after recirculation and purifier use."
}
```

## Minimum fields

- `parcel_id`
- `verification_id`
- `verified_at`
- `hazard_type`
- `result_class`

Useful early fields:

- `intervention_ref`
- `response_window_minutes`
- `before`
- `after`
- `summary`

## Design rules

- Verification should remain separate from parcel-state.
- A verification record should capture whether an action helped over a defined
  window, not silently alter hazard confidence.
- The first serious target for this object is smoke protection with bounded
  windows such as **30-90 minutes**.

## Related docs

- `intervention-event-schema.md`
- `house-state-schema.md`
- `../parcel-state-schema.md`
- `../../architecture/v1.5/house-state-and-verification-model.md`
