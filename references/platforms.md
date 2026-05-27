# Platforms

Use this file when assay platform, chemistry, instrument, sample handling, sequencing depth, acquisition mode, or preprocessing parameter choices can change the result.

## Intake

Before analysis or study design, record:

- sample source, tissue handling, storage, dissociation, nuclei extraction, fixation, ischemia time, viability, cell size, debris, red blood cells, necrosis, and expected rare-cell fraction
- platform, chemistry, kit version, barcode structure, UMI structure, sample multiplexing method, read structure, read length, sequencing instrument, run mode, and reference version
- raw pipeline, cell-calling method, demultiplexing method, expected cells, loaded cells, recovered cells, multiplet expectation, sequencing saturation, median genes, median UMI, mapping rate, and batch structure
- for MS data: instrument class, acquisition mode, chromatography, ion mode, labeling, fractionation, library type, raw format, converter, search database, FDR, missingness, and QC sample design
- for imaging data: scanner, resolution, tile size, staining, registration, segmentation, annotation protocol, patient split, and export format

## Single-Cell Platforms

### 10x Genomics Chromium

Typical context:

- droplet-based 3' or 5' gene expression, VDJ, Feature Barcode, CITE-seq, Flex, Multiome, ATAC, and Visium-linked workflows
- default raw route is Cell Ranger, Cell Ranger ARC, Cell Ranger ATAC, Space Ranger, Xenium Ranger, or Loupe-derived exports

Key analysis points:

- chemistry version and read structure must match Cell Ranger or alternative pipeline settings
- 3' and 5' assays differ in transcript end, VDJ support, and some downstream expectations
- Flex probe-based data require platform-specific QC; mitochondrial reads may be less informative than in standard 3' or 5' assays
- overloading, poor viability, debris, damaged cells, or nuclei leakage increase multiplets and ambient RNA
- feature barcode, hashtag, or VDJ data need separate QC before merging with RNA labels

Parameter effects:

- expected cell count changes barcode calling, low-quality cell inclusion, and apparent library complexity
- mitochondrial, UMI, and gene thresholds change cell-type retention; sample-specific distributions should drive thresholds
- ambient correction can remove true marker expression if contamination and endogenous expression are not separated
- integration strength can erase tissue, treatment, or disease states if batch and biology are confounded

### BD Rhapsody

Typical context:

- microwell-based single-cell WTA, targeted RNA panels, AbSeq, sample tag multiplexing, and immune profiling
- default raw route is BD Rhapsody Sequence Analysis Pipeline or vendor-supported workflow

Key analysis points:

- targeted panels and WTA have different feature spaces and should not be treated as identical whole-transcriptome assays
- sample tag calling, multiplet calls, and panel detection limits need explicit review
- BD outputs may require careful conversion before Seurat or Scanpy workflows

Parameter effects:

- panel design determines detectable biology; absent genes may reflect panel design rather than true absence
- sample tag thresholds change singlet, multiplet, and negative calls
- targeted RNA sensitivity can improve selected genes but limits unbiased discovery

### MGI, BGI, And DNBelab

Typical context:

- DNBSEQ sequencing, DNBelab C-series single-cell workflows, and MGI-linked service outputs
- spatial context may include Stereo-seq from STOmics or MGI service workflows

Key analysis points:

- barcode structure, read structure, pipeline choice, and reference version must match the vendor workflow
- DNBSEQ read properties and index handling should be recorded when integrating with Illumina-derived cohorts
- raw output may need vendor-specific parsing before standard matrix analysis

Parameter effects:

- reference mismatch, barcode parsing errors, and chemistry mismatch can appear as low mapping, low UMI, or abnormal cell calling
- platform mixing with 10x, BD, Parse, Scale, or Singleron requires explicit platform diagnostics before integration

### Singleron GEXSCOPE

Typical context:

- microwell-based single-cell RNA-seq, FFPE-compatible or specialized Singleron kits, and Singleron software outputs

Key analysis points:

- verify kit version, cell or nucleus input, FFPE status, read structure, and vendor pipeline
- FFPE and fixed-sample workflows can change gene-body coverage, mitochondrial metrics, and RNA degradation patterns
- tissue dissociation reagents and sample preservation can affect immune and stromal cell recovery

Parameter effects:

- fixed or FFPE samples require different QC expectations from fresh cells
- cell calling and matrix import should be checked against vendor summaries before downstream filtering

### Other Documented Vendor Platforms

Typical context:

- commercial single-cell or spatial workflows with vendor-specific barcode structure, pipeline outputs, and data reports

Key analysis points:

- verify the exact platform name, chemistry, software, read structure, output matrix format, and support documentation before analysis
- do not assume 10x defaults apply to a non-10x matrix
- request or inspect raw vendor QC, barcode whitelist, reference version, feature annotation, and cell-calling report

Parameter effects:

- wrong barcode parsing or chemistry settings can produce a plausible-looking matrix with distorted cell counts and UMI distributions
- platform-specific cell-calling thresholds affect rare-cell retention and doublet risk

### Parse Biosciences Evercode

Typical context:

- combinatorial barcoding, fixed cells or nuclei, high sample count, large cell count, and instrument-free library preparation
- default processing uses Parse-supported software such as Split Pipe or Trailmaker exports when available

Key analysis points:

- fixation, washing, and split-pool barcoding can cause cell or nuclei loss; record input and recovered counts
- combinatorial indexing changes multiplet logic and sample multiplexing interpretation
- large sample numbers require careful metadata, barcode, and batch review before integration

Parameter effects:

- barcode collision, sample multiplexing, and batch layout affect doublet and sample identity calls
- fixed-sample biology and stress signatures should be interpreted separately from fresh dissociation effects

### ScaleBio QuantumScale

Typical context:

- combinatorial barcoding, fixed samples, high-throughput perturbation or cohort-scale designs, and ScalePlex multiplexing
- default route uses ScaleBio Seq Suite or supported Nextflow workflow

Key analysis points:

- cell identification uses platform-specific barcode combinations; standard droplet-only assumptions are not enough
- large-scale designs need plate, well, sample, and batch metadata preserved from the start
- perturbation screens need guide, sample, and cell barcode linkage checks

Parameter effects:

- plate layout and barcode configuration affect recovered cell count and multiplet estimates
- filtering can change sample representation strongly when many samples are pooled

### Fluent BioSciences PIPseq

Typical context:

- particle-templated instant partition sequencing, Illumina single-cell prep workflows, and PIPseeker outputs

Key analysis points:

- use PIPseeker or documented compatible routes for raw data processing
- non-model organisms need reference and barcode compatibility checks before trusting output summaries
- integration with 10x or other platforms requires platform-aware diagnostics

Parameter effects:

- sample multiplexing and reference quality can strongly alter cell calling and gene detection
- raw converter and read structure errors can create inconsistent matrices across pipelines

### SMART-seq, Plate-Based, Split-Seq, sci-RNA-seq, And Full-Length Routes

Typical context:

- full-length transcript coverage, lower cell numbers, isoform or allele-specific questions, or plate-linked metadata

Key analysis points:

- no UMI or different UMI structure changes normalization and duplicate interpretation
- batch is often plate, well, reagent lot, or capture day
- full-length data fit isoform, splicing, and allele analyses better than many droplet 3' assays

Parameter effects:

- library-size normalization, gene detection thresholds, and plate effects can dominate clustering
- dropout and transcript-length bias differ from droplet UMI assays

## Single-Cell Failure Sources

Common reasons for poor data:

- low viability, delayed processing, ischemia, freeze-thaw damage, harsh dissociation, high debris, necrosis, mucus, fat, calcification, blood contamination, and high ambient RNA
- overloaded cells or nuclei, inaccurate concentration, large cell size, aggregates, poor filtering, and incomplete dead-cell removal
- wrong chemistry, wrong barcode whitelist, wrong reference, poor sequencing quality, low read depth, low saturation, index hopping, lane or sample swap
- FFPE degradation, nuclei leakage, ribosomal or intronic dominance, tissue-specific mitochondrial expectations, and strong dissociation stress

Required review:

- compare vendor summary metrics with downstream QC plots
- stratify QC by sample, platform, chemistry, tissue, patient, processing day, and batch
- inspect retained and removed cell types to avoid removing fragile or rare populations only by global thresholds
- record every threshold and its cell-count effect in `分析状态.md` or the project QC report

## Spatial Platforms

### 10x Visium, Visium HD, And Slide-Based Capture

Key points:

- spot, bin, or capture-area size determines whether deconvolution or cell-level interpretation is justified
- histology image, tissue mask, fiducial alignment, permeabilization, and section quality affect expression maps
- Space Ranger outputs need image, coordinate, and count matrix integrity checks before Seurat, Giotto, or Squidpy analysis

### Xenium, CosMx, MERSCOPE, MERFISH, And In Situ Platforms

Key points:

- gene panel design, decoding quality, segmentation, cell boundary assignment, and transcript density control interpretation
- cell segmentation errors can change cell type calls, neighborhood statistics, and ligand-receptor signals
- required QC includes transcript density, negative controls, segmentation overlays, cell size, panel detection, and field-of-view effects

### Stereo-seq, Slide-seq, DBiT-seq, Seq-Scope, And High-Resolution Spatial Methods

Key points:

- bin size, coordinate scaling, tissue registration, capture efficiency, and large field of view affect memory and analysis choices
- high resolution does not automatically mean single-cell accuracy without segmentation or deconvolution support
- platform-specific pipelines and coordinate systems must be preserved before object conversion

## Sequencing Instruments And Run Design

Record:

- Illumina, MGI DNBSEQ, Ultima, Oxford Nanopore, PacBio, or other sequencer
- read length, paired-end or single-end, index strategy, flow cell, lane distribution, expected depth, and run quality
- whether batch is aligned with biological group

Parameter effects:

- read depth changes detected genes, saturation, allele support, peak calling, ASV detection, peptide identification, and variant sensitivity
- longer reads can improve splicing, isoform, VDJ, assembly, and structural-variant interpretation
- lane distribution and dual indexing affect sample swap and index hopping review

## Mass Spectrometry Platforms

### Proteomics

Key points:

- DDA, DIA, diaPASEF, TMT, iTRAQ, LFQ, PRM, and SRM generate different missingness, quantification precision, and downstream models
- Orbitrap, Q-TOF, timsTOF, triple quadrupole, and MALDI-based systems require method-specific raw conversion and QC
- search engine, spectral library, enzyme, missed cleavages, modifications, protein database, FDR, match-between-runs, and protein grouping all change results

Parameter effects:

- TMT ratio compression, channel design, reference channel, and batch layout affect group comparison
- DIA window scheme, library strategy, and retention-time alignment affect identification and quantification
- missing-value imputation can create artificial group separation if not checked with missingness plots

### Metabolomics And Lipidomics

Key points:

- LC-MS, GC-MS, CE-MS, MALDI-MSI, and NMR differ in metabolite coverage, reproducibility, annotation depth, and preprocessing
- ion mode, chromatography, adducts, isotope peaks, retention-time drift, blank subtraction, pooled QC, internal standards, and batch order must be recorded
- annotation confidence should distinguish confirmed standards, MS/MS library match, putative class, and unknown features

Parameter effects:

- peak picking, alignment, gap filling, blank filtering, QC correction, normalization, and adduct grouping can change the final feature table
- pathway interpretation should be based on annotation confidence, not only feature-level P values

## Imaging Platforms

Record:

- WSI scanner, objective, pixel size, staining, batch, color profile, tissue mask, tile size, annotation quality, segmentation protocol, and patient-level split
- DICOM or NIfTI modality, voxel spacing, reconstruction kernel, contrast phase, contour protocol, structure names, and preprocessing
- multiplex imaging platform, channel order, spillover, autofluorescence, registration, segmentation model, and marker panel

Parameter effects:

- tile-level splits can leak patient information and overstate performance
- color normalization, resampling, contour interpolation, and segmentation errors change radiomics and pathomics features
- multiplex channel normalization and segmentation directly alter phenotype maps and neighborhood statistics

## Design And Parameter Review Output

For every platform-sensitive project, produce:

- platform and chemistry table
- sample handling and run design table
- raw QC and vendor summary review
- parameter-decision table with before-after sample, cell, feature, read, peak, peptide, metabolite, or image counts
- blocked or exploratory analysis list caused by platform limits
- figure manifest covering all platform-specific QC and signature plots

## Source Index

Last checked: 2026-05-28.

- 10x Chromium GEM-X 3' v4 user guide: https://www.10xgenomics.com/support/single-cell-gene-expression/documentation/steps/library-prep/chromium-gem-x-single-cell-3-v4-gene-expression-user-guide
- 10x Cell Ranger documentation: https://www.10xgenomics.com/support/software/cell-ranger
- 10x spatial support: https://www.10xgenomics.com/support/spatial-gene-expression
- BD Rhapsody pipeline documentation: https://bd-rhapsody-bioinfo-docs.genomics.bd.com/
- BD Rhapsody sample tag analysis: https://bd-rhapsody-bioinfo-docs.genomics.bd.com/steps/steps_sample_tag.html
- MGI Stereo-seq technology: https://global-mgitech.com/technologies/stereo-seq-technology/
- Singleron GEXSCOPE: https://singleron.bio/products/gexscope-single-cell/
- Parse Evercode WT: https://www.parsebiosciences.com/products/evercode-wt/
- ScaleBio Seq Suite documentation: https://scalebio.github.io/ScaleRna-docs/
- ScaleBio QuantumScale: https://scale.bio/single-cell-rna-sequencing-kit/
- Fluent BioSciences PIPseq and PIPseeker: https://www.fluentbio.com/
- MZmine LC-MS workflow: https://mzmine.github.io/mzmine_documentation/workflows/lcmsworkflow/lcms-workflow.html
- MetaboAnalystR LC-MS workflow: https://www.metaboanalyst.ca/MetaboAnalyst/resources/vignettes/LCMSMS_Raw_Spectral_Processing.html
- FragPipe DIA tutorial: https://fragpipe.nesvilab.org/docs/tutorial_DIA.html
- MSstats documentation: https://msstats.org/
- pmultiqc: https://pmultiqc.quantms.org/
