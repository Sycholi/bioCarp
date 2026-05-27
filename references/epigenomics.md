# Epigenomics

Use this file for ATAC-seq, scATAC-seq, CUT&Tag, CUT&Run, ChIP-seq, histone marks, TF binding, DNA methylation, Hi-C, chromatin interaction, chromVAR, footprinting, motif analysis, co-accessibility, and regulatory interpretation.

## Intake

Before implementation, verify:

- assay type, organism, genome build, antibody or mark, control type, replicate structure, read length, paired-end status, spike-in, blacklist, and peak type
- input level: FASTQ, BAM, bigWig, narrowPeak, broadPeak, fragment file, methylation IDAT, bisulfite BAM, Hi-C pairs, cool, hic, or processed matrix
- biological question: accessibility, TF binding, histone mark, methylation, regulatory network, chromatin loop, enhancer-promoter link, disease-associated variant, or multiome integration

## ATAC-seq And scATAC-seq

Current route:

1. For bulk ATAC-seq, run read QC, trimming, alignment, duplicate handling, mitochondrial read review, blacklist filtering, Tn5 shift, peak calling, consensus peaks, read counting, replicate concordance, and differential accessibility.
2. For scATAC-seq, preserve fragment files, cell barcode QC, TSS enrichment, nucleosome signal, fragments per cell, blacklist fraction, peak matrix, gene activity, LSI, clustering, annotation, and motif deviation.
3. Use MACS2 or MACS3 for peak calling when appropriate. Use Signac, ArchR, SnapATAC2, chromVAR, Cicero, Monocle3, or scGLUE according to object ecosystem and question.
4. Run motif enrichment, motif deviation, footprinting, co-accessibility, peak-to-gene links, and genome-browser tracks when regulatory interpretation is central.

Required figures:

- fragment size, TSS enrichment, nucleosome signal, FRiP, peak count, duplicate rate, mapping rate, blacklist fraction, and replicate concordance
- LSI or UMAP by sample, cluster, annotation, and QC metrics for scATAC-seq
- differential accessibility volcano or heatmap
- motif enrichment, chromVAR deviation heatmap, and TF activity plots
- footprint plots when supported
- Cicero or co-accessibility links and peak-to-gene plots
- genome-browser tracks at key loci

## ChIP-seq, CUT&Tag, And CUT&Run

Current route:

1. Separate narrow TF marks, narrow histone marks, broad histone marks, and protocol-specific CUT&Tag or CUT&Run assumptions.
2. Use ENCODE-style pipelines, `nf-core/chipseq`, `nf-core/cutandrun`, or protocol-specific routes when raw data exist.
3. Use MACS2, MACS3, SEACR, SICER, Genrich, HOMER, deepTools, DiffBind, csaw, ChIPseeker, ChIPpeakAnno, MEME Suite, FIMO, or TOBIAS as needed.
4. Preserve normalized bigWig tracks, peaks, replicate QC, FRiP, cross-correlation where suitable, metaplots, heatmaps, and differential binding results.

Required figures:

- alignment, duplicate, FRiP, peak count, enrichment, cross-correlation, and replicate concordance
- peak genomic annotation and genomic distribution
- signal metaplot and heatmap around peaks, TSS, enhancers, or selected regions
- differential binding volcano, MA plot, heatmap, and sample correlation
- motif enrichment, motif occurrence, footprint, and TF binding evidence plots
- genome-browser tracks at key loci

## DNA Methylation

Current route:

1. For Illumina arrays, preserve IDAT files, detection P values, bead count, sex check, SNP and cross-reactive probe filtering, normalization, beta or M values, DMPs, DMRs, and methylation-aware enrichment.
2. For bisulfite sequencing, use Bismark, bwa-meth, BS-Seeker2, methylDackel, methylKit, DSS, bsseq, metilene, ViewBS, or BSXplorer according to input and design.
3. Use minfi, sesame, ChAMP, RnBeads, DMRcate, missMethyl, methylKit, DSS, or bsseq according to platform and statistical goal.
4. Connect methylation to expression, chromatin, survival, or cell-type composition only after checking sample matching and feature annotation.

Required figures:

- array intensity, detection P value, sex check, density, MDS or PCA, and sample correlation
- bisulfite conversion, coverage, methylation distribution, and CpG context plots
- DMP volcano, DMR track, regional methylation heatmap, and annotation plots
- methylation-expression correlation and enrichment plots when integrated

## Hi-C And Chromatin Interaction

Current route:

1. Preserve raw read QC, valid pairs, cis-trans ratio, contact matrix resolution, restriction enzyme or protocol, normalization, and compartment or loop calling parameters.
2. Use HiC-Pro, Juicer, cooler, HiCExplorer, FitHiC, HiCCUPS, Mustache, FAN-C, GENOVA, or cooltools according to input and required output.
3. For promoter capture, HiChIP, PLAC-seq, or Micro-C, choose protocol-aware peak and loop analysis.
4. Connect loops to genes, enhancers, ATAC peaks, ChIP peaks, variants, and expression only when genome build and sample matching are controlled.

Required figures:

- valid pair, distance decay, cis-trans ratio, duplication, and matrix QC plots
- contact maps, compartment eigenvector plots, TAD boundaries, loops, and insulation score plots
- differential interaction plots when design supports them
- loop-to-gene and enhancer-promoter integration plots

## Source Index

Last checked: 2026-05-28.

- ENCODE ATAC-seq: https://www.encodeproject.org/atac-seq/
- ENCODE pipelines: https://www.encodeproject.org/pipelines/
- MACS3: https://macs3-project.github.io/MACS/
- deepTools: https://deeptools.readthedocs.io/
- HOMER: http://homer.ucsd.edu/homer/
- MEME Suite: https://meme-suite.org/
- TOBIAS: https://github.com/loosolab/TOBIAS
- Signac: https://stuartlab.org/signac/
- ArchR: https://www.archrproject.com/bookdown/
- SnapATAC2: https://scverse.org/SnapATAC2/
- chromVAR: https://bioconductor.org/packages/release/bioc/html/chromVAR.html
- Cicero: https://cole-trapnell-lab.github.io/cicero-release/
- Bismark: https://www.bioinformatics.babraham.ac.uk/projects/bismark/
- methylKit: https://bioconductor.org/packages/release/bioc/html/methylKit.html
- DSS: https://bioconductor.org/packages/release/bioc/html/DSS.html
- bsseq: https://bioconductor.org/packages/release/bioc/html/bsseq.html
- minfi: https://bioconductor.org/packages/release/bioc/html/minfi.html
- ChAMP: https://bioconductor.org/packages/release/bioc/html/ChAMP.html
- RnBeads: https://rnbeads.org/
- HiC-Pro: https://github.com/nservant/HiC-Pro
- Juicer: https://github.com/aidenlab/juicer
- cooler: https://cooler.readthedocs.io/
- HiCExplorer: https://hicexplorer.readthedocs.io/
