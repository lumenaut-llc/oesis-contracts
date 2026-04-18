# Trust Score Schema v1.0

## Purpose

Define a per-parcel trust-score object that composes signal-level quality
factors (freshness, node health, calibration state, install quality) into an
auditable measurement-trust assessment.

## Status

Specified. Not yet implemented in the inference path.

## Why this object exists

Confidence bands (`high`, `medium`, `low`) already appear on individual
source-provenance records and equipment-state observations. But no object
currently composes those per-signal judgments into a parcel-level trust
posture that operators and downstream consumers can inspect.

Without a trust-score object:

- freshness penalties are applied silently inside the inference engine
- node health degradation affects output confidence without explanation
- operators cannot distinguish "low confidence because data is stale" from
  "low confidence because the model is uncertain"

The trust-score object makes measurement trust auditable and explainable.

## Scope

This object describes **measurement trust** — confidence in the evidence
feeding parcel-state, not confidence in the parcel-state conclusion itself.
Parcel-state carries its own `confidence` and `evidence_mode` fields for
conclusion-level confidence.

## Core fields

### Required

| Field | Type | Description |
|-------|------|-------------|
| `parcel_id` | string | Parcel this score applies to |
| `scored_at` | datetime | When this score was computed |
| `overall_band` | enum | Composite trust band: `high`, `medium`, `low`, `degraded` |
| `overall_score` | number (0.0–1.0) | Numeric composite; bands map to thresholds |
| `factors` | array | Per-factor breakdown (see below) |

### Factor object (each entry in `factors`)

| Field | Type | Description |
|-------|------|-------------|
| `factor_key` | string | Factor name (see enumerated factors below) |
| `weight` | number (0.0–1.0) | Relative weight in composite score |
| `score` | number (0.0–1.0) | Factor-level score |
| `band` | enum | `high`, `medium`, `low`, `degraded` |
| `reason` | string | Human-readable explanation |

### Optional

| Field | Type | Description |
|-------|------|-------------|
| `node_scores` | array | Per-node trust breakdown when multiple nodes contribute |
| `penalty_log` | array | Ordered list of penalties applied with reason and magnitude |

## Enumerated factors

### 1. Freshness (`freshness`)

Drawn from public-context-freshness-policy and per-node staleness:

- `fresh` (age <= 30 min): score 1.0
- `aging` (30 min – 2 hr): score 0.7
- `stale` (2 hr – 6 hr): score 0.3
- `expired` (> 6 hr): score 0.0

When multiple sources contribute, the composite freshness score is the
**minimum** across all contributing sources — the weakest link governs.

### 2. Node health (`node_health`)

Derived from node health telemetry (wifi_rssi, heap, read failures, uptime):

- All health indicators nominal: score 1.0
- Minor degradation (weak signal, elevated read failures): score 0.7
- Significant degradation (frequent failures, low heap): score 0.3
- Node offline or unresponsive beyond TTL: score 0.0

### 3. Calibration state (`calibration_state`)

Derived from node-registry calibration_state field:

- `verified`: score 1.0
- `provisional`: score 0.6
- `needs_service`: score 0.2
- `unsupported`: score 0.0

### 4. Install quality (`install_quality`)

Derived from deployment-metadata (when available):

- Field-validated install with verified mount and exposure: score 1.0
- Standard install without field validation: score 0.7
- Provisional or bench-only deployment: score 0.4
- No deployment metadata available: score 0.5 (neutral — absence is not penalty)

### 5. Source diversity (`source_diversity`)

Measures whether parcel-state is supported by multiple independent evidence
sources:

- Local node + public context + shared signal: score 1.0
- Local node + public context: score 0.8
- Local node only: score 0.6
- Public context only: score 0.3

## Composite scoring

The overall score is a weighted sum of factor scores:

```
overall_score = sum(factor.weight * factor.score) / sum(factor.weight)
```

Default weights (configurable per deployment):

| Factor | Default weight |
|--------|---------------|
| freshness | 0.30 |
| node_health | 0.25 |
| calibration_state | 0.20 |
| install_quality | 0.10 |
| source_diversity | 0.15 |

Band thresholds:

| Band | Score range |
|------|------------|
| `high` | >= 0.75 |
| `medium` | 0.50 – 0.74 |
| `low` | 0.25 – 0.49 |
| `degraded` | < 0.25 |

## Penalty log

When a factor score drops below `medium`, the trust-score object should
record the penalty in `penalty_log`:

```json
{
  "factor_key": "freshness",
  "penalty": 0.30,
  "reason": "Primary public context source is stale (age: 3h 42m)",
  "applied_at": "2026-04-14T15:30:00Z"
}
```

This allows operators to trace exactly why trust degraded without reading
inference internals.

## Recomputation

Trust scores are recomputed:

- on each parcel-state inference cycle
- when node health telemetry changes materially (state transition, not noise)
- when deployment metadata is updated

Trust scores are **not** persisted historically by default. The current score
is the relevant score. Historical trust trends are derivable from
observation-level provenance records.

## Relationship to parcel-state

The trust score informs but does not replace parcel-state confidence:

- Parcel-state `confidence` reflects conclusion-level certainty (model output)
- Trust score `overall_band` reflects evidence-level quality (input quality)
- When trust is `degraded`, parcel-state confidence should be capped at `low`
  regardless of model output
- When trust is `low`, parcel-state explanation should note measurement trust
  as a limiting factor

## Design rules

- Trust scores are read-side only — they do not gate data ingestion
- Factor weights are externalized configuration, not hardcoded
- Band thresholds are externalized configuration
- Absence of deployment metadata is neutral (score 0.5), not penalizing —
  early parcels without install records should not be artificially degraded
- The penalty log is append-per-cycle, not append-forever — it resets on
  each recomputation

## Related

- `../v0.1/node-registry-schema.md` (calibration_state source)
- `deployment-metadata-schema.md` (install_quality source)
- `source-provenance-record-schema.md` (per-signal confidence and staleness)
- `../../software/inference-engine/public-context-freshness-policy.md`
  (freshness band definitions)
