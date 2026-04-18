# Contributing to oesis-contracts

Thank you for your interest in contributing to OESIS contracts. This repository defines the machine-verifiable shapes and prose that describe how data flows between OESIS services. Schema changes ripple across the runtime, the public site, and downstream consumers — so the contribution process is intentionally more structured than for pure documentation.

For project-wide governance and process, see the [CONTRIBUTING.md](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/CONTRIBUTING.md) in oesis-program-specs.

## Two contribution tracks

This repository contains two kinds of assets under different licenses:

| Track | Assets | License | Examples |
|-------|--------|---------|----------|
| Schema + example | JSON Schema docs, example payloads | AGPL-3.0+ | `v1.0/schemas/trust-score.schema.json`, `v1.0/examples/trust-score.example.json` |
| Prose | Schema prose, READMEs, governance notes | CC BY-SA 4.0 | `v1.0/trust-score-schema.md`, `v1.0/README.md` |

Match your contribution's license to the asset class.

## Lane discipline

Contracts follow the OESIS lane model. Before adding or modifying a schema, decide which lane owns it:

- **v0.1** — baseline. Changes to v0.1 are breaking for every lane that inherits from it.
- **v0.2 – v0.5** — overlay lanes. These inherit from v0.1; runtime adds test-fixture overlays, but schemas in this repo for these lanes stay empty.
- **v1.0** — fielded additive lane. New schemas for trust scoring, deployment metadata, and multi-node composition go here.
- **v1.5** — bridge additive lane. New schemas for house-state, equipment-state, intervention events, and verification outcomes go here.

If you are unsure which lane, open an issue first.

## Schema change requirements

Every non-trivial schema change must ship with:

1. An updated example payload that validates against the revised schema
2. A matching runtime PR that mirrors the change under `oesis/assets/v*/`
3. A passing `make cross-repo-sync` run from `oesis-program-specs/`
4. An updated prose `*-schema.md` document if the change affects field semantics, not just field presence

Pure typo fixes in prose docs do not require a runtime PR.

## Validation

Before submitting, run at minimum:

```bash
# Syntax check all JSON files
find . -name "*.json" -exec python3 -m json.tool {} \; >/dev/null

# Full cross-repo consistency check (from oesis-program-specs)
cd ../oesis-program-specs
make cross-repo-sync
```

## Commit style

Short, imperative, scoped:

- `feat(v1.0): add deployment_grade field to parcel-state schema`
- `fix(v0.1): correct example payload for evidence-summary`
- `docs(v1.5): clarify intervention-event recurrence semantics`
