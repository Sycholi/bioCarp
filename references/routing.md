# Routing

## Contents

1. Intake checklist
2. Data-to-analysis matrix
3. Reference routing baseline
4. Single-cell route
5. Bulk and microarray route
6. Spatial route
7. Clinical and survival route
8. Multi-omics integration route
9. Variant and antigen route
10. Proteomics, metabolomics, and flux route
11. Metagenomics route
12. Structural bioinformatics route
13. Imaging route
14. "What can this dataset do?" route
15. Paper-oriented output chain

## Intake Checklist

Reconstruct these items before coding:

- disease, tissue, and species
- assay type and platform
- sample unit: patient, sample, cell, spot, region, image, slide, molecule, ligand, protein, contig, MAG, or microbial feature
- available metadata: response, stage, grade, survival, treatment, batch, tissue, clone, collection site, scanner, sequencing run, structure source, compound library, HLA, raw MS batch, isotope tracer, or peptide evidence
- requested endpoint or biological axis
- custom data, public data, or mixed validation
- intended output: figure, table, reusable script, full draft result, or study design

If any of these are missing and materially affect analysis logic, infer from files first. Ask the user only when the ambiguity is truly blocking.

## Reference Routing Baseline

After choosing a route from this file, use `index.md` to select the companion references for the data type, method family, and risk level. Every executable route must read `workflows.md` unless the task is purely conversational.

Use the selected companion files to decide:

- QC and preprocessing steps that cannot be skipped
- package and model selection
- required diagnostic and signature figures
- recent literature figure types that should be reproduced for the module
- conditions where the analysis should be marked blocked or exploratory

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

### Variants, HLA, Antigen Peptides, Or Immunopeptidomics

Feasible branches:

- germline or somatic variant calling and annotation
- CNV, SV, MSI, TMB, mutational signatures, clonality, and cancer driver summaries
- HLA typing and HLA loss review
- neoantigen and antigen peptide candidate ranking
- immunopeptidomics QC, MHC motif analysis, peptide-source annotation, and peptide evidence review
- TCR-pMHC candidate follow-up when TCR or epitope databases exist

Shortest route:

1. define sample type, HLA source, variant source, and evidence layers
2. run or verify variant and HLA calls
3. add expression, clonality, copy-number, and normal-tissue filters
4. run antigen peptide prediction or immunopeptidomics interpretation
5. rank candidates with explicit evidence and limitations

### Proteomics, Metabolomics, Lipidomics, Or Metabolic Flux

Feasible branches:

- raw MS QC, peptide or metabolite identification, quantification, normalization, and differential analysis
- protein, peptide, PTM-site, kinase, and pathway inference
- metabolite, lipid class, pathway, and compound annotation analysis
- isotope tracing, mass isotopomer distribution, and 13C metabolic flux modeling
- genome-scale metabolic modeling, FBA, and single-cell metabolism inference
- multi-omics integration with RNA, variants, microbiome, imaging, or clinical data

Shortest route:

1. verify raw data, acquisition type, batch, QC samples, and annotation evidence
2. run assay-specific processing or verify supplied matrices
3. perform normalization, missingness review, and sample-level QC
4. run differential, pathway, PTM, lipid, flux, or modeling module
5. connect results to expression, phenotype, or validation evidence

### Metagenomics Or Microbiome

Feasible branches:

- amplicon ASV analysis
- shotgun taxonomic profiling
- functional profiling
- differential abundance
- microbiome diversity and ordination
- MAG reconstruction and annotation
- host-microbe integration

Shortest route:

1. define assay type, sample source, controls, and metadata
2. run read QC and contamination review
3. generate taxonomic or functional profiles
4. run diversity and association analysis
5. connect microbial features to phenotype, host omics, or literature

### Structural Bioinformatics Or Virtual Screening

Feasible branches:

- structure retrieval or prediction
- pocket and interface analysis
- molecular docking
- virtual screening
- ADMET and chemoinformatics filtering
- molecular dynamics and free-energy analysis

Shortest route:

1. define target, ligand, structure source, and endpoint
2. validate structure and binding-site evidence
3. run docking or structure prediction route
4. validate poses or confidence metrics
5. add MD or free-energy analysis only when the claim needs dynamics

### Imaging, Radiomics, Or Virtual Spatial Omics

Feasible branches:

- radiomics feature extraction
- WSI or pathology image classification
- automatic segmentation or contouring
- multiplex imaging and spatial phenotype analysis
- virtual immunofluorescence or virtual staining
- virtual spatial transcriptomics

Shortest route:

1. verify image format, resolution, modality, annotation, and patient split
2. run image QC and segmentation or registration checks
3. extract measured or predicted features
4. evaluate model or biological association at patient or slide level
5. validate against measured markers, annotations, or external cohorts

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

## Metagenomics Route

Use this route when the key signal is microbial composition, microbial function, strain or MAG biology, or host-microbe association. Read `metagenomics.md` before implementation.

## Structural Bioinformatics Route

Use this route when the task depends on molecular structure, ligand binding, virtual screening, docking, molecular dynamics, or ADMET. Read `structural.md` before implementation.

## Imaging Route

Use this route when the task depends on radiomics, pathomics, WSI analysis, automatic segmentation, multiplex imaging, virtual staining, virtual immunofluorescence, or virtual spatial omics. Read `imaging.md` before implementation.

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
This limit does not permit dropping required diagnostic plots, package-signature visualizations, or literature-standard method plots. For every selected method, still generate the full figure set needed to judge that method, then choose the subset used in the final story.
