# Public Data And Literature Playbook

## Contents

1. Retrieval order
2. Primary portals
3. Paper extraction template
4. Public-data reproduction checklist
5. Study-design synthesis

## Retrieval Order

Build literature and public-data context in this order:

1. source paper or primary report
2. supplementary methods and figures
3. public accession page
4. processed matrix or object, if available
5. raw-data portal only when needed
6. official package or pipeline documentation for method reproduction

Do not claim to have preloaded the last decade of literature. Build a focused corpus around the actual disease, modality, and endpoint.

## Primary Portals

Use primary or source-adjacent portals first:

- PubMed and PMC for literature discovery and full text when available
- GEO for transcriptomic processed data and series metadata
- SRA for raw sequencing runs
- GDC or TCGA for cancer multi-omics and clinical data
- cBioPortal for rapid cohort-level cancer exploration
- GTEx for normal-tissue expression context
- CPTAC for proteogenomic validation when relevant
- ArrayExpress for archived expression studies
- EGA when controlled-access studies matter
- Human Protein Atlas for expression and pathology support

Secondary discovery portals may help, but always reconcile claims back to the primary source paper or official dataset record.

## Paper Extraction Template

Extract these fields for every key paper:

- disease and biological premise
- sample type and tissue
- species
- cohort size and grouping
- assay platform
- preprocessing pipeline
- QC thresholds
- major statistical models
- key pathway or signature methods
- validation cohort or orthogonal experiments
- accession numbers
- main figures tied to the core claim
- explicit limitations or caveats

Convert the extraction into a compact table or note so the analysis logic can be traced to evidence.

## Public-Data Reproduction Checklist

Before saying a result is reproduced, verify:

- sample counts match or explain why they do not
- group labels match the source
- gene identifiers are mapped correctly
- assay or normalization assumptions are comparable
- exclusion criteria are documented
- statistical method is matched closely enough
- figure-level directionality matches the paper

If the requested target still fails:

- state the unmet target explicitly
- list each plausible source of mismatch
- separate "cannot reproduce yet" from "biologically disproven"

## Study-Design Synthesis

When asked to design a project from literature and available data:

1. define the biological axis or clinical need
2. identify what modality can observe it directly
3. identify what public data can support discovery
4. identify what private or local data can support extension
5. identify what external cohort can support validation
6. turn that path into a figure and table sequence

Typical oncology design chains:

- bulk public discovery -> single-cell mechanistic refinement -> clinical validation
- single-cell discovery -> spatial or CellChat support -> public survival validation
- clinical cohort signal -> public expression support -> mechanistic single-cell follow-up

Use the shortest chain that can support the claim with available data.
