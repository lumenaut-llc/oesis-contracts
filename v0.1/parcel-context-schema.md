# Parcel Context Schema

## Purpose

Define the minimum parcel and installation context needed for the inference engine to interpret observations without pretending a node reading is equivalent to parcel truth.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `node-observation-schema.md`
- `parcel-state-schema.md`
- `house-state-schema.md`
- `house-capability-schema.md`
- [`bench-air-node/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/bench-air-node/README.md)
- `../../software/inference-engine/interfaces.md`

## Why this schema exists

The current repo has node-observation and parcel-state contracts, but it does not yet have a canonical parcel-context contract between them.

That gap matters because hazard reasoning depends on context such as:

- whether a node is indoor, sheltered, or outdoor
- whether a node is actually attached to a parcel
- whether a node is installed at a runoff-relevant low point
- whether parcel priors are known or absent

Without parcel context, the system can only see measurements. It cannot responsibly interpret their parcel relevance.

The current `v1` contract stays intentionally small.

`v1.5` should extend this context with optional fields that support building response, intervention planning, and later compatibility mapping without breaking the baseline contract.

**Staging note:** full **controls-compatibility inventory** (interface-class mapping and integration tiers) is primarily **capability stage `v2.5`**, not `v1.5`. See `../../architecture/system/architecture-gaps-by-stage.md` and `../../architecture/system/version-and-promotion-matrix.md`.

## Current implementation boundary

This doc describes the current parcel-context baseline plus planned deployment-maturity extensions.
The current machine-readable examples and schemas should still be treated as the implemented contract.

## Minimum parcel-context object

```json
{
  "parcel_id": "parcel_123",
  "site_profile": {
    "structure_type": "single_family",
    "parcel_area_m2": 740,
    "climate_zone": "unknown",
    "notes": null
  },
  "node_installations": [
    {
      "node_id": "bench-air-01",
      "node_type": "bench_air_node",
      "location_mode": "indoor",
      "install_role": "reference_indoor",
      "placement_notes": "office near hallway",
      "height_m": 1.2,
      "exposure_bias_flags": [
        "hvac_possible"
      ],
      "installed_at": "2026-03-30T18:00:00Z"
    }
  ],
  "parcel_priors": {
    "heat_retention_class": "high",
    "runoff_tendency_class": "low",
    "smoke_exposure_class": "high",
    "fema_zone": "AE",
    "foundation_type": "basement",
    "first_floor_elev_ft": 9.5,
    "base_flood_elev_ft": 10.0,
    "year_built": 1968,
    "dist_to_water_ft": 420,
    "zone_zero_clearance_class": "combustible",
    "defensible_space_class": "partial",
    "roof_class": "roof_class_a",
    "exterior_class": "exterior_wood",
    "vent_class": "vents_unscreened",
    "window_class": "single_pane",
    "dist_to_wildland_ft": 680
  },
  "structure_response_profile": {
    "orientation_class": "southwest_exposed",
    "hvac_type": "forced_air",
    "filter_path_class": "1_inch_return",
    "higher_merv_support": "unknown"
  },
  "site_dependency_profile": {
    "drainage_path_notes": [
      "driveway lip drains toward curb cut"
    ],
    "primary_route_posture": "limited_exits",
    "backup_power_available": "no"
  },
  "known_protective_capabilities": {
    "recirculation_available": true,
    "portable_purifier_present": true,
    "motorized_shades_present": false
  },
  "known_vulnerable_zones": [
    "west upstairs bedroom",
    "driveway low point"
  ],
  "divergence_tracking": {
    "temperature_c": {
      "persistence_minutes": 105,
      "num_concordant_sensors": 2
    },
    "pm25": {
      "persistence_minutes": 190,
      "num_concordant_sensors": 2
    }
  }
}
```

## Required top-level fields

- `parcel_id`
- `site_profile`
- `node_installations`
- `parcel_priors`

The following are optional in `current v1`, but intended to become important in `v1.5`:
- `structure_response_profile`
- `site_dependency_profile`
- `known_protective_capabilities`
- `known_vulnerable_zones`
- `divergence_tracking`

## Site profile fields

- `structure_type`
  Suggested initial enum: `single_family`, `duplex`, `multi_unit`, `unknown`
- `parcel_area_m2`
  Optional numeric field for later use in parcel modeling
- `climate_zone`
  Optional string for future external-context interpretation
- `notes`
  Optional free-text for admin use, not inference by default

## Node installation fields

Each node linked to a parcel should carry explicit installation context.

Minimum fields:

- `node_id`
- `node_type`
- `location_mode`
- `install_role`
- `placement_notes`
- `height_m`
- `exposure_bias_flags`
- `installed_at`

Suggested initial `location_mode` enum:

- `indoor`
- `sheltered`
- `outdoor`
- `low_point`

Suggested initial `install_role` enum:

- `reference_indoor`
- `reference_sheltered`
- `primary_outdoor_air`
- `runoff_low_point`
- `thermal_scan`
- `unknown`

Suggested initial `exposure_bias_flags` values:

- `hvac_possible`
- `kitchen_adjacent`
- `garage_adjacent`
- `direct_sun_possible`
- `under_eave`
- `not_runoff_representative`

## Parcel priors fields

The parcel-prior surface now supports a mixed model: coarse categorical classes for
baseline interpretation plus parcel metadata fields that let the inference engine
derive auditable flood and wildfire priors.

Baseline categorical fields:

- `heat_retention_class`
- `runoff_tendency_class`
- `smoke_exposure_class`

Suggested initial enum for those classes:

- `low`
- `moderate`
- `high`
- `unknown`

Flood-prior metadata fields:

- `fema_zone`
- `foundation_type`
- `first_floor_elev_ft`
- `base_flood_elev_ft`
- `year_built`
- `dist_to_water_ft`

Wildfire / smoke-prior metadata fields:

- `zone_zero_clearance_class`
- `defensible_space_class`
- `roof_class`
- `exterior_class`
- `vent_class`
- `window_class`
- `dist_to_wildland_ft`

Interpretation rule:

- parcel metadata should set prior probabilities and priors should remain
  inspectable as separate factors rather than disappearing into a single opaque score

## Divergence tracking fields

`divergence_tracking` is an optional parcel-scoped helper object for carrying
rolling persistence and concordance hints into the inference cycle.

Useful per-parameter fields:

- `persistence_minutes`
- `num_concordant_sensors`

This field is not raw telemetry history. It is a bounded runtime hint so the
inference engine can distinguish a brief mismatch from a sustained hyperlocal
signal.

## v1.5 extension fields

### `structure_response_profile`

Optional slow-changing building characteristics that affect how the house responds to outside conditions.

Useful fields:
- orientation or dominant exposure
- HVAC type
- filter-path class or filter size
- higher-MERV support posture
- cooling and filtration availability where it changes recommendation quality

### `site_dependency_profile`

Optional parcel and access context that matters for route, runoff, and resilience planning.

Useful fields:
- drainage path notes
- low-point or curb-cut relationship
- primary route posture
- backup power availability
- known infrastructure dependencies

### `known_protective_capabilities`

Optional parcel-level protective capacities that are not yet a control interface inventory.

Useful fields:
- recirculation available
- purifier present
- backup power present
- motorized shades present
- pump or sump present

### `known_vulnerable_zones`

Optional list of rooms, facades, low points, or route segments that repeatedly matter for interpretation.

## Planned v1.5 companion surfaces (taxonomy)

The JSON example above stays the **parcel-context** center of gravity. Additional **v1.5** evidence and logs should usually appear as **separate support objects** (not stuffed into one mega-record) so the core parcel-state contract stays stable.

Canonical names and staging: `../../architecture/system/node-taxonomy.md`.

| Surface | Role |
| --- | --- |
| Indoor response evidence | Indoor PM2.5, temperature, RH — planned hardware family `indoor-response-node` or equivalent normalized observations |
| Power and outage evidence | Mains up/down, backup power posture — planned `power-outage-node` or adapters |
| Equipment-state (read-side) | Observed HVAC mode, fan, recirculation, purifier, shade, sump/pump signals — often via adapters |
| Action log | What the household or building did in response to a hazard or guidance cue |
| Outcome / response verification | Whether actions improved observed conditions over bounded windows (for example smoke-related indoor PM over 30–90 minutes) |
| Building-and-site metadata | Overlaps the optional `structure_response_profile`, `site_dependency_profile`, and related fields in this doc |

**Controls-compatibility inventory** (full per-parcel integration matrix) is **v2.5-first** even when draft schemas ship early for experimentation.

## Planned deployment-maturity extensions

To keep the current parcel-context baseline small, the repo may later split richer installation and service facts into a dedicated deployment-metadata companion object.

Future installation extensions likely include:

- `mount_type`
- `orientation_class`
- `sun_exposure_class`
- `airflow_exposure_class`
- `enclosure_revision`
- `power_source_type`
- `storage_type`
- `maintenance_status`
- `last_maintenance_at`
- `install_photo_refs`

Future deployment-quality handling may also add:

- `deployment_quality_class`
- `deployment_quality_reasons`

These fields are valuable for trust and field operations, but they should not silently inflate the current implemented parcel-context contract.

## Interpretation rules

- A node reading is a point observation, not a parcel-wide condition.
- `location_mode` and `install_role` constrain what hazards the node may influence.
- `indoor` and `sheltered` nodes may contribute evidence, but should not be treated as direct parcel-wide outdoor truth.
- `runoff_low_point` context is required before flood-node observations can support stronger runoff or accumulation claims.
- Missing parcel priors should not be silently replaced with assumed values.
- Parcel metadata may inform auditable priors, but those priors should remain
  separable from direct sensor evidence.
- Divergence tracking should help confirm persistence, not substitute for the
  underlying measurements.
- `v1.5` extension fields should improve building-response and recommendation quality, not silently inflate hazard confidence on their own.

## MVP usage rules

- The first MVP may attach one bench-air-node to one parcel with minimal site profile information.
- If parcel context is missing, the inference engine should lower confidence and favor `unknown` outputs.
- Parcel context should be editable without rewriting raw observations.

## Follow-up additions

- parcel geometry linkage
- building-entry-point metadata
- canopy and shade context
- drainage-path annotations
- install-photo references
- explicit deployment-quality metadata

## Related docs

- `deployment-metadata-schema.md`
- `node-registry-schema.md`
- `../../architecture/system/node-taxonomy.md`
- `../../architecture/system/version-and-promotion-matrix.md`
- [`parcel-kit/parcel-installation-checklist.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/parcel-installation-checklist.md)
