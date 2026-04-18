# Research Data Export Schema (`v1.0`)

## Purpose

Define the framework contract for data that flows from a parcel to a named
research program under the research/pilot sharing mode. Because each research
program defines its own data needs, this contract specifies the envelope and
governance fields that every export must carry, while the inner `data_payload`
structure is program-specific.

## Core fields

- `export_id`
- `research_program_id`
- `program_parcel_id` -- program-scoped pseudonym replacing `parcel_ref`
- `generated_at`
- `consent_verified`
- `retention_expires_at`
- `publication_allowed`
- `anonymization_level`
- `payload_schema_version`
- `data_payload`

### `anonymization_level`

Enum describing the anonymization applied before export:

- `parcel_ref_only` -- parcel_ref replaced with program-scoped pseudonym;
  internal identifiers stripped; temporal and spatial detail retained
- `structural_anonymization` -- pseudonym plus coarsened timestamps and spatial
  identifiers to reduce re-identification risk
- `full_anonymization` -- no linkability to a specific parcel; statistical
  use only

### `data_payload`

A program-specific object. Every `data_payload` must include:

- `extracted_fields` -- array of field names included in the export
- `extraction_window` -- object with `from` and `to` timestamps bounding the
  source data
- `source_contract_version` -- the contract version of the source data used
  for extraction

Additional keys are defined by the research program protocol and validated
against the program's own payload schema (identified by
`payload_schema_version`).

### Optional fields

- `audit_trail` -- object containing:
  - `program_operator` -- identifier of the research program operator
  - `access_logged` -- boolean indicating whether access was logged
  - `export_timestamp` -- timestamp of the export event

## Minimum object

```json
{
  "export_id": "rde_pilot_smoke_2026q2_parcel_ref_001",
  "research_program_id": "pilot_smoke_response_2026q2",
  "program_parcel_id": "ps2026q2_anon_0047",
  "generated_at": "2026-04-13T06:00:00Z",
  "consent_verified": true,
  "retention_expires_at": "2026-10-13T06:00:00Z",
  "publication_allowed": false,
  "anonymization_level": "parcel_ref_only",
  "payload_schema_version": "pilot_smoke_response_2026q2.v1",
  "data_payload": {
    "extracted_fields": ["outdoor_pm25_hourly", "smoke_band", "evidence_mode"],
    "extraction_window": {
      "from": "2026-04-01T00:00:00Z",
      "to": "2026-04-12T23:59:59Z"
    },
    "source_contract_version": "v0.1"
  }
}
```

## Design rules

- Every export must carry `consent_verified: true`. If consent is not active at
  extraction time, the export must not be generated.
- `program_parcel_id` is a pseudonym scoped to the research program. It must not
  be derivable from `parcel_ref`, `parcel_id`, or any public identifier. The
  mapping from parcel identity to pseudonym is held only by the platform operator
  and must not be shared with the research program.
- `retention_expires_at` is set by the research program protocol at export time.
  The research program operator must delete or return the export by this date.
- `publication_allowed` defaults to `false`. Publication of findings derived
  from exported data requires a separate approval step outside this contract.
  This field records whether that approval has been granted at export time.
- Access to exported data is via an export bundle, not a live API query. The
  research program does not receive streaming or real-time access to parcel data.
- Each research program defines its own `data_payload` schema, referenced by
  `payload_schema_version`. The platform validates the envelope fields; the
  program operator is responsible for payload schema compliance.
- The `anonymization_level` must match or exceed the level required by the
  research program protocol. The platform must not export at a weaker
  anonymization level than the program specifies.
- Exported data must not be repurposed beyond the documented program purpose.
  Redistribution, secondary analysis, or use in unrelated products requires a
  new consent and a new export.

## Related docs

- `governance-operational-model.md`
- `consent-store-schema.md`
- `sharing-settings-schema.md`
- `../../legal/privacy/permissions-matrix.md`
- `../../operations/pilots/pilot-consent-checklist.md`
