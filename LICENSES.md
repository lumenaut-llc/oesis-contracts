# Licensing

This repository uses a dual-license model matching the rest of the OESIS program:

| File class | License | Rationale |
|------------|---------|-----------|
| Prose documentation (`*.md`) | CC BY-SA 4.0 | Documentation, governance, and schema prose — shared-alike keeps adapted derivatives in the commons |
| Schema and example JSON (`*.schema.json`, `*.example.json`) | AGPL-3.0-or-later | Machine-verifiable artifacts treated as code for copyleft purposes |

Full text of both licenses:

- CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/legalcode
- AGPL-3.0: see [`LICENSE`](LICENSE) in this repository (same text used by oesis-runtime)

## Matching the program-wide matrix

This split mirrors the one in [oesis-program-specs/LICENSES.md](https://github.com/lumenaut-llc/oesis-program-specs/blob/main/LICENSES.md). The short version:

- software and machine-verifiable artifacts → AGPL-3.0
- documentation and governance prose → CC BY-SA 4.0
- hardware designs → CERN-OHL-S v2 (lives in [oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware))

## Third-party schema references

JSON Schema `$id` URIs in schema files reference `https://lumenaut-llc.github.io/oesis-program-specs/contracts/v*/schemas/*`. These URIs are stable identifiers for schema identity and are not changed by this repository split; they may be served from either oesis-program-specs or oesis-contracts in the future, but their role is identity, not dereference.
