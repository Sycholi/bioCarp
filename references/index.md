# Reference Index

Use this file first after `SKILL.md`. It maps task types to the smallest set of reference files needed for an analysis.

## Core Layers

Read these in order:

1. `routing.md` for request intake, data-type routing, and paper-oriented output logic.
2. `r-style.md` for the user's local R style before writing substantial R scripts.
3. `coverage.md` for complete capability scope.
4. `execution.md` for sub-agent use, goal handling, tool deployment, figure inspection, result interpretation, and phase documentation.
5. `learning.md` for user-level assessment, proactive method suggestions, bug learning, and method updates.
6. `methods.md` for concise package choice.
7. `workflows.md` for current module-level QC, modeling, figure, and source requirements.
8. `tools.md` when the task needs method-family comparison or a newer challenger route.
9. `tool-issues.md` before using version-sensitive, web-service, fast-moving, or error-prone tools.

## Task-Specific Layers

### Literature, Public Data, And Study Design

Use:

- `literature.md`
- `public-data.md`
- `data-assessment.md`

Triggers:

- disease-specific or modality-specific study design
- public dataset reproduction
- "what can this dataset do?"
- last-decade method or paper landscape
- public validation cohort selection

### Current Module Execution

Use:

- `workflows.md`
- `execution.md`
- `methods.md`
- `tools.md`

Triggers:

- bulk RNA-seq or microarray
- scRNA-seq
- spatial transcriptomics
- TCR or BCR
- CNV or malignancy inference
- ATAC-seq, scATAC-seq, ChIP-seq, CUT&Tag, CUT&Run, or methylation
- sequence analysis, alignment, variant calling, genome assembly, genome annotation, Hi-C, long-read sequencing, RNA biology, proteomics, metabolomics, flow cytometry, CRISPR screens, or phylogenetics
- survival, prediction modeling, clinical cohorts
- multi-omics integration

### Advanced Single-Cell And Spatial Methods

Use:

- `single-cell-advanced.md`
- `tool-issues.md`
- `workflows.md`

Triggers:

- single-cell QC, ambient RNA, doublets, normalization, integration, clustering, or annotation
- phenotype-associated cell methods such as Scissor, SCIPAC, scPAS, or PACells
- foundation models, virtual cells, virtual knockout, or in silico perturbation
- Geneformer, scGPT, scFoundation, scTenifoldNet, scTenifoldKnk, CellOracle, or related tools
- drug prediction, drug repurposing, DrugReflector, scDrug, scDrug+, scDrugPrio, or drug2cell
- perturbation databases, Perturb-seq, CROP-seq, sci-Plex, ECCITE-seq, Perturb-ATAC, SHARE-seq, Mixscape, or pertpy
- advanced spatial algorithms, niches, adjacency, neighborhood enrichment, BANKSY, CellCharter, Milo, BayesSpace, SpaGCN, GraphST, or PRECAST
- emerging named tools such as scALPI that require name and source verification

### Bulk Functional Inference

Use:

- `bulk-inference.md`
- `workflows.md`
- `tool-issues.md`

Triggers:

- transcription factor activity
- pathway or signaling activity
- kinase, proteomics, or phosphoproteomics activity
- decoupleR, DoRothEA, PROGENy, CollecTRI, OmniPath, VIPER, GSVA, ssGSEA, singscore, or WGCNA
- immune, stromal, or cell-type deconvolution
- CIBERSORTx, immunedeconv, xCell, MCP-counter, EPIC, quanTIseq, TIMER, MuSiC, BisqueRNA, BayesPrism, SCDC, DWLS, or ESTIMATE
- bulk-to-single-cell interpretation

### Metagenomics And Microbiome

Use:

- `metagenomics.md`
- `workflows.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- 16S rRNA, ITS, shotgun metagenomics, metatranscriptomics, virome, or long-read metagenomics
- microbiome diversity, composition, differential abundance, network, or ecological analysis
- Kraken2, Bracken, MetaPhlAn, HUMAnN, QIIME 2, DADA2, mothur, ANCOM-BC2, ALDEx2, MaAsLin2, LEfSe, phyloseq, vegan, or microbiomeMarker
- MAGs, microbial assembly, microbial annotation, GTDB-Tk, CheckM2, dRep, Prokka, Bakta, DRAM, CARD, dbCAN, or eggNOG
- host-microbe, tumor microbiome, therapy-response microbiome, or microbiome multi-omics integration

### Structural Bioinformatics And Drug Screening

Use:

- `structural.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- protein structure prediction, protein complex prediction, antibody-antigen structure, protein-DNA, protein-RNA, protein-ligand, or ligand-binding pocket analysis
- molecular docking, molecular dynamics, free-energy estimation, virtual screening, ADMET, QSAR, ligand preparation, or chemoinformatics
- AlphaFold, ColabFold, AlphaFold 3, Chai-1, Boltz, AutoDock Vina, GNINA, DiffDock, GROMACS, OpenMM, AMBER, RDKit, or DeepChem

### Imaging And Virtual Spatial Omics

Use:

- `imaging.md`
- `workflows.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- pathology imaging, radiomics, pathomics, WSI, H&E, IHC, IF, mIF, MxIF, CODEX, MIBI, IMC, CyCIF, or CyTOF-linked tissue analysis
- automatic segmentation, automatic contouring, radiotherapy structure generation, nnU-Net, MONAI, TotalSegmentator, MedSAM, Cellpose, StarDist, QuPath, Hover-Net, Mesmer, or ilastik
- virtual multiplex immunofluorescence, virtual staining, H&E-to-marker prediction, label-free-to-stain prediction, or sequential IHC virtual multiplexing
- virtual spatial transcriptomics, histology-to-gene-expression prediction, spatial expression imputation, ST-Net, Hist2ST, HisToGene, THItoGene, iStar, BLEEP, STimage, or FineST

### Didactic Or Target-Driven Sensitivity Work

Use:

- `sensitivity.md`
- `data-assessment.md`

Triggers:

- teaching data
- self-test data
- requested target signal is weak or absent
- threshold or grouping choices may be tuned for demonstration

## Tool Issue Layer

Use `tool-issues.md` whenever any of these are true:

- the tool changed object format recently
- the tool depends on web login, model checkpoints, Docker, or a remote service
- the task uses a new, preprint, code-only, or lightly benchmarked method
- the same error appears in GitHub issues, Bioconductor Support, Biostars, CSDN, or package forums
- a workaround changes the data object, assay layer, normalization, or scientific output

Record checked issues and selected workarounds in the project output.

## Execution Layer

Use `execution.md` for every executable analysis.

It controls:

- sub-agent assignment and integration
- goal tracking when explicitly requested or already active
- default tool deployment and installation records
- figure inspection and figure regeneration
- per-figure interpretation
- phase reports and state recovery files

## Learning Layer

Use `learning.md` for every analysis and consultation.

It controls:

- beginner, intermediate, and experienced user assessment
- direct correction of incorrect assumptions
- proactive tool, data type, public dataset, and validation suggestions
- provisional user preference records
- recurring bug and error records
- new tool version, new workflow, and new literature update records

## Output Artifacts

Each real analysis should produce the relevant subset:

- `分析状态.md`
- main analysis script
- key intermediate RDS, CSV, TSV, or AnnData files
- final tables
- complete figure set
- `图表清单.md`
- `图表解读.md`
- `方法学说明.md`
- `工具部署记录.md`
- `参考文献与依据.md`
- `工具问题记录.md` when applicable
- `阶段报告.md` with result analysis, interpretation, methods, references, and limitations
- `限制说明.md` for blocked or exploratory branches

## Learning Artifacts

Maintain these skill-level records:

- `user-profile.md`
- `bug-log.md`
- `method-updates.md`

## Maintenance Rule

When adding a new reference file, update this map and `SKILL.md`.

When adding a new tool family, place method workflow in the most specific reference file and add only a trigger here. Avoid duplicating detailed workflows in multiple files.
