# Coverage

This file defines the complete capability scope of `biocarp`. The skill must cover routine biomedical analysis, oncology-focused translational analysis, public-data reproduction, current method comparison, and newer frontier methods.

## Coverage Contract

When a task falls into a capability group:

1. Use `index.md` to select local reference files.
2. Follow the complete workflow, figure, and issue-review requirements from the selected files.
3. If a method family is under-specified, update the most specific local reference file before implementing a recurring or central analysis.
4. Use official documentation, primary papers, current issue trackers, and disease-specific recent literature before making method-level claims.

## Capability Groups

`biocarp` must cover these groups:

- sequence and alignment: sequence IO, sequence manipulation, alignment, alignment files, database access
- read processing: read QC, trimming, alignment, contamination review
- RNA-seq and expression: RNA quantification, differential expression, expression matrix analysis
- single-cell and spatial: scRNA-seq, scATAC-seq, multiome, spatial transcriptomics
- variant analysis: variant calling, copy number, phasing, imputation
- epigenomics: ChIP-seq, ATAC-seq, methylation, Hi-C
- metagenomics and microbiome: 16S, ITS, shotgun metagenomics, metatranscriptomics, MAGs, microbiome statistics
- genomics and assembly: genome assembly, genome annotation, genome intervals, genome engineering, primer design
- regulatory and causal: gene regulatory networks, causal genomics, RNA structure
- temporal and ecological: time-series genomics, ecological genomics
- immunology and clinical: immunoinformatics, clinical databases, TCR/BCR, epidemiological genomics
- specialized omics: proteomics, metabolomics, alternative splicing, chemoinformatics, liquid biopsy
- RNA biology: small RNA-seq, epitranscriptomics, CLIP-seq, ribo-seq
- phylogenetics and evolution: phylogenetics, population genetics, comparative genomics
- structural and systems: structural biology, systems biology, molecular interaction modeling
- screens and cytometry: CRISPR screens, perturbation screens, flow cytometry, CyTOF, multiplex tissue imaging
- pathway and integration: pathway analysis, multi-omics integration, restriction analysis
- infrastructure: visualization, machine learning, workflow management, reporting, experimental design, long-read sequencing
- end-to-end workflows: FASTQ-to-result pipelines and publication-ready result packages

## Local Reference Placement

Use these files first:

- `workflows.md`: routine executable workflows and complete figure requirements
- `execution.md`: project control, sub-agent use, goal handling, tool deployment, figure inspection, and phase reports
- `learning.md`: user-level assessment, proactive method suggestions, user habit records, bug learning, and method updates
- `methods.md`: route and package selection
- `tools.md`: package-family comparison
- `single-cell-advanced.md`: advanced single-cell, spatial, perturbation, virtual cell, single-cell drug prediction
- `bulk-inference.md`: bulk regulator, pathway, deconvolution, co-expression, score inference
- `metagenomics.md`: microbiome and metagenomics
- `structural.md`: structure prediction, docking, molecular dynamics, virtual screening, ADMET
- `imaging.md`: radiomics, pathomics, automatic segmentation, automatic contouring, multiplex imaging, virtual multiplex immunofluorescence, virtual spatial transcriptomics, pathology imaging
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
