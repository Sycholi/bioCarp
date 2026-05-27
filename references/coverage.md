# Coverage

This file defines the complete capability scope of `biocarp`. The skill must cover routine biomedical analysis, oncology-focused translational analysis, clinical research design, platform-aware assay review, public-data reproduction, current method comparison, and newer frontier methods.

## Coverage Contract

When a task falls into a capability group:

1. Use `index.md` to select local reference files.
2. Follow the complete workflow, figure, and issue-review requirements from the selected files.
3. If a method family is under-specified, update the most specific local reference file before implementing a recurring or central analysis.
4. Use official documentation, primary papers, current issue trackers, and disease-specific recent literature before making method-level claims.

## Capability Groups

`biocarp` must cover these groups:

- sequence and alignment: sequence IO, sequence manipulation, alignment, alignment files, database access
- read processing: read QC, trimming, demultiplexing, alignment, quantification, UMI handling, contamination review, and workflow execution
- platform and parameter review: sequencing platforms, single-cell chemistries, spatial platforms, MS instruments, imaging scanners, acquisition modes, sample handling, run design, and parameter effects on results
- RNA-seq and expression: RNA quantification, differential expression, expression matrix analysis
- single-cell and spatial: scRNA-seq, CITE-seq, scATAC-seq, multiome, spatial transcriptomics, spatial proteomics, perturbation, velocity, communication, and neighborhood analysis
- variant analysis: germline, somatic, copy number, structural variants, phasing, imputation, HLA typing, MSI, TMB, signatures, and antigen-peptide handoff
- epigenomics: ChIP-seq, CUT&Tag, CUT&Run, ATAC-seq, scATAC-seq, methylation, Hi-C, motif, footprinting, co-accessibility, and chromatin interaction
- metagenomics and microbiome: 16S, ITS, shotgun metagenomics, metatranscriptomics, virome, strain analysis, MAGs, microbiome statistics, and host-microbe integration
- genomics and assembly: genome assembly, genome annotation, genome intervals, genome engineering, primer design
- regulatory and causal: gene regulatory networks, causal genomics, RNA structure
- temporal and ecological: time-series genomics, ecological genomics
- immunology and clinical: immunoinformatics, clinical databases, clinical trial design, real-world evidence, target trial emulation, TCR/BCR, epidemiological genomics
- clinical research and evidence: interventional, observational, diagnostic, prognostic, prediction, implementation, health-services, health-economic, translational, adaptive, master-protocol, registry, EHR, REDCap, OMOP, FHIR, CDISC, sample size, SAP, meta-analysis, network meta-analysis, pharmacovigilance, Mendelian randomization
- specialized omics: proteomics, phosphoproteomics, immunopeptidomics, metabolomics, lipidomics, isotope tracing, metabolic flux, alternative splicing, long-read transcriptomics, CLIP-seq, ribo-seq, epitranscriptomics, RNA editing, chemoinformatics, and liquid biopsy
- genetic epidemiology: GWAS, PheWAS, PRS, fine mapping, colocalization, QTL, TWAS, heritability, genetic correlation, and biobank genetics
- RNA biology: small RNA-seq, epitranscriptomics, CLIP-seq, ribo-seq
- phylogenetics and evolution: phylogenetics, population genetics, comparative genomics
- structural and systems: structural biology, systems biology, molecular interaction modeling
- screens and cytometry: CRISPR screens, perturbation screens, flow cytometry, CyTOF, multiplex tissue imaging
- pathway and integration: pathway analysis, multi-omics integration, bulk-to-single-cell interpretation, proteogenomics, metabolome-host integration, and restriction analysis
- infrastructure: visualization, statistics, clinical modeling, machine learning, workflow management, reporting, experimental design, long-read sequencing
- end-to-end workflows: FASTQ-to-result pipelines and publication-ready result packages

## Local Reference Placement

Use these files first:

- `workflows.md`: routine executable workflows and complete figure requirements
- `execution.md`: project control, sub-agent use, goal handling, tool deployment, figure inspection, and phase reports
- `learning.md`: user-level assessment, proactive method suggestions, user habit records, bug learning, and method updates
- `platforms.md`: sequencing, single-cell, spatial, MS, imaging, sample-handling, acquisition, and platform-output differences
- `parameters.md`: threshold, normalization, integration, model, database, and software-option effects on results
- `methods.md`: route and package selection
- `tools.md`: package-family comparison
- `upstream.md`: FASTQ-to-matrix, FASTQ-to-BAM, raw QC, demultiplexing, alignment, quantification, workflow pipelines, and MultiQC outputs
- `variants.md`: germline variants, somatic variants, CNV, SV, HLA typing, mutational signatures, and variant-to-antigen handoff
- `immunopeptidomics.md`: antigen peptides, neoantigens, MHC binding prediction, immunopeptidomics, and TCR-pMHC follow-up
- `single-cell-advanced.md`: advanced single-cell, spatial, perturbation, virtual cell, single-cell drug prediction
- `bulk-inference.md`: bulk regulator, pathway, deconvolution, co-expression, score inference
- `multiomics.md`: bulk, single-cell, spatial, imaging, proteogenomic, metabolomic, and host-microbe multi-omics integration
- `epigenomics.md`: ATAC, ChIP, CUT&Tag, CUT&Run, methylation, Hi-C, motif analysis, footprinting, and regulatory interpretation
- `proteomics.md`: DDA, DIA, TMT, LFQ, phosphoproteomics, PTM analysis, targeted proteomics, and proteogenomics
- `metabolomics.md`: untargeted and targeted metabolomics, lipidomics, isotope tracing, metabolic flux, and constraint-based metabolic modeling
- `metagenomics.md`: microbiome and metagenomics
- `structural.md`: structure prediction, docking, molecular dynamics, virtual screening, ADMET
- `imaging.md`: radiomics, pathomics, automatic segmentation, automatic contouring, multiplex imaging, virtual multiplex immunofluorescence, virtual spatial transcriptomics, pathology imaging
- `clinical-research.md`: clinical study design taxonomy, sample size, power, endpoints, SAP logic, safety, PRO, implementation, health economics, and reporting standards
- `causal-inference.md`: target trial emulation, external controls, real-world evidence, matching, weighting, g-methods, and quasi-experimental designs
- `clinical-data.md`: EHR, registry, REDCap, OMOP, FHIR, CDISC, SDTM, ADaM, terminology, and clinical data quality
- `evidence-synthesis.md`: systematic review, meta-analysis, network meta-analysis, diagnostic and prognostic meta-analysis, Mendelian randomization, and pharmacovigilance
- `genetic-epidemiology.md`: GWAS, PheWAS, PRS, fine mapping, colocalization, QTL, TWAS, LDSC, and biobank genetics
- `specialized-omics.md`: small RNA, miRNA, splicing, isoforms, long-read transcriptomics, CLIP-seq, Ribo-seq, epitranscriptomics, RNA editing, cfDNA, ctDNA, CTC, and exosome assays
- `statistics.md`: downstream statistics, clinical models, visualization, figure checks, and report tables
- `tool-issues.md`: version conflicts, unresolved issues, forum errors, GitHub issues
- `literature.md` and `public-data.md`: literature and public data extraction
- `data-assessment.md`: feasible and blocked analysis branches

## Minimum Update Rule

When a new method family is needed, add:

- task trigger
- accepted input formats
- current route
- required figures
- standard tools
- issue checks
- source index
  - platform and parameter effects when they can change the result
