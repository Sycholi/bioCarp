# Upstream Processing

Use this file for FASTQ-to-matrix, FASTQ-to-BAM, raw sequencing QC, demultiplexing, alignment, quantification, workflow execution, and cross-assay preprocessing.

## Intake

Before implementation, verify:

- assay type, organism, genome build, annotation release, sequencing platform, library chemistry, read length, strandedness, UMI status, paired-end status, and sample sheet
- raw data source, checksum, lane structure, barcode structure, adapter sequence, index hopping risk, sample swaps, and expected output unit
- compute environment, container support, reference-cache location, thread count, memory, GPU availability, and storage requirement
- whether the task needs raw-count preservation, transcript-level quantification, allele-specific output, splice-aware alignment, or spliced/unspliced matrices
- whether `platforms.md` or `parameters.md` is required because chemistry, barcode structure, acquisition mode, vendor output, or threshold settings can change the result

## Sequencing Workflow Selection

Current route:

1. Prefer documented workflows such as `nf-core`, ENCODE pipelines, GATK Best Practices, 10x Genomics pipelines, or official assay pipelines when raw data are central.
2. Use custom scripts only when the assay, species, or study design is outside well-maintained workflows.
3. Pin workflow version, container, reference genome, annotation, database, and command line.
4. Preserve raw logs, MultiQC, per-sample QC, final matrices, BAM or CRAM files when needed, and workflow reports.
5. For public data, record accession, run table, sample mapping, and any mismatch between metadata and sequencing files.

Primary routes:

- bulk RNA-seq: `nf-core/rnaseq`, STAR plus Salmon, HISAT2, RSEM, kallisto, featureCounts, tximport
- scRNA-seq: `nf-core/scrnaseq`, Cell Ranger, STARsolo, kallisto-bustools, simpleaf, alevin-fry, velocyto when spliced or unspliced counts are needed
- platform-specific single-cell: Cell Ranger for 10x, BD Rhapsody Sequence Analysis Pipeline for BD, ScaleBio Seq Suite for ScaleBio, Parse Split Pipe or Trailmaker-supported exports for Parse, PIPseeker for Fluent, Singleron or vendor-supported workflows for GEXSCOPE, and documented vendor workflows for MGI, BGI, DNBelab, or other platforms
- scATAC or multiome: Cell Ranger ARC, Cell Ranger ATAC, Signac-compatible fragment files, ArchR-compatible fragment files
- spatial transcriptomics: Space Ranger, Xenium Ranger, CosMx SMI tools, platform vendor outputs, Giotto or Squidpy import routes
- ATAC-seq: `nf-core/atacseq`, ENCODE ATAC pipeline
- ChIP-seq: `nf-core/chipseq`, ENCODE ChIP pipeline
- CUT&Tag or CUT&Run: `nf-core/cutandrun`
- methylation: `nf-core/methylseq`, Bismark, bwa-meth, methylDackel
- small RNA-seq: `nf-core/smrnaseq`, miRDeep2, sRNAbench
- CLIP-seq or ribo-seq: `nf-core/clipseq`, `nf-core/riboseq`, assay-specific pipelines
- WGS, WES, targeted panels: `nf-core/sarek`, GATK, DeepVariant, Sentieon when licensed
- long-read DNA or RNA: Minimap2, pbmm2, Dorado, Guppy, NanoPlot, FLAIR, TALON, StringTie2, IsoQuant
- proteomics raw MS: `nf-core/quantms`, FragPipe, MaxQuant, DIA-NN, OpenMS
- microbiome: `nf-core/ampliseq`, `nf-core/mag`, QIIME 2, DADA2, Kraken2, MetaPhlAn, HUMAnN

## Required Figures

- per-sample read quality, base composition, adapter content, GC content, duplication, sequence length, overrepresented sequence, and trimming summary
- demultiplexing and sample-retention summary
- alignment, mapping, insert size, strandedness, gene body coverage, duplication, UMI saturation, and coverage plots when relevant
- feature assignment, transcript quantification, detected genes, detected peaks, detected ASVs, detected peptides, or detected metabolites according to assay
- MultiQC or equivalent dashboard
- sample-swap, sex-check, contamination, and genotype concordance plots when metadata or genotype data support them
- workflow runtime, failed-step, and resource summary when deployment or reproducibility matters

## Common Tool Risks

- Cell Ranger, Space Ranger, and vendor pipelines have chemistry, reference, and license constraints.
- Seurat v5 and AnnData conversion can lose layers, raw counts, reductions, or metadata if conversion is casual.
- STARsolo, alevin-fry, kallisto-bustools, and Cell Ranger can produce different gene-count conventions.
- RNA velocity requires spliced and unspliced information; ordinary expression matrices are insufficient.
- GTF version, gene biotype filtering, mitochondrial gene naming, and genome build affect downstream biological interpretation.
- Public SRA metadata can be incomplete or inconsistent with file names.

## Source Index

Last checked: 2026-05-28.

- nf-core/rnaseq: https://nf-co.re/rnaseq
- nf-core/scrnaseq: https://nf-co.re/scrnaseq
- nf-core/sarek: https://nf-co.re/sarek
- nf-core/atacseq: https://nf-co.re/atacseq
- nf-core/chipseq: https://nf-co.re/chipseq
- nf-core/cutandrun: https://nf-co.re/cutandrun
- nf-core/methylseq: https://nf-co.re/methylseq
- nf-core/quantms: https://nf-co.re/quantms
- Cell Ranger: https://www.10xgenomics.com/support/software/cell-ranger
- STARsolo: https://github.com/alexdobin/STAR
- alevin-fry and simpleaf: https://alevin-fry.readthedocs.io/
- kallisto-bustools: https://www.kallistobus.tools/
- MultiQC: https://multiqc.info/
- GATK documentation: https://gatk.broadinstitute.org/
- ENCODE pipelines: https://www.encodeproject.org/pipelines/
