# OESIS Contracts

Canonical schemas, examples, and contract prose for the [Open Environmental Sensing and Inference System (OESIS)](https://github.com/lumenaut-llc/oesis-program-specs). This repository is the source of truth for the data shapes that flow between OESIS services — nodes, ingest, inference, parcel-platform, and shared-map.

## What's in here

| Path | Contents |
|------|----------|
| [`v0.1/`](v0.1/) | Baseline lane: bench-air node observations, consent, sharing, rights requests, operator access |
| [`v0.2/`](v0.2/) — [`v0.5/`](v0.5/) | Overlay lanes (inherit v0.1 baseline; runtime adds test-fixture overlays) |
| [`v1.0/`](v1.0/) | Fielded lane: trust scoring, multi-node composition, deployment metadata. Planned: observation-schema admissibility facts per [`calibration-program.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/calibration-program.md) §C — tracked as gap G17 |
| [`v1.5/`](v1.5/) | Bridge lane: house-state, equipment-state, intervention events, verification outcomes. Adapter-derived observation facts per [`adapter-trust-program.md`](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/architecture/system/adapter-trust-program.md) §C land here — tracked as gap G18 |
| [`bundles/contracts-bundle/`](bundles/contracts-bundle/) | Published snapshot for downstream consumers |
| [`LANE-INDEX.md`](LANE-INDEX.md) | Detailed lane-by-lane navigation |

Each lane directory contains:

- `*.schema.md` — human-readable schema prose
- `schemas/*.schema.json` — machine-verifiable JSON Schema documents
- `examples/*.example.json` — canonical example payloads that validate against the schemas

## Lane model

Contracts follow the same lane model as the runtime. Canonical examples live here for **v0.1**, **v1.0**, and **v1.5**; overlay lanes v0.2–v0.5 inherit from v0.1 and add their overlays only inside the runtime's test fixtures.

## Consumers

| Repository | How it consumes contracts |
|------------|---------------------------|
| [oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime) | Mirrors examples under `oesis/assets/v*/examples/`; hand-codes validators per lane; parity enforced by `cross_repo_sync_check.py` in oesis-program-specs |
| [oesis-public-site](https://github.com/lumenaut-llc/oesis-public-site) | Consumes public-safe content via the `public-content-bundle` published by oesis-program-specs |
| [oesis-program-specs](https://github.com/lumenaut-llc/oesis-program-specs) | References contracts from architecture, release, and governance docs via absolute GitHub URLs |
| External downstream | Pulls [`bundles/contracts-bundle/`](bundles/contracts-bundle/) as a pinned snapshot with its own manifest |

See [`CONSUMING.md`](CONSUMING.md) for the full consumer guide — lane selection, validation patterns, sync discipline, and the step-by-step dev loop for adding a new contract.

## Validation

Quick syntax check of all example payloads:

```bash
find . -name "*.example.json" -exec python3 -m json.tool {} \; >/dev/null
```

Full cross-repo consistency check (run from oesis-program-specs):

```bash
cd ../oesis-program-specs
make cross-repo-sync
```

## Sibling repositories

| Repository | What it contains |
|---|---|
| [oesis-program-specs](https://github.com/lumenaut-llc/oesis-program-specs) | Architecture, governance, release materials |
| [oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime) | Python reference services |
| [oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware) | Sensor node specs, firmware, BOMs |
| [oesis-public-site](https://github.com/lumenaut-llc/oesis-public-site) | Public preview website |

## License

This repository uses a dual-license model matching the rest of the OESIS program:

- **Schema and example JSON files** (`*.schema.json`, `*.example.json`) — AGPL-3.0
- **Prose documentation** (`*.md`) — CC BY-SA 4.0

See [`LICENSES.md`](LICENSES.md) for details and [`NOTICE.md`](NOTICE.md) for the release boundary.
