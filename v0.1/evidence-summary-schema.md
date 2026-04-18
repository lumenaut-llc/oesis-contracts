# Evidence Summary Schema

## Purpose

Define a parcel-platform-safe evidence summary object derived from the parcel-state snapshot. This gives UI and API consumers a stable explanation/provenance surface without requiring them to reinterpret the full parcel-state contract.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `parcel-state-schema.md`
- `explanation-payload-schema.md`
- `../../software/parcel-platform/interfaces.md`

## Minimum evidence-summary object

```json
{
  "parcel_id": "parcel_123",
  "computed_at": "2026-03-30T19:46:00Z",
  "evidence_mode": "insufficient",
  "inference_basis": "insufficient",
  "confidence": 0.30,
  "headline": "Estimate uses limited local evidence with low parcel certainty.",
  "confidence_band": "low",
  "top_drivers": [
    "Indoor gas-resistance trend shows a moderate change."
  ],
  "top_limitations": [
    "The local node is indoor and does not represent parcel-wide outdoor conditions.",
    "No flood-capable local sensor or public flood context is present."
  ],
  "source_breakdown": {
    "local": true,
    "shared": false,
    "public": false,
    "parcel_context": false,
    "system": true
  },
  "grouped_contributions": {
    "local": [],
    "shared": [],
    "public": [],
    "parcel_context": [],
    "system": []
  },
  "source_modes": [
    "dwelling_node"
  ],
  "freshness": {
    "latest_observation_at": "2026-03-30T19:45:00Z",
    "seconds_since_latest": 60,
    "stale": false
  }
}
```

## Field notes

- `headline`
  The top-level explanation line appropriate for compact UI rendering.
- `top_drivers`
  The highest-weight driver contributions from the explanation payload.
- `top_limitations`
  The highest-weight limitation contributions from the explanation payload.
- `grouped_contributions`
  Contribution objects grouped by source class so clients can render evidence cards without recomputing grouping logic.
- `system`
  A reserved source class for engine-detected absences or interpretation limits that are not themselves evidence sources.
- `source_modes`
  High-level provenance classes used in the underlying parcel-state decision.

## Design rules

- Evidence summary is derived from parcel-state and should not invent new inference.
- The shape should stay safe for dwelling-facing UI by default.
- Grouping and ordering should remain stable as new contribution types are added.
