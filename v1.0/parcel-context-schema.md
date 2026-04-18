# Parcel Context Schema v1.0 Direction

## Purpose

Describe the target-lane role of parcel context without mutating the frozen
`../v0.1/` contract docs.

## Core rule

`parcel-context` remains the parcel-centered metadata anchor, but it is not
where every future support surface should be stuffed.

The stronger target lane should keep:

- parcel context as the center of gravity for stable parcel and site metadata
- bridge-stage support objects as separate first-class records

## Why this matters

The next important product move is not simply a wider outdoor sensor stack.
The next move is the bridge from hazard sensing to house state, action, and
verified outcome.

That means parcel context should work alongside, not instead of:

- indoor response evidence
- power and outage evidence
- equipment-state adapters
- action logs
- outcome / response verification

## What belongs in parcel context

Parcel context should continue to hold stable or slowly changing facts such as:

- parcel identity and role metadata
- structure characteristics
- orientation and exposure
- drainage and low-point clues
- vent and filter-path constraints
- dependency and vulnerability metadata

## What should usually stay separate

These should usually land as companion support surfaces rather than as fields
stuffed into one mega-record:

- indoor response observations
- power and outage observations
- read-side equipment-state snapshots
- action-log entries
- verification-outcome records
- later controls compatibility inventory

## Building-and-site metadata surface

The target lane should make `building-and-site-metadata-surface` explicit as a
first-class architecture surface even when much of its content overlaps the
parcel-context family.

Practical rule:

- keep stable parcel metadata here
- move higher-churn operational, deployment, or response records into companion
  objects

## Stage mapping

- `current v1`: parcel context supports parcel sensing and inference
- `v1.5`: parcel context works beside indoor response, outage, equipment-state,
  action, and verification support objects
- `v2.5`: fuller controls compatibility may reference parcel context but should
  remain its own surface
- `v4`: route and community overlays may consume parcel context without turning
  parcel context into a route model

## First closed-loop priority

The first serious closed-loop proof remains smoke response:

- outdoor evidence
- indoor response evidence
- building and filter metadata
- action logging
- bounded verification window

## Related

- `README.md`
- `../../architecture/system/product-requirements-phase-1.md`
- `../../architecture/system/node-taxonomy.md`
- `../../architecture/system/architecture-gaps-by-stage.md`
