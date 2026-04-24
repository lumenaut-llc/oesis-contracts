# Source Provenance Record Schema (v1.0 lane variant)

## Purpose

Document the v1.0 lane variant of `source-provenance-record` — provides per-signal confidence and freshness metadata for observations crossing the v1.0 governance boundary.

This is **not** a replacement for the v0.1 baseline schema. It is an additive lane variant per the additive-lane pattern in [`README.md`](README.md).

## What v1.0 adds

The v1.0 schema (`schemas/source-provenance-record.schema.json`) extends the v0.1 baseline with v1.0-specific fields needed for governance enforcement:

- per-signal confidence and freshness metadata
- linkage to adapter/source authority records (per [`adapter-trust-program.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/adapter-trust-program.md))
- alignment with the v1.0 governance contract surface (per [`governance-operational-model.md`](governance-operational-model.md))

See the schema JSON for the full field-by-field contract.

## Lane relationship

v1.5 also has a `source-provenance-record` schema variant ([`../v1.5/source-provenance-record-schema.md`](../v1.5/source-provenance-record-schema.md)) for bridge-stage support objects. Like `equipment-state-observation`, the v1.0 and v1.5 variants evolve independently along parallel axes — pick the lane that matches your use case.

## Related

- [`../v0.1/source-provenance-record-schema.md`](../v0.1/source-provenance-record-schema.md) — baseline
- [`../v1.5/source-provenance-record-schema.md`](../v1.5/source-provenance-record-schema.md) — v1.5 bridge-stage variant
- `schemas/source-provenance-record.schema.json` — v1.0 schema JSON
- `examples/source-provenance-record.example.json` — v1.0 example
