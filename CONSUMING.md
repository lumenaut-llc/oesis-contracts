# Consuming OESIS Contracts

This guide explains how to use the schemas, examples, and contract prose in this repository when building or integrating an OESIS-adjacent service. Read this before writing code that produces or consumes OESIS data.

## Audience

- New contributors to [`oesis-runtime`](https://github.com/lumenaut-llc/oesis-runtime) adding a normalizer, inference module, or governance check
- Authors of new sibling services (e.g., a future adapter daemon, analytics consumer)
- External downstream consumers pulling the published contract bundle
- Authors of architecture or release docs referencing contract fields

## The consumption model — three distinct patterns

```text
oesis-contracts (source of truth for data shape)
    │
    ├── runtime validators (oesis-runtime)  ← hand-coded Python per lane
    ├── test fixtures      (oesis-runtime)  ← examples mirrored from here
    ├── bundle snapshot    (bundles/)       ← for external consumers
    └── doc references                      ← GitHub absolute URLs
```

**This repository is the source of truth for data shape.** Nothing ingests-or-emits OESIS data without conforming to it. But each consumer type uses it differently.

## Lane selection — which version to target

| Use case | Lane |
|---|---|
| v0.1 reference pipeline (bench-air) | [`v0.1/`](v0.1/) |
| v0.2-v0.5 runtime slices (widened kit, flood, registry, governance) | [`v0.1/`](v0.1/) — overlays inherit baseline |
| Fielded stack (trust scoring, multi-node, deployment metadata) | [`v1.0/`](v1.0/) adds; [`v0.1/`](v0.1/) for baseline |
| Bridge stage (house-state, intervention, verification, equipment-state) | [`v1.5/`](v1.5/) adds; [`v0.1/`](v0.1/) for baseline |
| External downstream consumers | [`bundles/contracts-bundle/`](bundles/contracts-bundle/) |

**Rule:** always start at the lane that matches your slice. Fall back to v0.1 for anything not explicitly delta'd in your target lane. See [`LANE-INDEX.md`](LANE-INDEX.md) for a detailed lane matrix.

**Never mutate v0.1.** v0.1 is the frozen baseline contract surface. If a v1.0 or v1.5 consumer needs a richer field, add it to that lane — never change v0.1 in place.

## Pattern 1 — Runtime (reference Python implementation)

This is the primary consumer pattern, used by `oesis-runtime`.

### What runtime does NOT do

- It does **not** re-import `.schema.json` files from oesis-contracts at runtime
- It does **not** depend on `jsonschema` library at the ingest boundary
- It does **not** duplicate schema content

### What runtime DOES do

1. **Hand-codes validators** per observation type. Example from `oesis-runtime/oesis/ingest/v0_1/validate_examples.py`:

   ```python
   def validate_node_observation(payload):
       required = ["schema_version", "node_id", "observed_at", ...]
       for field in required:
           require(field in payload, f"missing field: {field}")
       require(payload["schema_version"] == "oesis.bench-air.v1", ...)
       # per-field checks with domain-specific error messages
   ```

2. **Mirrors example payloads** as test fixtures under `oesis/assets/v*/examples/`. Parity with this repository is enforced by `cross_repo_sync_check.py` in `oesis-program-specs`.

3. **References the contract in docstrings**, from `oesis-runtime/oesis/inference/v1_0/compute_trust_score.py`:

   ```python
   # Contract: https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/trust-score-schema.md
   # Schema:   https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/schemas/trust-score.schema.json
   ```

### Why hand-coded validators

Trade-off chosen by the project:

- **Pro**: tailored error messages, domain-specific constraints beyond schema, no runtime jsonschema dependency
- **Con**: validator drift risk — hand-coded validator must stay in sync with JSON Schema

Drift risk is mitigated at CI time: `scripts/validate_examples.py` in this repo validates every example against its schema using `jsonschema`. If a hand-coded validator in runtime accepts something the schema rejects, the example eventually fails CI.

### Adding a new runtime consumer

When writing new runtime code that handles an OESIS observation:

1. Find the contract you're implementing in the right lane (e.g., `v1.0/schemas/<type>.schema.json`)
2. Copy the matching example into `oesis-runtime/oesis/assets/<lane>/examples/`
3. Write a hand-coded `validate_<type>()` function matching the schema's required/enum/min/max constraints
4. Cite both URLs in the docstring (MD doc + schema JSON) as done in `compute_trust_score.py`
5. Run `make cross-repo-sync` in `oesis-program-specs` to confirm parity

## Pattern 2 — External/downstream consumers (the bundle)

[`bundles/contracts-bundle/`](bundles/contracts-bundle/) is for consumers who need one versioned drop without tracking the full contracts repo.

### What the bundle provides

- Full schemas + examples + a manifest at a pinned `source_commit`
- Currently mirrors v0.1 fully (26 schemas + 30 examples, including 4 variant examples)
- `manifest.json` declares `bundle_version`, `lane`, and the `source_commit` the snapshot was taken from

### Consumer guidance

- **Validate against bundle schemas using the `jsonschema` library** — external consumers do not need to hand-code validators
- Sample code (Python):

  ```python
  import json
  from jsonschema import Draft202012Validator
  from referencing import Registry, Resource
  from referencing.jsonschema import DRAFT202012
  from pathlib import Path

  bundle = Path("contracts-bundle")
  registry = Registry()
  for schema_path in (bundle / "schemas").glob("*.schema.json"):
      contents = json.loads(schema_path.read_text())
      resource = Resource(contents=contents, specification=DRAFT202012)
      registry = registry.with_resource(uri=schema_path.name, resource=resource)

  node_schema = json.loads((bundle / "schemas/node-observation.schema.json").read_text())
  validator = Draft202012Validator(node_schema, registry=registry)
  validator.validate(my_payload)
  ```

- Pin to a specific `source_commit` from the manifest if you need stability; upgrade when you're ready to accept schema evolution
- When the bundle regenerates, diff and decide whether to pin or upgrade

### Current bundle maintenance

The bundle is currently hand-maintained. See [`#4`](https://github.com/lumenaut-llc/oesis-contracts/issues/4) for the follow-up to write a mechanical generator.

## Pattern 3 — Documentation references (GitHub URLs)

Used by `oesis-program-specs` (architecture + release docs) and `oesis-public-site`.

### Rule: always use absolute GitHub URLs for contract references in docs

```markdown
See [`trust-score-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/trust-score-schema.md)
```

Not relative paths like `../../oesis-contracts/v1.0/trust-score-schema.md` — these break on site builds and in cross-repo browsing.

The `Check internal links` and `Cross-repo consistency` CI jobs in `oesis-program-specs` enforce that these URLs resolve.

## Sync discipline — keeping everything aligned

`oesis-program-specs/scripts/cross_repo_sync_check.py` enforces the following invariants:

| Invariant | What it catches |
|---|---|
| Every `oesis-contracts/<lane>/examples/*.json` has a matching `oesis-runtime/oesis/assets/<lane>/examples/*.json` | Runtime fixture drift |
| No runtime example files exist without a contracts counterpart | Hidden runtime-only examples |
| Every contracts schema has a matching example | Structural schema-example coverage |
| Contract URLs in program-specs resolve against actual files | Stale doc references |

Run `make cross-repo-sync` in `oesis-program-specs` whenever:

- Adding a new schema or example to `oesis-contracts`
- Changing a schema shape in any lane
- Bumping a contract version
- Restructuring directory layout in any sibling repo

This repository's own CI also runs `scripts/validate_examples.py`, which validates every example against its schema across all lanes including the bundle.

## Development loop — adding a new contract

Example: adding a new observation type (`air-quality-index`):

### Step 1 — Design in this repo

```sh
# In oesis-contracts
# Create the prose doc
vim v1.0/air-quality-index-schema.md

# Create the machine-verifiable schema
vim v1.0/schemas/air-quality-index.schema.json

# Create a canonical example
vim v1.0/examples/air-quality-index.example.json

# Validate
python3 scripts/validate_examples.py
# Expect: "All examples validate against their schemas."
```

### Step 2 — Mirror the example to runtime

```sh
# In oesis-runtime
cp ../oesis-contracts/v1.0/examples/air-quality-index.example.json \
   oesis/assets/v1.0/examples/

# In oesis-program-specs
make cross-repo-sync
# Expect: no drift errors
```

### Step 3 — Implement runtime normalizer

Create `oesis-runtime/oesis/ingest/v1_0/normalize_air_quality_index.py` with a hand-coded `validate_air_quality_index()` function. Cite both URLs at the top.

### Step 4 — Add to bundle (only if lane is v0.1)

For v0.1 additions, copy the schema + example to the bundle and update the manifest. v1.0/v1.5 additions stay out of the bundle until bundle policy includes later-lane deltas.

### Step 5 — Reference in docs

Use absolute GitHub URLs when citing the schema from any architecture or release doc in `oesis-program-specs`.

## Common pitfalls

| Pitfall | How it's caught |
|---|---|
| Adding a schema without an example | `schema-example-coverage` CI job |
| Editing example in runtime without updating contracts | `cross_repo_sync_check.py` |
| Hand-coded validator accepts what schema rejects (or vice versa) | Silent drift; example-validation CI eventually |
| Using relative paths in contract doc references | `lychee` broken-link CI job |
| Bypassing the lane model by editing v0.1 schemas directly | Manual review (the lane model is doctrine; see [`v0.1/README.md`](v0.1/README.md)) |
| Forgetting to update bundle when adding v0.1 schemas | Manual for now; [`#4`](https://github.com/lumenaut-llc/oesis-contracts/issues/4) tracks generator |

## The deeper architectural principle

The lane model (frozen baseline + additive lanes) lets you extend contracts without breaking existing consumers:

- A v0.1 consumer keeps working forever
- A v1.0-aware consumer can opt into richer fields
- A v1.5-aware consumer gets bridge-stage support objects

**Never mutate v0.1.** **Never require v1.0+ if the consumer only claimed v0.1 support.**

This is the same principle `oesis-runtime` uses internally with its `v0_1/`, `v1_0/`, `v1_5/` module structure — each lane's module is independently loadable, and no consumer is forced to upgrade.

## Related reading

- [`README.md`](README.md) — repo overview
- [`LANE-INDEX.md`](LANE-INDEX.md) — lane-by-lane navigation
- [`v0.1/README.md`](v0.1/README.md) — baseline lane contract
- [`v1.0/README.md`](v1.0/README.md) — fielded lane additions
- [`v1.5/README.md`](v1.5/README.md) — bridge lane additions
- [`bundles/contracts-bundle/README.md`](bundles/contracts-bundle/README.md) — bundle purpose and structure
- `oesis-program-specs/architecture/current/pre-1.0-version-progression.md` — slice promotion rules
- `oesis-program-specs/architecture/system/version-and-promotion-matrix.md` — how lanes relate to capability stages and deployment maturity
