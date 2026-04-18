# OESIS Contracts Notice

## Purpose

This notice explains how to read this subtree during the current OESIS release period.

## License direction

This repository uses a dual-license model:

- **Prose documentation** (`*.md`) — **CC BY-SA 4.0**
- **Schemas and examples** (`*.schema.json`, `*.example.json`) — **GNU AGPL v3 or later**

See [`LICENSE`](LICENSE) for the AGPL text and [`LICENSES.md`](LICENSES.md) for the full license split.

## Release boundary

During the current release period:

- approved schemas, examples, and contract prose may be public under their attached notices and licenses
- publication of a schema does not mean every call site or downstream consumer is approved for public release
- exact release scope should be checked against program-level notices and non-release controls in [oesis-program-specs](https://github.com/lumenaut-llc/oesis-program-specs)

## Safety and claims boundary

Contract schemas describe data shapes, not operational guarantees.

Nothing in this subtree should be read as a guarantee of data accuracy, calibration, retention, or field suitability. Those guarantees live in deployment-time governance, trust-score, and operator documentation — not in the schemas themselves.

## Source of truth for schema changes

- this repository is the canonical source for schema + example shapes
- `oesis-runtime` mirrors these under `oesis/assets/v*/` for offline acceptance tests; parity is enforced by `cross_repo_sync_check.py` in `oesis-program-specs`
- any schema change must ship with a matching runtime PR and a passing `make cross-repo-sync` before merge
