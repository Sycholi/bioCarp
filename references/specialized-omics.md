# Specialized Omics

Use this file for small RNA, miRNA, piRNA, lncRNA, circRNA, alternative splicing, isoforms, long-read transcriptomics, CLIP-seq, RIP-seq, Ribo-seq, epitranscriptomics, RNA editing, liquid biopsy, cfDNA, ctDNA, CTC, exosome, and other focused assays not covered by the main modality files.

## Intake

Before implementation, verify:

- assay type, organism, genome build, annotation release, library prep, size selection, strand, paired-end status, UMI, spike-in, and batch
- input level: FASTQ, BAM, junction counts, transcript abundance, circRNA candidates, small RNA counts, peak files, modification calls, isoform table, or liquid biopsy variant table
- endpoint: differential expression, isoform switching, splicing, RNA-binding protein target, translation efficiency, RNA modification, RNA editing, minimal residual disease, or biomarker validation

## Single-Cell Total RNA And Non-Poly(A) RNA

Use this module when the assay profiles total RNA, non-poly(A) RNA, nascent RNA, small RNA fragments, or mixed coding and noncoding transcript classes at single-cell level.

Current route:

1. Confirm whether the assay is TotalX, VASA-seq, Smart-seq-total, SUPeR-seq, RamDA-seq, MATQ-seq, or another total-RNA protocol.
2. Preserve chemistry, enzymatic steps, rRNA depletion, small-fragment handling, read structure, UMI convention, reference transcriptome, and gene biotype annotation.
3. Separate coding genes, lncRNA, circRNA-supporting reads, small RNA, intronic, antisense, and repetitive or ribosomal content when the protocol supports those classes.
4. Check protocol-specific background, rRNA fraction, fragment-size distribution, gene body coverage, strandedness, and annotation sensitivity before downstream clustering.
5. Compare results with standard poly(A)-based scRNA-seq only after aligning gene sets and transcript classes.

Required figures:

- protocol workflow and read-structure summary
- mapping category, rRNA fraction, gene biotype, and fragment-size plots
- coding versus noncoding RNA detection plots
- QC distributions by sample and chemistry
- selected noncoding RNA feature plots, dot plots, and trend plots when biologically central

## Small RNA And miRNA

Current route:

1. Run small-RNA-specific QC, adapter trimming, length distribution, contamination review, genome and miRNA database mapping.
2. Use nf-core/smrnaseq, miRDeep2, sRNAbench, miRge, miRTrace, ShortStack, or small RNA-specific aligners according to organism and annotation.
3. Separate miRNA, piRNA, tRNA fragments, rRNA fragments, and other small RNA classes when biologically relevant.
4. Use count-based differential analysis, isomiR review, target prediction, pathway enrichment, and validation against public resources.

Required figures:

- read length distribution, adapter trimming, mapping category, and small RNA class composition
- miRNA count PCA, heatmap, volcano, and top-feature plots
- isomiR or arm-switching plots when used
- target-gene and pathway plots

## Alternative Splicing, Isoforms, lncRNA, And circRNA

Current route:

1. For splicing, choose event-level, transcript-level, or junction-level analysis according to input and question.
2. Use rMATS, MAJIQ, SUPPA2, DEXSeq, JunctionSeq, LeafCutter, MISO, or SplAdder for short-read splicing when assumptions fit.
3. Use FLAIR, TALON, IsoQuant, Bambu, StringTie2, FLAMES, TAMA, Mandalorion, or Iso-Seq tools for long-read isoform analysis.
4. Use CIRI2, CIRCexplorer2, find_circ, circRNAprofiler, or DCC for circRNA discovery, then validate back-splice junctions and RNase R evidence when available.
5. Use FEELnc, CPC2, CPAT, CNCI, LncADeep, or annotation resources for lncRNA classification when relevant.

Required figures:

- junction or isoform QC and read-support plots
- PSI distribution, delta PSI volcano, event-type summary, and sashimi plots
- isoform structure plots, transcript model comparison, and isoform-switch plots
- circRNA back-splice junction support, circRNA class, and host-gene plots
- lncRNA class, coding potential, expression, and co-expression plots

## CLIP, RIP, RNA-Binding Proteins, And Ribo-seq

Current route:

1. For CLIP or RIP, preserve crosslink type, antibody, control, UMI, deduplication, peak calling, motif discovery, and target annotation.
2. Use nf-core/clipseq, CLIPper, PureCLIP, iCount, PARalyzer, Piranha, CTK, or PEAKachu according to protocol.
3. For Ribo-seq, preserve read length, P-site offset, frame periodicity, coding sequence coverage, and matched RNA-seq when available.
4. Use nf-core/riboseq, RiboTaper, RiboCode, riboWaltz, RiboProfiling, ORFquant, or Ribo-seQC according to question.

Required figures:

- read length, mapping, deduplication, and crosslink-site QC
- CLIP peak distribution, motif, metagene, target-gene, and replicate concordance plots
- Ribo-seq periodicity, frame distribution, P-site offset, metagene, translation efficiency, and ORF plots

## Epitranscriptomics And RNA Editing

Current route:

1. For m6A, m5C, pseudouridine, ac4C, or related assays, identify protocol, antibody or chemistry, controls, peak calling method, and transcript annotation.
2. Use exomePeak2, MeTPeak, MACS-style routes, RADAR, DRACH motif review, Nanopolish, Tombo, m6Anet, EpiNano, or direct RNA long-read tools according to input.
3. For RNA editing, use REDItools, SPRINT, JACUSA2, or related tools and filter DNA variants, mapping artifacts, strand bias, and repetitive regions.

Required figures:

- modification peak QC, motif, metagene, peak annotation, and differential modification plots
- direct RNA modification probability and per-site evidence plots when long-read methods are used
- RNA editing distribution, known-site overlap, editing level, and site-class plots

## Liquid Biopsy

Current route:

1. Preserve sample type, collection tube, plasma volume, extraction, UMI, panel, depth, fragment size, tumor fraction, and limit of detection.
2. Use ctDNA, cfDNA, methylation, fragmentomics, CTC, exosome RNA, or multi-analyte routes according to input.
3. For ctDNA variants, use UMI-aware callers and orthogonal validation where possible.
4. For cfDNA methylation or fragmentomics, preserve coverage, nucleosome, fragment size, end motif, and tissue-of-origin evidence.

Required figures:

- fragment-size distribution and library QC
- variant allele fraction and molecular support plots
- tumor fraction, MRD, or longitudinal monitoring plots
- methylation, fragmentomics, tissue-of-origin, and classifier performance plots when used

## Source Index

Last checked: 2026-05-28.

- nf-core/smrnaseq: https://nf-co.re/smrnaseq
- TotalX paper: https://www.nature.com/articles/s41587-026-03068-6
- TotalX open article: https://pmc.ncbi.nlm.nih.gov/articles/PMC12440072/
- miRDeep2: https://github.com/rajewsky-lab/mirdeep2
- sRNAbench: https://arn.ugr.es/srnatoolbox/srnabench/
- rMATS: https://rnaseq-mats.sourceforge.io/
- MAJIQ: https://majiq.biociphers.org/
- SUPPA2 paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC5866513/
- LeafCutter: https://github.com/davidaknowles/leafcutter
- IsoQuant: https://github.com/ablab/IsoQuant
- FLAIR: https://github.com/BrooksLabUCSC/flair
- TALON: https://github.com/mortazavilab/TALON
- Bambu: https://bioconductor.org/packages/release/bioc/html/bambu.html
- nf-core/clipseq: https://nf-co.re/clipseq
- nf-core/riboseq: https://nf-co.re/riboseq
- riboWaltz: https://bioconductor.org/packages/release/bioc/html/riboWaltz.html
- exomePeak2: https://bioconductor.org/packages/release/bioc/html/exomePeak2.html
- REDItools: https://github.com/BioinfoUNIBA/REDItools
