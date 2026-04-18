# Public Context Schema

## Purpose

Define the first minimal contract for public external context used by the inference engine to support parcel estimates when local evidence is sparse or incomplete.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `node-observation-schema.md`
- `parcel-state-schema.md`
- `evidence-mode-and-observability.md`
- `../../software/inference-engine/interfaces.md`

## Content

## Why this contract exists

The repo already assumes public context may support parcel inference, but the MVP scaffolding has not yet defined a concrete machine-readable example for that evidence.

This contract is intentionally small. It is not a full feed-ingest standard. It is the first reference object the inference engine can consume alongside local node evidence.

## Minimum public-context object

```json
{
  "context_id": "pubctx_example_0001",
  "source_kind": "public_context",
  "source_name": "demo_regional_weather_air",
  "observed_at": "2026-03-30T19:40:00Z",
  "coverage_mode": "regional",
  "parcel_id": "parcel_demo_001",
  "hazards": {
    "smoke_probability": 0.18,
    "heat_probability": 0.36,
    "flood_probability": 0.04
  },
  "summary": [
    "Regional conditions suggest modest heat concern.",
    "Regional smoke conditions are present but not severe."
  ]
}
```

## Required fields

- `context_id`
- `source_kind`
- `source_name`
- `observed_at`
- `coverage_mode`
- `parcel_id`
- `hazards`
- `summary`

## Field notes

- `source_kind`
  Must remain `public_context` for the MVP.
- `source_name`
  Short identifier for the external source bundle or derived source product.
- `coverage_mode`
  Suggested initial enum: `regional`, `subregional`, `parcel_adjacent`
- `hazards`
  Hazard-supporting scores on the same 0 to 1 scale used by parcel-state outputs.
- `summary`
  Human-readable context fragments suitable for explanation output and audit review.

## Design rules

- Public context should support inference, not silently replace local evidence.
- Public context must carry its own freshness timestamp.
- Public context may influence parcel-state outputs even when local evidence is weak, but confidence should remain constrained when local confirmation is absent.
- Public context should be traceable in provenance and reasons.

## MVP usage rules

- The first reference pipeline may use one or more public-context objects per inference run.
- Public-context objects may be merged upstream or passed as separate inputs to the inference scaffold.
- The first public-context objects may be hand-authored or adapter-derived example data rather than live feeds.
- If public context is absent, the inference engine should still produce a valid parcel-state output.

## Follow-up additions

- freshness expiry
- geometry or cell references
- source licensing metadata
- confidence or quality fields from the public source
- multiple public evidence layers in one inference run
