# Data To Project Map

## Contents

1. Purpose
2. Consultation output
3. Data-type map
4. Metadata gates
5. Publication-path heuristics

## Purpose

Use this file when the researcher does not know what the data can support.

Translate the actual dataset into:

- feasible analyses
- high-yield publication routes
- impossible or weak routes
- extra metadata or validation needed for blocked routes

## Consultation Output

Return the consultation in four blocks:

1. what this dataset can answer directly
2. what it can answer after adding public validation
3. what it cannot answer yet
4. the shortest publishable figure chain

## Data-Type Map

### Bulk RNA-seq or microarray

If group labels exist:

- differential expression
- enrichment and pathway ranking
- immune and stromal deconvolution
- survival or clinical association if endpoints exist
- public-cohort validation

If paired tumor-normal exists:

- within-patient contrasts
- tumor-versus-normal signatures
- matched pathway and immune changes

If no phenotype labels exist:

- unsupervised subtype discovery
- score-based stratification from literature signatures
- association with available clinical covariates

Usually weak without more metadata:

- causal claims
- cell-state claims without deconvolution or single-cell support

### Single-cell RNA-seq

Directly feasible:

- QC and batch inspection
- clustering and annotation
- marker programs
- differential cell states
- pathway scoring
- trajectory or differentiation logic
- communication analysis
- malignancy inference if tumor data are present

If paired clinical or response labels exist:

- responder-versus-nonresponder state shifts
- cell-fraction changes
- state-specific differential programs
- clonality or repertoire coupling when TCR or BCR is paired

If paired tumor-normal or lesion types exist:

- compartment shifts
- tumor-enriched state discovery
- lineage-state transitions across conditions

Usually blocked without extra metadata:

- patient-level inferential claims when replicate labels are missing
- survival validation without external cohort

### Spatial transcriptomics

Directly feasible:

- spatial domain discovery
- neighborhood structure
- spatially variable genes
- spatial support for single-cell-defined states

High-value routes:

- single-cell state mapping into spatial context
- tumor-stroma or immune niche reconstruction

Usually blocked without paired reference:

- confident spot deconvolution
- fine cell-state attribution

### TCR or BCR repertoire

Directly feasible:

- clonotype abundance
- diversity metrics
- expansion and sharing
- phenotype-clonotype coupling when paired with scRNA-seq

High-value routes:

- exhausted or activated clone-state mapping
- tissue-distribution or transition analysis

Usually blocked without pairing:

- state-specific clonotype biology

### ATAC-seq or chromatin layers

Directly feasible:

- peak accessibility
- motif enrichment
- gene-activity trends
- lineage-regulatory changes

High-value routes:

- multimodal coupling with scRNA-seq
- regulator prioritization for a discovered cell state

Usually blocked without matching expression or phenotype labels:

- interpretable downstream biology

### Clinical cohort only

Directly feasible:

- descriptive statistics
- survival modeling
- clinical subgroup analysis
- nomogram or risk model construction

High-value routes:

- literature-signature validation
- public expression linkage

Usually blocked without molecular data:

- mechanistic claims

## Metadata Gates

Before promising an analysis branch, verify:

1. sample or patient IDs exist
2. grouping or endpoint labels are defined
3. batch or platform metadata are known
4. paired or longitudinal structure is explicit
5. validation material exists
6. covariates needed for confounding control exist

If a gate is missing, mark the branch as blocked or exploratory-only.

## Publication-Path Heuristics

Shortest common paths:

- bulk discovery -> public validation -> concise mechanism discussion
- single-cell state discovery -> pathway plus trajectory -> public cohort validation
- single-cell discovery -> spatial support -> external cohort validation
- clinical cohort signal -> public expression support -> targeted single-cell follow-up

Choose the shortest route that can support the target claim with the existing data. Do not create a larger pipeline than the data can defend.
