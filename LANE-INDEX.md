# Contracts Lane Index

Use this directory to navigate contract lanes by release posture.

## Lane matrix

| Lane | Purpose | Current status | Where to start |
| --- | --- | --- | --- |
| `v0.1` | Frozen baseline contract surface | Active baseline | `v0.1/README.md` |
| `v0.2` | Promotion marker: widened parcel kit | Inherits `v0.1` (no overrides) | `v0.2/README.md` |
| `v0.3` | Promotion marker: flood-capable runtime | Inherits `v0.1` (no overrides) | `v0.3/README.md` |
| `v0.4` | Promotion marker: multi-node + evidence composition | Inherits `v0.1` (no overrides) | `v0.4/README.md` |
| `v0.5` | Promotion marker: governance enforcement | Inherits `v0.1` (no overrides) | `v0.5/README.md` |
| `v1.0` | Additive lane for broader contract deltas | Active additive lane | `v1.0/README.md` |
| `v1.5` | Additive bridge lane for response/verification objects | Active additive lane | `v1.5/README.md` |

## Baseline lane

- [`v0.1/README.md`](v0.1/README.md) — frozen baseline contract surface
- [`v0.1/schemas/README.md`](v0.1/schemas/README.md) — canonical baseline schemas
- [`v0.1/examples/README.md`](v0.1/examples/README.md) — canonical baseline examples

## Promotion-marker lanes (currently inherit baseline)

- [`v0.2/README.md`](v0.2/README.md)
- [`v0.3/README.md`](v0.3/README.md)
- [`v0.4/README.md`](v0.4/README.md)
- [`v0.5/README.md`](v0.5/README.md)

These lanes are structurally complete (README + `examples/` + `schemas/`) and
currently inherit `v0.1` until explicit lane-specific contract deltas are
accepted.

## Additive lanes

- [`v1.0/README.md`](v1.0/README.md)
- [`v1.5/README.md`](v1.5/README.md)
