# Clinical Data

Use this file for clinical data ingestion, EHR, registry, REDCap, OMOP, FHIR, CDISC, SDTM, ADaM, adverse event tables, laboratory data, medication exposure, outcomes, data quality review, and clinical data harmonization.

## Intake

Before implementation, verify:

- data source: case report form, REDCap, EDC, EHR, registry, claims, imaging archive, laboratory system, wearable device, public cohort, trial database, OMOP, CDISC, FHIR, or linked omics-clinical table
- patient identifier, encounter identifier, sample identifier, visit date, diagnosis date, treatment dates, response dates, event dates, death date, censoring date, and data cut date
- coding systems: ICD, SNOMED CT, LOINC, RxNorm, ATC, CPT, MedDRA, CTCAE, CDISC controlled terminology, HGNC, Ensembl, or ontology mappings
- privacy requirements, consent, de-identification, date shifting, site labels, and controlled access

## Data Standard Selection

Current route:

1. Use project-native tables for small internal exploratory projects after checking identifiers and dates.
2. Use REDCap exports or API when study data are collected through REDCap.
3. Use OMOP CDM when working with standardized EHR, registry, claims, or multi-site real-world data.
4. Use FHIR when exchanging structured EHR data or integrating clinical systems.
5. Use CDISC SDTM and ADaM when preparing or interpreting regulatory-style clinical trial datasets.
6. Preserve a data dictionary, mapping table, unit conversion table, and date derivation table.

Primary standards and tools:

- REDCap, REDCapR, redcapAPI
- OMOP CDM, OHDSI ATLAS, WhiteRabbit, Rabbit-in-a-Hat, Achilles, DataQualityDashboard, CohortDiagnostics, FeatureExtraction
- FHIR, HL7, SMART on FHIR, fhircrackr, fhiry
- CDISC SDTM, ADaM, CDASH, Define-XML, ODM, admiral, metacore, xportr, haven
- MedDRA, CTCAE, WHO Drug, ICD, SNOMED CT, LOINC, RxNorm, ATC

## Data Quality Review

Current route:

1. Check row counts, patient counts, visit counts, duplicate keys, impossible dates, out-of-order dates, missing identifiers, unit conflicts, and range errors.
2. Derive analysis dates and endpoint dates from raw fields with transparent rules.
3. Check treatment exposure, dose, line of therapy, regimen changes, discontinuation, and rescue therapy.
4. Check adverse events by MedDRA or CTCAE term, grade, seriousness, relatedness, action taken, and outcome.
5. Check laboratory units, normal ranges, baseline values, worst post-baseline values, and shift tables.
6. Check response definitions such as RECIST, iRECIST, RANO, pathologic response, MRD, or disease-specific endpoints.

Required outputs:

- data dictionary and mapping table
- patient, sample, visit, exposure, endpoint, and censoring derivation tables
- missingness, range, duplicate, and date-ordering reports
- baseline table and exposure summary
- adverse event, serious adverse event, lab shift, and medication summary
- endpoint derivation audit table

Required figures:

- cohort flow
- missingness heatmap
- visit timeline and data cut plot
- treatment exposure and line-of-therapy plot
- adverse event overview and grade plot
- laboratory shift and spaghetti plots when longitudinal labs matter
- endpoint and censoring timeline

## Source Index

Last checked: 2026-05-28.

- REDCap: https://projectredcap.org/
- REDCap CDIS and FHIR: https://projectredcap.org/software/cdis/
- OMOP Common Data Model: https://ohdsi.github.io/CommonDataModel/
- OHDSI ATLAS: https://github.com/OHDSI/Atlas
- OHDSI DataQualityDashboard: https://github.com/OHDSI/DataQualityDashboard
- CDISC Foundational Standards: https://www.cdisc.org/standards/foundational
- CDISC SDTM: https://www.cdisc.org/standards/foundational/sdtm
- CDISC ADaM: https://www.cdisc.org/standards/foundational/adam
- CDISC Real World Data: https://www.cdisc.org/standards/real-world-data
- FHIR: https://hl7.org/fhir/
- admiral: https://pharmaverse.github.io/admiral/
