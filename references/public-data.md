# Public Data

## Contents

1. Retrieval order
2. Primary portals
3. Paper extraction template
4. Public-data reproduction checklist
5. Study-design synthesis

## Retrieval Order

Build literature and public-data context in this order:

1. focused last-decade corpus from `scripts/build_literature_landscape.py`
2. source paper or primary report
3. supplementary methods and figures
4. public accession page
5. processed matrix or object, if available
6. raw-data portal only when needed
7. official package or pipeline documentation for method reproduction
8. `workflows.md` for the current QC, analysis, and figure baseline
9. `tool-issues.md` for current issue trackers, known bugs, and accepted workarounds

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
- CELLxGENE Census, Human Cell Atlas, Single Cell Portal, Tabula Sapiens, TISCH, CancerSEA, HTAN, HuBMAP, and CZ CELLxGENE collections for single-cell and spatial reference data
- ENA, MGnify, Qiita, HMP, GMrepo, and curated SRA projects for microbiome and metagenomics
- PRIDE, MassIVE, ProteomeXchange, Panorama, PeptideAtlas, CPTAC, Metabolomics Workbench, MetaboLights, GNPS, HMDB, LIPID MAPS, and MoTrPAC for proteomics, immunopeptidomics, metabolomics, and flux-related resources
- IEDB, HLA Ligand Atlas, SysteMHC Atlas, VDJdb, McPAS-TCR, ipMSDB, TANTIGEN, TSNAdb, and related primary antigen resources for antigen peptide and TCR-pMHC work
- PDB, AlphaFold DB, UniProt, ChEMBL, PubChem, BindingDB, DrugBank, ZINC, and PDBbind for structural and ligand data
- TCIA, CPTAC imaging collections, Cancer Imaging Archive-linked TCGA cohorts, IDC, and institutional DICOM exports for radiomics and contouring
- public WSI and multiplex imaging resources linked to TCGA, CPTAC, HuBMAP, HTAN, CODEX, MIBI, IMC, or spatial transcriptomics papers

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
- module-specific workflow steps and required diagnostic plots
- package limitations, issue tracker notes, or code workarounds reported by the authors
- validation cohort or orthogonal experiments
- accession numbers
- main figures tied to the core claim
- supplementary figures needed to judge the method
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
- required package-signature and literature-standard method plots are reproduced or recorded as blocked with the exact reason

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
