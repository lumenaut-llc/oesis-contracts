# Node Observation Schema (v1.0 lane variant — admissibility facts)

## Purpose

Document the v1.0 lane variant of `node-observation` — adds the six **admissibility-fact** fields that runtime needs to compute the §C admissibility decision per [`calibration-program.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/calibration-program.md).

This is **not** a replacement for the v0.1 baseline schema. It is an additive lane variant per the additive-lane pattern in [`README.md`](README.md). The v0.1 baseline at [`../v0.1/node-observation-schema.md`](../v0.1/node-observation-schema.md) remains unchanged.

## Why this exists (ADR 0009)

Per [ADR 0009](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/meta/adr/0009-admissibility-schema-split-facts-vs-decision.md): **schema carries facts, runtime computes decision**. The facts must be formal schema fields so every consumer sees the same evidence. Before this lane variant, there was no place in the canonical observation to record burn-in state, calibration-session pointers, deployment class, or placement representativeness — so admissibility couldn't be computed deterministically across consumers.

The admissibility *decision* fields (`admissible_to_calibration_dataset`, `admissibility_reasons`) are runtime-computed outputs on the normalized observation. They do **not** appear in this schema.

## What v1.0 adds

The v1.0 schema (`schemas/node-observation.schema.json`) extends v0.1's baseline (12 properties) with six additional fields. All six are **optional** to keep the change forward-compatible — a v0.1-era producer's payload still validates against this schema.

| Field | Type | Purpose |
| --- | --- | --- |
| `burn_in_complete` | boolean | Whether the producing device has cleared the §B burn-in window. Runtime treats absent as `false`. |
| `node_calibration_session_ref` | string | Opaque pointer to the most recent calibration session record (URN, URL, or repo-relative path; format is implementation-defined). Runtime treats absent as "no calibration on file." |
| `node_deployment_maturity` | enum | One of `v0.1` / `v1.0` / `v1.5` / `v2.0` per [`deployment-maturity-ladder.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/deployment-maturity-ladder.md). Runtime treats absent as `v0.1`. |
| `node_deployment_class` | enum | One of `indoor` / `sheltered` / `outdoor` per [`sensor-placement-and-representativeness-guide.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/sensor-placement-and-representativeness-guide.md). |
| `protective_fixture_verified_at` | timestamp \| null | Last verified thermal-loading (or equivalent) test for the protective fixture, or `null` if no fixture is required. |
| `placement_representativeness_class` | `A` \| `B` \| `C` \| `D` \| null | Placement representativeness class per the placement guide. |

### `location_mode` vs `node_deployment_class` — not the same field

These are intentionally separate:

- **`location_mode`** (in v0.1 baseline) is a *producer-side intent declaration* — what the firmware was told about its placement at install time.
- **`node_deployment_class`** (new in v1.0) is a *verified install attribute* — what the deployment audit confirmed and what admissibility logic should use.

In well-installed nodes the two will agree. Disagreement is a real signal: either the firmware was misconfigured or the install differs from intent. Runtime can flag this as an admissibility reason without re-reading the producer's own `location_mode`.

## Versioning posture

- **`schema_version` is unchanged** at `oesis.bench-air.v1`. This is intentional — the v0.1 and v1.0 schemas are versioning the *contract surface*, not the *wire format*. A producer stamping `oesis.bench-air.v1` and including the new fields is still emitting a valid bench-air observation; older consumers ignore unknown fields.
- **Backward compatibility:** every v0.1 example validates against this schema (the new fields are optional).
- **Forward compatibility:** consumers that read this lane should treat any of the six new fields as "may be absent" and apply the runtime fallback rules in calibration-program §C.

## Adapter-derived parallel (not in this schema)

For Tier 1 / Tier 2 adapter sources, the parallel adapter-trust-program §C facts (`adapter_source_ref`, `adapter_contract_version`, `adapter_onboarding_ref`, `adapter_credential_last_verified_at`, `adapter_tier`) land in the v1.5 lane variant. See [`../v1.5/`](../v1.5/) (tracked as gap G18). Runtime branches on `adapter_tier` — if absent or `tier_3_direct`, calibration-program §C applies (this schema's facts); otherwise adapter-trust-program §C applies.

## Variant examples

The v1.0 lane also contains two pre-existing variant examples that share this schema's superset shape:

- `examples/node-observation-mast-lite.example.json` — bench-air with mast-lite radiation shield (still `oesis.bench-air.v1`)
- `examples/node-observation-flood.example.json` — flood-node payload (uses `oesis.flood-node.v1` — different schema; see `flood-observation.schema.json` for that lane's contract)

The mast-lite variant should populate the admissibility facts on the same v1.0 cadence as the canonical example. Flood-observation has its own admissibility surface tracked separately.

## Related

- [ADR 0009 — schema-carries-facts decision](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/meta/adr/0009-admissibility-schema-split-facts-vs-decision.md)
- [Calibration program §C](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/calibration-program.md)
- [Adapter-trust program §C](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/adapter-trust-program.md)
- [`../v0.1/node-observation-schema.md`](../v0.1/node-observation-schema.md) — baseline (no admissibility facts)
- [`schema-migration-v0.1-to-v1.0.md`](schema-migration-v0.1-to-v1.0.md) — migration notes for runtime
- `schemas/node-observation.schema.json` — v1.0 schema JSON
- `examples/node-observation.example.json` — v1.0 canonical example with all six fields populated
