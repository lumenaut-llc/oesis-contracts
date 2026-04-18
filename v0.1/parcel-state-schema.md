# Parcel State Schema

## Purpose

Define the canonical parcel-level output produced by the inference engine for dwelling-facing use and downstream mapping.

## Version boundary

This schema represents the current `v1` parcel sensing and inference baseline.

It stays additive through `v1.5` so the repo can add house-state, coarse
capability / equipment-state, intervention, and verification objects without
forcing a breaking parcel-state redesign.

Narrative aliases such as `stay_safe`, `enter_safe`, `escape_safe`, and `asset_safe` may appear in planning documents, but the current repo keeps the existing field names through at least `v2`.

## Hazard, functional, and response (conceptual)

This contract **compresses** what the layered blueprint separates as **hazard-oriented**
reasoning and **functional / operational** meaning:

- **`hazards`** (e.g. smoke, flood, heat probabilities) and fused environmental
  estimates support **hazard state**—what the environment is believed to be doing,
  with confidence and evidence discipline.
- **`shelter_status`**, **`reentry_status`**, **`egress_status`**, and
  **`asset_risk_status`** express **functional** interpretation: what those
  conditions mean for shelter, movement, and asset exposure at parcel scope—not
  official alerts or guarantees.

**Response state** (actions taken, interventions, verification, adaptation
learning) is **not** carried in this object. Program-phase **`v1.5`** and later add
**separate support objects** (house state, intervention events, verification
outcomes) so response quality does not inflate hazard confidence. See **Planned
follow-on additions** below and `../../program/operating-packet/functional-state-and-response-model.md`.

## Core status fields

- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`
- `confidence`
- `evidence_mode`
- `inference_basis`
- `reasons`

Suggested initial enum for status fields:
- `safe`
- `caution`
- `unsafe`
- `unknown`

Suggested initial enum for `evidence_mode`:
- `local_only`
- `local_plus_public`
- `public_only`
- `insufficient`

Suggested initial enum for `inference_basis`:
- `local_only`
- `local_plus_shared`
- `local_plus_public`
- `local_plus_shared_plus_public`
- `public_only`
- `shared_only`
- `shared_plus_public`
- `insufficient`

## v0.1 acceptance-bar subset

All supporting values below are **structurally required** by the JSON schema
(`parcel-state.schema.json`) — the inference engine always emits them, and
`make oesis-validate` enforces their presence.

However, the `v0.1` **acceptance criteria** (`v0.1-acceptance-criteria.md`,
criterion 4) inspect the quality and meaning of only the **core status fields**
plus **confidence**, **evidence mode**, **reasons**, **freshness**, and
**provenance summary**. The remaining fields are carried structurally but their
content quality is not gated until the richer explanation and divergence
surfaces are exercised from `v0.2` onward.

See `../../architecture/current/minimum-functioning-v0.1.md` for the canonical
minimum-functioning definition.

## Supporting values

- `smoke_probability`
- `flood_probability`
- `heat_probability`
- `explanation_payload`
- `hazard_statuses`
- `parcel_priors_applied` *(quality not gated until v0.2+)*
- `divergence_records` *(quality not gated until v0.2+)*
- `public_only_counterfactual` *(quality not gated until v0.2+)*
- `contrastive_explanations` *(quality not gated until v0.2+)*
- `freshness`
- `provenance_summary`

## v0.1 minimum subset

The **v0.1 acceptance bar** (`minimum-functioning-v0.1.md`) requires only these
fields to be present and quality-gated:

- Core statuses: `shelter_status`, `reentry_status`, `egress_status`, `asset_risk_status`
- `confidence`
- `evidence_mode`
- `reasons`
- `freshness`
- `provenance_summary`

All other fields (`parcel_priors_applied`, `divergence_records`,
`public_only_counterfactual`, `contrastive_explanations`, `explanation_payload`,
`hazard_statuses`, hazard probabilities) are present in the schema for
forward-compatibility and inference auditability, but their **quality is not
gated until v0.2+** (see annotations in Supporting values above). Developers
targeting v0.1 should implement the subset above first.

## Minimum parcel-state object

```json
{
  "parcel_id": "parcel_demo_001",
  "computed_at": "2026-03-30T19:46:00Z",
  "shelter_status": "unknown",
  "reentry_status": "unknown",
  "egress_status": "unknown",
  "asset_risk_status": "unknown",
  "confidence": 0.69,
  "evidence_mode": "local_plus_public",
  "inference_basis": "local_plus_public",
  "explanation_payload": {
    "headline": "Estimate uses local plus public evidence with medium confidence.",
    "basis": {
      "evidence_mode": "local_plus_public",
      "inference_basis": "local_plus_public",
      "confidence_band": "medium"
    },
    "drivers": [
      "Local temperature_c diverged from demo_regional_weather_v1 by 7.6 (local_depressed, sustained).",
      "Regional conditions suggest modest heat concern."
    ],
    "limitations": [
      "Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions.",
      "Regional or neighborhood heat context is stronger than the local node reading, so parcel heat interpretation remains cautious."
    ],
    "evidence_contributions": [
      {
        "contribution_id": "parcel_smoke_prior",
        "source_class": "parcel_context",
        "source_name": "parcel_demo_001",
        "role": "driver",
        "summary": "Parcel metadata sets a smoke prior at 0.30 from exposure class 'high'.",
        "hazards": ["smoke"],
        "weight": 0.24,
        "visibility": "dwelling_safe"
      },
      {
        "contribution_id": "divergence_pm25",
        "source_class": "system",
        "source_name": "demo_regional_smoke_v1",
        "role": "driver",
        "summary": "Local pm25 diverged from demo_regional_smoke_v1 by 19.8 (local_depressed, persistent).",
        "hazards": ["smoke"],
        "weight": 0.42,
        "visibility": "dwelling_safe"
      }
    ],
    "source_breakdown": {
      "local": true,
      "shared": false,
      "public": true,
      "parcel_context": true,
      "system": true
    },
    "divergence_summary": [
      "Public data alone would have classified smoke as 'safe' (p=0.31), while fused parcel inference classified it as 'safe' (p=0.37)."
    ]
  },
  "reasons": [
    "Parcel metadata sets a smoke prior at 0.30 from exposure class 'high'.",
    "Public data alone would have classified smoke as 'safe' (p=0.31), while fused parcel inference classified it as 'safe' (p=0.37). Local evidence diverged by 19.8 and was local_depressed relative to the regional baseline."
  ],
  "hazards": {
    "smoke_probability": 0.37,
    "flood_probability": 0.03,
    "heat_probability": 0.31
  },
  "hazard_statuses": {
    "smoke": "safe",
    "flood": "unknown",
    "heat": "safe"
  },
  "parcel_priors_applied": {
    "smoke": {
      "probability": 0.30,
      "adjustment": 0.12,
      "summary": "Parcel metadata sets a smoke prior at 0.30 from exposure class 'high'.",
      "factors": [
        {
          "factor": "smoke_exposure_class",
          "value": "high",
          "effect": "baseline_probability",
          "applied_value": 0.12
        }
      ]
    },
    "heat": {
      "probability": null,
      "adjustment": 0.04,
      "summary": "Parcel metadata applies a +0.04 heat prior from retention class 'high'.",
      "factors": []
    },
    "flood": {
      "probability": 0.0263,
      "adjustment": null,
      "summary": "Parcel flood prior resolves to 0.026 from FEMA zone 'AE' and parcel modifiers.",
      "factors": []
    }
  },
  "divergence_records": [
    {
      "timestamp": "2026-03-30T19:45:00Z",
      "sensor_id": "indoor-response-01",
      "parameter": "pm25",
      "local_value": 18.2,
      "regional_value": 38.0,
      "regional_source": "demo_regional_smoke_v1",
      "correction_applied": "none",
      "abs_diff": 19.8,
      "ratio": 0.48,
      "z_score": 2.48,
      "direction": "local_depressed",
      "magnitude": "moderate",
      "persistence_minutes": 190,
      "persistence_class": "persistent",
      "aqi_category_local": "moderate",
      "aqi_category_regional": "usg",
      "aqi_category_diff": -1,
      "num_concordant_sensors": 2,
      "confidence": "medium"
    }
  ],
  "public_only_counterfactual": {
    "hazards": {
      "smoke_probability": 0.31,
      "flood_probability": 0.03,
      "heat_probability": 0.31
    },
    "hazard_statuses": {
      "smoke": "safe",
      "flood": "unknown",
      "heat": "safe"
    },
    "confidence": 0.66
  },
  "contrastive_explanations": [
    {
      "explanation_id": "obs_example_0001:smoke:contrast",
      "timestamp": "2026-03-30T19:46:00Z",
      "hazard_type": "smoke",
      "fact": {
        "conclusion": "safe",
        "hazard_level": "safe",
        "probability": 0.37,
        "confidence": 0.69,
        "data_sources": [
          "local:bench-air-01",
          "parcel_context",
          "public:demo_regional_smoke_v1"
        ]
      },
      "foil": {
        "conclusion": "safe",
        "hazard_level": "safe",
        "probability": 0.31,
        "confidence": 0.66,
        "data_sources": [
          "parcel_context",
          "public:demo_regional_smoke_v1"
        ]
      },
      "contrast": {
        "summary": "Public data alone would have classified smoke as 'safe' (p=0.31), while fused parcel inference classified it as 'safe' (p=0.37).",
        "delta_hazard_level": 0,
        "delta_probability": 0.06,
        "divergence_factors": [
          {
            "factor": "pm25",
            "local_value": 18.2,
            "public_value": 38.0,
            "contribution_delta": 0.06,
            "is_novel_signal": false
          }
        ]
      },
      "verification": {
        "prediction_window_end": "2026-03-30T23:46:00Z",
        "ground_truth_available": false,
        "scores": {
          "brier_score_fact": null,
          "brier_score_foil": null,
          "local_data_added_value": null
        }
      }
    }
  },
  "freshness": {
    "latest_observation_at": "2026-03-30T19:45:00Z",
    "seconds_since_latest": 60,
    "stale": false
  },
  "provenance_summary": {
    "observation_count": 1,
    "source_modes": [
      "dwelling_node"
    ],
    "observation_refs": [
      "obs_example_0001"
    ],
    "support_object_refs": []
  }
}
```

## Field notes

- `confidence`
  Numeric confidence in the parcel-state assessment, not a claim of physical certainty.
- `reasons`
  Human-readable explanation fragments suitable for UI and audit logs.
- `inference_basis`
  Machine-facing evidence-composition field that distinguishes mixed-source combinations more precisely than the dwelling-facing `evidence_mode`.
- `explanation_payload`
  Structured explanation object for UI composition, notification drafting, and audit support.
  Its `drivers` and `limitations` should be derived from weighted `evidence_contributions`, not maintained as unrelated text lists.
  The payload may also include `system` limitations for missing context or other engine-detected absences that are not true source classes.
- `hazard_statuses`
  Hazard-specific status labels derived from the probability fields so a consumer can compare parcel-wide functional status to per-hazard interpretation.
- `parcel_priors_applied`
  Structured explanation of which parcel metadata fields affected baseline probabilities before local sensor fusion.
- `divergence_records`
  Machine-readable local-versus-public mismatch records. These are first-class signals, not mere diagnostics.
- `public_only_counterfactual`
  The public-data-only foil path used for contrastive explanation and later verification.
- `contrastive_explanations`
  Fact-versus-foil explanation objects that make local-data-added value auditable over time.
- `hazards`
  Hazard-specific supporting scores used to derive the status fields.
- `closed_loop_summary`
  Optional derived response summary for the first measured parcel-specific loop,
  such as smoke protection with indoor PM before/after comparison.
- `freshness`
  Explicit recency information so old evidence does not look current.
- `provenance_summary`
  Short reference block pointing to the evidence used for the decision.
  It may optionally include `support_object_refs` when later bridge support
  objects are present alongside the baseline parcel-state evaluation.
- `local_value_summary`
  Optional top-level string that concisely states what the local node
  contributed that public context alone could not provide.
  Example: `"Local PM2.5 (47 ug/m3) is 22 ug/m3 higher than regional estimate, consistent with localized smoke accumulation at this parcel."`
  If no local node evidence exists or local evidence agrees with public
  context, this field should be null or state
  `"Local evidence consistent with regional data; no novel parcel-specific signal detected."`
  This field makes the differentiation between parcel-first and regional
  reasoning immediately visible without requiring consumers to parse nested
  `contrastive_explanations`.

## Design rules

- Parcel-state outputs must remain understandable to a parcel operator.
- Status labels should frame conditions and risk, not imply emergency authorization or guarantees.
- Confidence should fall when evidence is sparse, stale, or conflicting.
- Divergence should remain visible as its own runtime surface so hyperlocal signals are not hidden inside fused probabilities.
- Inference should produce `unknown` when evidence quality is too weak for a stronger claim.
- `evidence_mode` may remain a coarse dwelling-facing summary while `inference_basis` carries the exact source composition for backend use.
- Hazard scores support the parcel-state output but do not replace the parcel operator-readable statuses.
- The parcel-state object may include additive contrastive and verification hooks without changing the top-level functional-status fields.
- Every parcel-state snapshot should be traceable back to source observations.

## Planned follow-on additions

`v1.5`:
- keep parcel-state stable
- store house-state, coarse capability / equipment-state, intervention, and
  verification data as separate support objects

`v2.5`:
- treat full controls-compatibility inventory and bounded-control policy as
  separate later-stage objects rather than backfilling them into parcel-state

`v2` and later may add optional presentation summaries such as:
- bounded recommendations
- actionability notes
- recommendation or verification references

Those additions should not erase the current distinction between condition estimate and later-stage adaptation logic.

## Related docs

- `../../program/operating-packet/functional-state-and-response-model.md` — hazard / functional / response split by phase
- `../../program/operating-packet/05-revised-architecture-blueprint.md` — layered model and impact / functional layer
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` — when objects mature by program phase
- `../../architecture/current/architecture-object-map.md` — enumerated objects (parcel state §9)
- `node-observation-schema.md`
- `parcel-context-schema.md`
- `house-state-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- `explanation-payload-schema.md`
- `../../software/inference-engine/interfaces.md`
- `../../software/parcel-platform/README.md`
