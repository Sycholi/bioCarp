# Tool Landscape

## Contents

1. How to use this file
2. Core selection rule
3. Bulk and cohort tools
4. Single-cell tools
5. Spatial and deconvolution tools
6. Immune-repertoire tools
7. Multi-omics tools
8. Selection checklist

## How To Use This File

Use this file when the request asks for:

- a package comparison
- dominant tool families over the last decade or two decades
- strengths and weaknesses of competing methods
- which route should be chosen for a dataset

This file is a family map, not a package encyclopedia. Use it to narrow to a route, then read official package documentation before implementation.

## Core Selection Rule

Choose the route that satisfies all four conditions:

1. it answers the biological question directly
2. it fits the actual data structure
3. it stays close to the user's `~/r_repo` execution style when scientific fit is comparable
4. it avoids unnecessary environment complexity

Do not switch to a newer package only because it is newer. Switch only when the biological fit, statistical fit, or scale requirement is materially better.

## Bulk And Cohort Tools

### Differential expression

- `limma` / `limma-voom`
  - Best for: microarray, normalized expression, complex designs, transformed RNA-seq
  - Strengths: mature, flexible design matrices, very strong publication history
  - Weaknesses: raw-count workflows usually fit better in count-based models
- `edgeR`
  - Best for: count matrices with modest sample sizes or strong library-size differences
  - Strengths: reliable dispersion modeling, transparent count-based assumptions
  - Weaknesses: less preferred when users strongly expect DESeq2-style output objects
- `DESeq2`
  - Best for: publication-standard count workflows with clean group definitions
  - Strengths: widely recognized, shrinkage options, straightforward reporting
  - Weaknesses: slower on very large matrices, not automatically the best choice for every complex design

### Survival and clinical modeling

- `survival` + `survminer`
  - Best for: Kaplan-Meier, Cox, clean clinical reporting
  - Strengths: canonical and interpretable
  - Weaknesses: feature selection and high-dimensional modeling need extra tools
- `rms`
  - Best for: nomograms, calibration, richer regression diagnostics
  - Strengths: strong clinical-modeling toolkit
  - Weaknesses: heavier modeling overhead than simple KM/Cox workflows
- `glmnet`
  - Best for: penalized signatures and high-dimensional feature reduction
  - Strengths: robust regularization
  - Weaknesses: signatures can become unstable without disciplined resampling and validation
- `timeROC`, `survivalROC`
  - Best for: time-dependent ROC reporting
  - Weaknesses: should support, not replace, core survival reasoning
- `MatchIt`
  - Best for: confounding reduction in observational cohorts
  - Weaknesses: matching cannot rescue missing biology or poor endpoint definition

### Bulk deconvolution and microenvironment

- `CIBERSORTx`
  - Best for: reference-based cellular composition estimates from bulk data
  - Strengths: widely cited and familiar to biomedical readers
  - Weaknesses: depends heavily on reference quality and signature transferability
- `EPIC`, `MCP-counter`, `xCell`, `quanTIseq`
  - Best for: quick immune or stromal context
  - Strengths: fast, useful for cohort-wide trends
  - Weaknesses: cell-resolution claims should stay modest
- `MuSiC`, `BisqueRNA`
  - Best for: single-cell-informed deconvolution
  - Strengths: better when matching single-cell reference exists
  - Weaknesses: strong dependence on reference compatibility

## Single-Cell Tools

### Object handling and integration

- `Seurat`
  - Best for: end-to-end R workflows, broad plotting, metadata-centric analysis
  - Strengths: dominant in the user's local library, easy handoff to downstream modules
  - Weaknesses: some advanced scaling or probabilistic integration tasks are better elsewhere
- `Harmony`
  - Best for: metadata-aware batch correction inside Seurat workflows
  - Strengths: practical, familiar, low-friction in R
  - Weaknesses: not a universal answer for every cross-cohort integration problem
- `RPCA` / Seurat anchors
  - Best for: moderate integration tasks where Seurat-native mapping is enough
  - Weaknesses: can over- or under-correct depending on cohort structure
- `LIGER`
  - Best for: factor-based integration across modalities or batches
  - Weaknesses: less aligned to the user's current dominant code style
- `scVI` / `scANVI`
  - Best for: difficult batch structure, large heterogeneous cohorts, probabilistic latent modeling
  - Strengths: strong integration performance
  - Weaknesses: heavier Python dependence and extra environment complexity

### Annotation

- Manual marker annotation
  - Best for: oncology projects needing interpretable subtypes and custom state naming
  - Strengths: strongest alignment with the user's style and manuscript defense
  - Weaknesses: slower and dependent on domain knowledge
- `SingleR`
  - Best for: first-pass reference transfer in R
  - Strengths: lightweight and easy to add
  - Weaknesses: final labels still need marker verification
- `CellTypist`
  - Best for: large immune-rich datasets needing rapid draft labels
  - Strengths: fast and practical
  - Weaknesses: draft labels can drift from disease-specific states
- `Azimuth`
  - Best for: reference mapping onto strong Seurat references
  - Weaknesses: less suitable when tumor-specific states dominate

### Differential state and marker analysis

- `FindMarkers` / `FindAllMarkers`
  - Best for: pragmatic cluster marker discovery inside Seurat
  - Strengths: direct and familiar
  - Weaknesses: pseudo-replication risk if biological replicate structure matters
- pseudo-bulk with `edgeR`, `DESeq2`, or `limma`
  - Best for: sample-aware differential testing across patient groups
  - Strengths: statistically cleaner for patient-level inference
  - Weaknesses: requires careful aggregation and replicate definition
- `muscat`
  - Best for: multi-sample differential state testing
  - Strengths: explicit design for replicate-aware single-cell comparisons
  - Weaknesses: higher setup cost than quick Seurat marker calls

### Trajectory and state transitions

- `Monocle2`
  - Historical role: classic pseudotime in older papers
  - Weaknesses: older design and fewer advantages for new projects
- `Monocle3`
  - Best for: trajectory graphing with modern workflows
  - Strengths: familiar in many single-cell papers
  - Weaknesses: lineage statistics may still need companion tools
- `slingshot` + `tradeSeq`
  - Best for: lineage-aware pseudotime with formal expression testing
  - Strengths: strong for state-transition questions and gene-trend statistics
  - Weaknesses: setup is less plug-and-play than one-click pseudotime plotting
- `PAGA`
  - Best for: topology-first trajectory reasoning in Scanpy ecosystems
  - Weaknesses: less natural in an R-first project
- `scVelo`
  - Best for: velocity-specific questions with spliced and unspliced data
  - Weaknesses: not appropriate unless velocity assumptions and inputs are satisfied
- `CytoTRACE` / `CytoTRACE2`
  - Best for: differentiation potential rather than explicit branch structure

### Cell-cell communication

- `CellChat`
  - Best for: pathway-level network visualization in R
  - Strengths: already present in the user's style
  - Weaknesses: communication plots should not be overinterpreted as direct mechanistic proof
- `CellPhoneDB`
  - Best for: canonical ligand-receptor interaction testing
  - Strengths: widely known
  - Weaknesses: Python workflow and less aligned with the local R-first style
- `NicheNet`
  - Best for: ligand-to-target prioritization
  - Strengths: stronger when downstream target programs matter
  - Weaknesses: requires more careful biological framing
- `LIANA`
  - Best for: consensus-style ligand-receptor scoring across methods
  - Strengths: broader method harmonization
  - Weaknesses: higher complexity than many projects need

### CNV and malignancy inference

- `infercnv`
  - Best for: transcriptome-based CNV estimation with reasonable normal references
  - Strengths: highly familiar in cancer single-cell papers
  - Weaknesses: sensitive to reference choice and parameter settings
- `CopyKAT`
  - Best for: tumor-versus-normal separation with inferable aneuploidy
  - Strengths: practical for malignancy calling
  - Weaknesses: not all tumors or datasets fit its assumptions equally well
- `HoneyBADGER`, `CONICSmat`
  - Best for: niche scenarios needing alternative CNV logic
  - Weaknesses: less standard for a shortest-path workflow

## Spatial And Deconvolution Tools

### Spatial preprocessing and exploration

- `Seurat` / `STutility`
  - Best for: R-first spatial handling close to existing Seurat workflows
- `Giotto`
  - Best for: richer spatial network and visualization workflows
  - Weaknesses: larger conceptual overhead
- `squidpy`
  - Best for: Scanpy/Python spatial ecosystems
  - Weaknesses: added Python complexity in an R-first environment

### Spatial statistics and deconvolution

- `SPARK-X`
  - Best for: spatially variable gene testing
- `BayesSpace`
  - Best for: spot-level clustering refinement
- `RCTD`, `cell2location`, `CARD`
  - Best for: cell-type deconvolution into spots
  - Strengths: useful when paired single-cell references exist
  - Weaknesses: conclusions are only as good as reference quality and platform compatibility

## Immune-Repertoire Tools

- `scRepertoire`
  - Best for: Seurat-linked clonotype integration in R
  - Strengths: direct metadata integration
- `Startrac`
  - Best for: expansion, transition, and distribution logic in immune-state studies
  - Strengths: strong when tissue ecology matters
- `immunarch`
  - Best for: bulk or repertoire-centric summaries
- `scirpy`
  - Best for: Python/Scanpy ecosystems

## Multi-Omics Tools

- `Signac`
  - Best for: scATAC or multimodal workflows inside Seurat
  - Strengths: minimal friction for Seurat users
- `ArchR`
  - Best for: large-scale scATAC projects with richer ATAC tooling
  - Weaknesses: larger framework shift
- `MOFA2`
  - Best for: latent-factor integration across multiple omics
- `mixOmics`
  - Best for: supervised or integrative feature relationships
- `iClusterPlus`
  - Best for: classical cancer multi-omics subtype integration
- Seurat `WNN`
  - Best for: multimodal single-cell integration when Seurat is already the backbone

## Selection Checklist

Before locking the route, answer all of these:

1. What is the actual unit of inference: cell, sample, patient, spot, clonotype, or cohort?
2. Does the default tool family respect that unit of inference?
3. Is a replicate-aware design required?
4. Does the tool fit the available metadata and validation path?
5. Does it materially improve the scientific fit over the user's existing route?
6. Is the environment cost justified?

If the answer to 5 or 6 is weak, stay with the route that is already coherent in `~/r_repo`.
