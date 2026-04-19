# Workflow Playbook

## Contents

1. Intake checklist
2. Data-to-analysis matrix
3. Single-cell route
4. Bulk and microarray route
5. Spatial route
6. Clinical and survival route
7. Multi-omics integration route
8. "What can this dataset do?" route
9. Paper-oriented output chain

## Intake Checklist

Reconstruct these items before coding:

- disease, tissue, and species
- assay type and platform
- sample unit: patient, sample, cell, spot, region, image, or slide
- available metadata: response, stage, grade, survival, treatment, batch, tissue, clone
- requested endpoint or biological axis
- custom data, public data, or mixed validation
- intended output: figure, table, reusable script, full draft result, or study design

If any of these are missing and materially affect analysis logic, infer from files first. Ask the user only when the ambiguity is truly blocking.

## Data-to-Analysis Matrix

### Bulk RNA-seq or Microarray

Feasible branches:

- QC and sample filtering
- gene identifier harmonization
- differential expression
- pathway enrichment or GSEA
- immune deconvolution
- phenotype or signature scoring
- survival modeling
- public-cohort validation

Typical shortest route:

1. align sample metadata and matrix
2. harmonize gene identifiers
3. define contrast
4. run DE model
5. run enrichment
6. build one or more validation plots
7. connect to survival or clinical phenotype if available

### Single-Cell RNA-seq

Feasible branches:

- per-sample QC
- batch integration
- cluster annotation
- lineage-specific subclustering
- differential expression by cluster, group, tissue, or response
- pathway activity and signature scoring
- trajectory or pseudotime
- cell-cell communication
- clonotype or repertoire integration
- CNV or malignant-cell inference
- public-dataset comparison

Typical shortest route:

1. load and QC each object
2. standardize metadata
3. merge or integrate
4. annotate major cell types
5. choose one lineage that answers the biological question
6. subcluster and compare groups inside that lineage
7. run pathway, communication, clonality, or trajectory modules as needed
8. validate with public data or orthogonal evidence

### Spatial Transcriptomics

Feasible branches:

- QC by spot or region
- region annotation
- tumor-stroma-immune niche mapping
- spatial feature plotting
- deconvolution or label transfer
- neighborhood analysis
- pathway or signature heatmaps
- spatial validation of single-cell findings

Shortest route:

1. build a clean spatial object
2. define regions or niches
3. quantify the requested signal spatially
4. connect spatial findings back to cell types, pathways, or outcome

### Clinical Cohort or Survival Table

Feasible branches:

- cohort summary tables
- Kaplan-Meier analysis
- univariate and multivariate Cox models
- subgroup analysis
- matching or balancing when design requires it
- biomarker cut-point comparison
- nomogram or risk score if explicitly requested

Shortest route:

1. clean clinical variables
2. define endpoint and censoring
3. generate baseline table
4. run KM and Cox analyses
5. add subgroup or matched analysis only if it answers the stated question

### Multi-Omics or Mixed Public/Private Validation

Feasible branches:

- cross-modality concordance
- molecular subtype definition
- signature projection
- mutation-expression or CNV-expression linkage
- validation across public cohorts
- mechanistic integration for figure narrative

Shortest route:

1. choose one anchor modality
2. derive the core phenotype or axis
3. project or validate that axis in the other modalities
4. keep the figure narrative causal and compact

## Single-Cell Route

Follow this order unless the request clearly narrows scope:

1. QC and remove obvious artifacts
2. integrate or batch-correct only as much as needed
3. annotate major cell classes
4. isolate the lineage relevant to the question
5. rerun a local analysis in that lineage
6. derive markers and pathway signals
7. add trajectory, communication, clonality, or CNV only when they sharpen the answer
8. validate against literature or public cohorts

Key downstream modules common in the user's library:

- marker-driven annotation
- CellChat
- Startrac or scRepertoire
- Monocle3, slingshot, tradeSeq, or CytoTRACE
- infercnv or related CNV tools
- clusterProfiler or fgsea

## Bulk and Microarray Route

Follow this order:

1. inspect metadata completeness
2. remove low-information genes
3. choose the DE framework that fits the matrix and design
4. rank genes and pathways
5. connect results to phenotype, immune infiltration, or survival
6. validate in at least one independent cohort when the request is publication-oriented

Use this route when researchers say:

- "I only have an expression matrix and clinical table"
- "Can this gene stratify prognosis?"
- "What pathways differ between responders and non-responders?"

## Spatial Route

Use spatial analysis mainly as:

- localization support for single-cell findings
- tumor-margin or niche analysis
- cell-interaction validation
- pathway activity mapping in tissue context

Do not expand a spatial project into a full multimodal platform paper unless the available data can actually support it.

## Clinical and Survival Route

Use this route when the key claim is clinical impact rather than cell biology.

Focus on:

- endpoint definitions
- covariate balance
- multivariable interpretability
- figure clarity

Only add matching, subgrouping, or cut-point optimization when the question truly depends on them.

## Multi-Omics Integration Route

Use this route when one omics layer alone cannot support the biological claim.

Prefer this sequence:

1. establish the signal in the strongest modality
2. map the signal into orthogonal modalities
3. show convergence rather than collecting disconnected panels

## "What Can This Dataset Do?" Route

When the requester does not know what bioinformatics can contribute:

1. identify data modality and metadata richness
2. list all technically feasible analyses
3. separate high-value analyses from low-yield ones
4. identify missing metadata that blocks stronger questions
5. propose the shortest study design that can produce a coherent paper story

Typical output should include:

- feasible analyses now
- feasible analyses after adding one or two missing metadata items
- likely publication angles
- validation options from public data

## Paper-Oriented Output Chain

Keep the logic compact and traceable:

1. cohort and data overview
2. global structure or phenotype split
3. one core differential or lineage finding
4. pathway or mechanism support
5. clinical or external validation
6. optional communication, clonality, or spatial reinforcement

Avoid building a figure set that is broader than the actual evidence.
