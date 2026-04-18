# Schema Migration: v0.1 → v1.0

## Purpose

Document the additive field changes between v0.1 baseline schemas and v1.0
overlay schemas so developers can handle both versions gracefully.

## Migration principle

All v1.0 changes are **additive**. v0.1 payloads remain valid against v1.0
schemas because new fields are optional. Clients that produce v0.1 payloads do
not need to change unless they want to use new v1.0 features.

## Changed schemas

### equipment-state-observation.schema.json

**Added field:** `fusion_hint` (optional)

| Field | Type | Values | Purpose |
| --- | --- | --- | --- |
| `fusion_hint` | string enum | `prefer_local`, `prefer_adapter`, `fallback_only`, `none` | Tells the inference engine which equipment-state source to prefer when multiple sources exist for the same signal |

**Migration:** Omit `fusion_hint` to get default behavior (inference engine uses
its own source-priority logic). Include it only when the parcel operator or
adapter integration has a specific preference.

**v0.1 compatibility:** A v0.1 payload without `fusion_hint` is valid against
the v1.0 schema.

### source-provenance-record.schema.json

**Added field in record items:** `used_inference_stage` (optional)

| Field | Type | Values | Purpose |
| --- | --- | --- | --- |
| `used_inference_stage` | string enum | `baseline`, `bridge`, `adaptation`, `unknown` | Tags which inference stage consumed this signal, useful for v1.5 bridge audit |

**Migration:** Omit `used_inference_stage` for v0.1-era records. The inference
engine populates it automatically when producing provenance records in v1.0+
mode.

**v0.1 compatibility:** A v0.1 record item without `used_inference_stage` is
valid against the v1.0 schema.

### consent-record, consent-store, sharing-settings, sharing-store

**Changes:** `$id` and `title` updated to include `v1.0` in the identifier path.
No structural field changes. These are namespace-only updates for schema
resolution.

**Migration:** No payload changes required. The v1.0 schemas accept the same
payloads as v0.1.

## Overlapping schemas summary

| Schema | v0.1 → v1.0 change | Breaking? | Action needed |
| --- | --- | --- | --- |
| `equipment-state-observation` | Added optional `fusion_hint` | No | None required |
| `source-provenance-record` | Added optional `used_inference_stage` in record items | No | None required |
| `consent-record` | `$id` and `title` updated | No | None |
| `consent-store` | `$id` and `title` updated | No | None |
| `sharing-settings` | `$id` and `title` updated | No | None |
| `sharing-store` | `$id` and `title` updated | No | None |

## Runtime lane behavior

When `OESIS_RUNTIME_LANE=v1.0`, the runtime loads v1.0 overlay schemas where
they exist. When `OESIS_RUNTIME_LANE=v0.1`, only v0.1 baseline schemas are
used. The runtime never rejects a v0.1 payload when running in v1.0 mode.

## Related docs

- `schemas/README.md` — v1.0 schema directory index
- `../v0.1/schemas/` — frozen v0.1 baseline
- `../../program/operating-packet/00-version-labels-and-lanes.md` — lane glossary
