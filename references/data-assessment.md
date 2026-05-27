# Data Assessment

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

For every data type below, check `workflows.md` before promising the analysis. A branch is feasible only when the data support the current QC, modeling, and figure requirements for that branch.

### Bulk RNA-seq or microarray

If group labels exist:

- differential expression
- enrichment and pathway ranking
- transcription factor, pathway, kinase, or regulator activity inference when suitable prior networks exist
- immune and stromal deconvolution
- cell-type or cell-state projection from single-cell references when reference compatibility is defensible
- co-expression modules or WGCNA when sample size and phenotype structure support network analysis
- survival or clinical association if endpoints exist
- public-cohort validation

If paired tumor-normal exists:

- within-patient contrasts
- tumor-versus-normal signatures
- matched pathway and immune changes

If no phenotype labels exist:

- unsupervised subtype discovery
- score-based stratification from literature signatures
- pathway, TF, or deconvolution-based exploratory stratification
- association with available clinical covariates

Usually weak without more metadata:

- causal claims
- cell-state claims without deconvolution or single-cell support
- direct TF, kinase, or cell-fraction claims without orthogonal validation

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
- QC and reproducibility review from fragment size, TSS enrichment, FRiP, peak count, replicate concordance, and genome-browser tracks when raw or aligned data exist

High-value routes:

- multimodal coupling with scRNA-seq
- regulator prioritization for a discovered cell state
- peak-to-gene linkage, footprinting, co-accessibility, and motif activity when data quality and package support are sufficient

Usually blocked without matching expression or phenotype labels:

- interpretable downstream biology

### ChIP-seq, CUT&Tag, or CUT&Run

Directly feasible:

- peak calling review or reuse of supplied peaks
- peak annotation and target-gene assignment
- motif enrichment and regulatory-region enrichment
- signal heatmaps, metaplots, and genome-browser tracks
- differential binding when replicate structure and design support it

High-value routes:

- TF or histone-mark support for a transcriptional state
- binding-to-expression integration with RNA-seq or scRNA-seq
- treatment or phenotype-linked differential binding

Usually blocked without raw or aligned reads and controls:

- full QC, replicate concordance, and confident differential binding

### DNA methylation

Directly feasible:

- array or sequencing QC when raw files exist
- DMP and DMR analysis
- methylation subtype or signature scoring
- gene or region annotation and enrichment

High-value routes:

- methylation-expression coupling
- public cohort validation
- clinical association when endpoints exist

Usually blocked without platform annotation or raw intensity or coverage data:

- defensible normalization, probe filtering, and sample-level QC

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

### Variants, HLA, and antigen peptides

Directly feasible:

- germline or somatic variant summary when VCF, MAF, or raw WGS, WES, panel, or RNA-seq data exist
- CNV, SV, TMB, MSI, and mutational signature analysis when data type and depth support them
- HLA typing when WES, WGS, RNA-seq, targeted HLA, or clinical HLA calls exist
- antigen peptide or neoantigen prioritization when variants, HLA, expression, and annotation are available
- immunopeptidomics interpretation when raw or processed LC-MS/MS peptide evidence exists

High-value routes:

- somatic variant -> HLA typing -> peptide binding prediction -> RNA or protein expression -> clonality and copy-number review
- immunopeptidomics peptide evidence -> HLA motif validation -> source protein expression -> tumor specificity
- variant, antigen, TCR, and clinical response integration when all layers are matched

Usually blocked without key inputs:

- neoantigen ranking without reliable HLA calls
- antigen claims without expression or peptide evidence
- TCR recognition claims without TCR data, known epitope database match, or functional validation

### Proteomics, phosphoproteomics, and immunopeptidomics

Directly feasible:

- raw MS QC, identification, quantification, normalization, missingness review, and differential protein abundance
- TMT, LFQ, DIA, targeted proteomics, phosphoproteomics, PTM analysis, and kinase activity when acquisition and metadata support them
- protein pathway analysis, protein network analysis, and RNA-protein concordance

High-value routes:

- RNA signature -> protein validation -> pathway or kinase activity -> drug target prioritization
- variant or fusion -> peptide evidence -> antigen prioritization
- proteogenomics with matched DNA, RNA, protein, and clinical data

Usually blocked without key inputs:

- peptide-level claims without raw spectra or peptide evidence
- PTM-site claims without localization probability or site-level quantification
- differential protein claims without biological replicates or clear batch design

### Metabolomics, lipidomics, and metabolic flux

Directly feasible:

- untargeted or targeted metabolomics QC, peak processing, annotation, normalization, and differential metabolite analysis
- lipid class, chain length, unsaturation, and lipid pathway analysis
- isotope tracing and metabolic flux analysis when tracer design, time points, and isotopologue data exist
- constraint-based metabolic modeling when a suitable model and objective are defined
- transcriptome-inferred single-cell or spatial metabolism scoring when measured metabolites are absent

High-value routes:

- metabolite changes -> pathway and enzyme expression -> cell type or spatial context -> external validation
- isotope tracing -> flux map -> gene or protein evidence -> perturbation or drug link
- microbiome function -> metabolite profile -> host immune or tumor state association

Usually blocked without key inputs:

- confirmed metabolite identity without MS/MS, retention time, standard, or high-confidence library evidence
- flux claims without isotope correction, model fit, and tracer design
- direct metabolite abundance claims from transcriptome-only scoring

### Metagenomics or microbiome

Directly feasible:

- read QC and host contamination review
- taxonomic profiling
- alpha and beta diversity
- differential abundance
- functional pathway profiling when shotgun data exist
- MAG reconstruction when depth and read structure support assembly
- host-microbe association when paired metadata or host omics exist

High-value routes:

- microbiome feature -> host immune or tumor state association -> external cohort or literature validation
- shotgun taxonomy plus function -> phenotype association -> pathway interpretation
- longitudinal microbiome shift -> treatment or response association

Usually blocked without controls or metadata:

- low-biomass microbiome claims without negative controls
- causal host-microbe claims without longitudinal, perturbation, or validation evidence
- confident strain or MAG claims without sufficient depth

### Structural bioinformatics and virtual screening

Directly feasible:

- structure retrieval or prediction
- domain, pocket, interface, or mutation mapping
- docking against a defined target
- ligand library filtering and prioritization
- MD stability review when compute and setup are adequate
- ADMET and chemoinformatics screening

High-value routes:

- expression or perturbation target -> structure validation -> docking -> ADMET -> pathway or cell-state interpretation
- mutation or residue hypothesis -> structure mapping -> MD or interface analysis
- drug prediction from transcriptomics -> structure-based prioritization when target and ligand evidence exist

Usually blocked without structural evidence:

- binding claims without a reliable structure, binding site, or validation control
- MD-based mechanistic claims from one short trajectory
- clinical drug prioritization without ADMET, literature, and experimental support

### Imaging, automatic segmentation, and virtual spatial omics

Directly feasible:

- image QC and annotation review
- radiomics feature extraction when segmentations exist
- automatic segmentation or contouring when labels or compatible pretrained models exist
- pathology WSI feature extraction or classification
- multiplex imaging cell phenotyping and spatial analysis
- virtual immunofluorescence or virtual spatial transcriptomics when paired validation data exist

High-value routes:

- image segmentation -> radiomics or pathomics features -> clinical endpoint validation
- measured mIF or IMC -> cell phenotype maps -> spatial neighborhood and immune-tumor interaction
- H&E plus measured spatial data -> virtual spatial model -> held-out slide validation

Usually blocked without annotations or paired measurements:

- segmentation model training without reliable labels
- virtual marker or virtual expression claims without measured paired validation
- patient-level outcome modeling without patient-level split and external validation

## Metadata Gates

Before promising an analysis branch, verify:

1. sample or patient IDs exist
2. grouping or endpoint labels are defined
3. batch or platform metadata are known
4. paired or longitudinal structure is explicit
5. validation material exists
6. covariates needed for confounding control exist
7. controls exist for low-biomass microbiome or imaging prediction tasks when needed
8. structure, ligand, annotation, or segmentation labels exist for structure and imaging tasks
9. HLA, expression, clonality, peptide evidence, or TCR evidence exist when antigen claims are requested
10. raw spectra, search database, FDR, and batch design exist when proteomics or immunopeptidomics claims are requested
11. blanks, pooled QC, internal standards, annotation evidence, isotope correction, or tracer design exist when metabolomics or flux claims are requested

If a gate is missing, mark the branch as blocked or exploratory-only.

## Publication-Path Heuristics

Shortest common paths:

- bulk discovery -> public validation -> concise mechanism discussion
- single-cell state discovery -> pathway plus trajectory -> public cohort validation
- single-cell discovery -> spatial support -> external cohort validation
- clinical cohort signal -> public expression support -> targeted single-cell follow-up

Choose the shortest route that can support the target claim with the existing data. Do not create a larger pipeline than the data can defend.
