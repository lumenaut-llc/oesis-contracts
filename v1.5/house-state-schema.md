# House State Schema

## Purpose

Define the minimum private house-state support object added in the **`v1.5`**
bridge so the product can move from parcel sensing toward measured household
response without changing the baseline parcel-state contract.

## Stage placement

This is a **`v1.5`** support object, not part of the `current v1`
parcel-state spine.

It exists to capture the minimum household response evidence needed for the
first serious closed loop:

- indoor PM2.5
- indoor temperature
- indoor relative humidity
- mains status
- backup-power posture

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "captured_at": "2026-04-14T19:20:00Z",
  "indoor_response": {
    "pm25_ugm3": 18.2,
    "temperature_c": 27.1,
    "relative_humidity_pct": 43.0
  },
  "power_state": {
    "mains_state": "up",
    "backup_power_present": true,
    "backup_power_active": false
  },
  "source_summary": {
    "node_ids": ["indoor-response-01"],
    "source_kind": "private_support_object"
  }
}
```

## Minimum fields

- `parcel_id`
- `captured_at`
- `indoor_response`
- `power_state`

### `indoor_response`

- `pm25_ugm3`
- `temperature_c`
- `relative_humidity_pct`
- `infiltration` (optional derived object)
- `thermal_dynamics` (optional derived object)

#### `infiltration`

IO ratio baseline characterization. The indoor/outdoor PM2.5 ratio under
non-event, non-intervention conditions is the parcel's structural smoke
infiltration signature.

- `io_ratio` -- current indoor/outdoor PM2.5 ratio at capture time.
- `baseline_io_ratio` -- 30-day rolling median computed only when outdoor PM2.5
  is 5-30 ug/m3, purifier is off, and HVAC is not in fresh-air mode. This
  represents the building envelope's passive infiltration behavior.
- `baseline_io_p25`, `baseline_io_p75` -- interquartile range of qualifying
  baseline samples; spread indicates how stable the envelope signature is.
- `envelope_class` -- derived from baseline: `tight` (<0.20), `average`
  (0.20-0.40), `leaky` (>0.40), `unknown` (insufficient samples). This
  classification conditions smoke loop outcome predictions. A tight home with a
  purifier running should achieve roughly 90% PM reduction; a leaky home roughly
  55%.
- `baseline_sample_count` -- number of qualifying samples in the rolling window.
- `baseline_last_updated` -- timestamp of last baseline recomputation.

#### `thermal_dynamics`

Indoor temperature trajectory for the heat closed loop.

- `indoor_rise_rate_f_per_hour` -- computed via linear regression on rolling
  2-hour temperature history. Positive values indicate warming; negative values
  indicate cooling.
- `rise_rate_r2` -- regression fit quality. Below 0.7 indicates noisy data
  (cooking, door openings, intermittent HVAC cycling) rather than genuine
  sustained heat accumulation. The engine should lower confidence when R2 is
  poor.
- `time_to_threshold_hours` -- projects when indoor temperature will cross the
  danger threshold at the current rise rate. Null if not warming. Default
  threshold is 88 deg F; adjusted to 82 deg F when vulnerable occupants are
  registered.
- `threshold_f` -- the temperature threshold used for the projection.
- `confidence_interval_low_hours`, `confidence_interval_high_hours` --
  uncertainty bounds on time-to-threshold derived from regression standard error.
- `recommendation` -- maps from the projected action window with a 1-hour safety
  buffer: `immediate_action` (<0.5h), `act_now` (<1.5h),
  `pre_cool_recommended` (<3h), `monitor_closely` (<6h), `low_urgency` (>6h),
  `no_action_needed` (not warming).

### `power_state`

- `mains_state`
- `backup_power_present`
- `backup_power_active`

Optional later additions may include:

- `battery_soc_pct`
- `generator_state`
- richer per-room or per-zone indoor-response breakdowns
- per-zone infiltration characterization when multi-sensor parcels exist

## Design rules

- This object should stay private by default.
- It should capture **measured house state**, not recommendations.
- It should not silently become a controls object.
- It exists so later intervention and verification records can answer whether
  the house actually protected occupants during smoke, heat, outage, or similar
  events.

## Related docs

- `../parcel-state-schema.md`
- `../parcel-context-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- `equipment-state-observation-schema.md`
- `../../architecture/v1.5/house-state-and-verification-model.md`
- `../../software/inference-engine/derived-house-state-fields.md`
- `../../software/inference-engine/hazard-logic-v0.md`
