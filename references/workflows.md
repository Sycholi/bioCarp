# Workflows

Use this file as the current method baseline before writing analysis scripts. It is selected through `index.md` and complements `routing.md`, `methods.md`, and `tools.md`.

This file is not a fixed package list. For every real project, update the route from official package documentation and recent papers in the same disease, modality, and endpoint. Prefer documentation and papers published or updated in the last 3 years when they exist. Use older sources only for canonical methods that remain standard.

## Source Discipline

Before running a module:

1. Read the current official package vignette, manual, or pipeline documentation.
2. Read representative recent papers using the same data type and disease context.
3. Extract preprocessing, QC, model choice, comparison design, required figures, signature figures, and known limitations.
4. Read `platforms.md` when platform, chemistry, instrument, acquisition mode, or sample handling can affect QC or interpretation.
5. Read `parameters.md` when thresholds, normalization, integration, model choices, databases, or software options can change the conclusion.
6. Write a module figure manifest before declaring the module complete.
7. Record package version, genome or annotation version, database version, platform, chemistry, acquisition mode, and key parameters.
8. Deploy missing required tools when feasible and record the installation in `工具部署记录.md`.
9. Inspect every figure and record per-figure interpretation as required by `execution.md`.
10. Regenerate failed figures until they pass inspection or a real blocker is documented.

## Detailed Companion Layers

Use these companion files for detailed routes that should not be duplicated here:

- `upstream.md` for raw FASTQ, BCL, BAM, CRAM, mzML, vendor MS files, demultiplexing, alignment, quantification, and workflow outputs
- `platforms.md` for sequencing, single-cell, spatial, MS, imaging, sample-handling, acquisition, and platform-output differences
- `parameters.md` for threshold, normalization, integration, model, database, and software-option effects on results
- `variants.md` for germline, somatic, CNV, SV, HLA, MSI, TMB, and mutational signatures
- `immunopeptidomics.md` for antigen peptides, MHC binding prediction, neoantigens, immunopeptidomics, and TCR-pMHC follow-up
- `single-cell-advanced.md` for advanced single-cell, spatial, perturbation, annotation, communication, trajectory, velocity, GRN, and drug-prediction modules
- `multiomics.md` for paired or unpaired bulk, single-cell, spatial, imaging, proteogenomic, metabolomic, and host-microbe integration
- `epigenomics.md` for ATAC, ChIP, CUT&Tag, CUT&Run, methylation, Hi-C, motif, footprinting, and regulatory interpretation
- `proteomics.md` for DDA, DIA, TMT, LFQ, PTM, phosphoproteomics, targeted proteomics, and proteogenomics
- `metabolomics.md` for untargeted and targeted metabolomics, lipidomics, isotope tracing, metabolic flux, and metabolic modeling
- `clinical-research.md` for clinical design taxonomy, sample size, power, endpoint definition, SAP logic, safety, PRO, implementation, health economics, translational study logic, and reporting
- `causal-inference.md` for target trial emulation, real-world evidence, external controls, matching, weighting, and quasi-experimental designs
- `clinical-data.md` for EHR, registry, REDCap, OMOP, FHIR, CDISC, SDTM, ADaM, terminology, and clinical data quality
- `evidence-synthesis.md` for systematic review, meta-analysis, network meta-analysis, Mendelian randomization, and pharmacovigilance
- `genetic-epidemiology.md` for GWAS, PheWAS, PRS, fine mapping, colocalization, TWAS, QTL, LDSC, and biobank genetics
- `specialized-omics.md` for small RNA, splicing, long-read transcriptomics, CLIP-seq, Ribo-seq, epitranscriptomics, RNA editing, and liquid biopsy
- `statistics.md` for model diagnostics, visualization, figure construction, clinical prediction plots, and report tables

## Bulk RNA-seq And Microarray

Current route:

1. Verify sample sheet, group labels, pairing, batch, library type, gene identifiers, and raw-count versus normalized-matrix status.
2. If starting from FASTQ, prefer `nf-core/rnaseq` or an equivalent documented workflow. Preserve FastQC, alignment or Salmon output, gene count matrix, MultiQC, software versions, genome build, and annotation version.
3. For raw RNA-seq counts, use `DESeq2`, `edgeR`, or `limma-voom` according to design and sample size. For microarray, perform platform-specific background correction, normalization, and probe annotation before `limma`.
4. Filter low-information features before modeling, normalize, inspect library size and sample-level structure, then fit the stated design.
5. Include batch, pairing, tissue source, treatment, and clinical group in the design matrix when supported by metadata.
6. Use shrinkage, quasi-likelihood, voom precision weights, or moderated statistics when appropriate, and keep the sample or patient as the inference unit.
7. Run ORA and preranked GSEA with versioned gene sets. Use `clusterProfiler`, `fgsea`, `msigdbr`, `ReactomePA`, or equivalent tools.
8. Add deconvolution only when the claim needs cell composition context and a reference is defensible.
9. Validate signatures or directions in an independent cohort when the request is publication-oriented.

Required figures:

- MultiQC or equivalent report when starting from FASTQ
- sample QC, library size or density, mean-variance trend, PCA or MDS, sample correlation heatmap
- DE volcano, MA or smear plot, top-gene heatmap, contrast summary
- ORA dot or bar plot, GSEA running-score plot, ridge plot, enrichment network or term-similarity plot when many terms are reported
- deconvolution composition and group comparison plots when deconvolution is used
- validation cohort effect plot, Kaplan-Meier, forest, or ROC only when endpoints support them

Primary sources to check:

- nf-core/rnaseq documentation
- DESeq2 Bioconductor vignette
- edgeR User's Guide and RNAseq123 workflow
- limma User's Guide and limma-voom workflow
- clusterProfiler book and enrichplot documentation
- `bulk-inference.md` for TF activity, pathway activity, deconvolution, signature scoring, and co-expression modules

## Single-Cell RNA-seq

Current route:

1. Import raw count matrices or processed objects with sample-level metadata intact.
2. Record platform, chemistry, sample handling, dissociation or nuclei protocol, fixation, sequencing instrument, raw pipeline, read structure, and reference version. Use `platforms.md` when the data come from 10x, BD, MGI, BGI, Singleron, Parse, ScaleBio, Fluent, SMART-seq, or another platform with nonstandard output.
3. Run per-sample QC for counts, detected genes, mitochondrial fraction, ribosomal fraction when relevant, doublets, ambient RNA, cell-cycle effects, and batch structure.
4. Normalize with the selected route, usually Seurat `SCTransform` or log-normalization for R-first workflows. Use Bioconductor `SingleCellExperiment` or Scanpy routes when the object ecosystem requires it.
5. Integrate only after checking whether biology and batch are separable. In Seurat v5 workflows, prefer layer-aware integration when it fits the object structure. Use Harmony, RPCA, scVI, or scANVI only when their assumptions fit the data.
6. Quantify integration quality with iLISI, cLISI, kBET, ASW or silhouette, graph connectivity, marker preservation, and sample or patient composition when integration affects the conclusion.
7. Cluster at multiple resolutions, annotate with manual markers plus reference transfer where useful, and preserve marker evidence for every final label.
8. Quantify cluster purity and heterogeneity with ROGUE, marker coherence, ASW or silhouette, cluster size, clustree or resolution stability, and reference-label agreement when annotation or subtype claims depend on clusters.
9. For group comparisons, use sample-aware pseudobulk or replicate-aware tools when biological replicates exist. Treat cell-level tests as descriptive unless the design justifies them.
10. Run lineage subclustering before trajectory, communication, CNV, or functional state modules.
11. Use `parameters.md` to record QC thresholds, doublet assumptions, ambient correction, normalization, integration, dimensions, neighbor count, clustering resolution, and marker thresholds with before-after cell counts.

Required figures:

- per-sample QC violin, ridge, and scatter plots, doublet and ambient RNA summaries, cell counts by sample
- platform, chemistry, vendor summary, barcode rank, sequencing saturation, mapping, and sample-retention plots when raw or vendor summaries are available
- PCA elbow or variance plots before final clustering
- integration diagnostics by sample, batch, condition, and major cell type
- integration metric plots: iLISI, cLISI, kBET, ASW or silhouette, graph connectivity, marker preservation, and batch-versus-biology comparison when integration is used
- cluster quality plots: ROGUE score distribution or heatmap, ASW or silhouette, cluster size, marker-coherence panels, and clustree or resolution stability plots when clusters drive biological claims
- UMAP or t-SNE by sample, condition, cluster, major annotation, fine annotation, and key markers
- marker dot plots, heatmaps, feature plots, and annotation evidence panels
- cell fraction by sample or patient, pseudobulk summary, DE volcano or heatmap, pathway activity plot

Primary sources to check:

- Seurat v5 vignettes
- Scanpy documentation when AnnData is the working object
- OSCA and Bioconductor single-cell workflows
- Single-cell best-practices reviews and the current online best-practices guide
- muscat, edgeR, DESeq2, or limma documentation for sample-aware testing
- ROGUE documentation and paper for cluster purity and heterogeneity
- LISI, scIB, and kBET documentation or benchmark papers for integration and batch-mixing metrics

## Trajectory, Pseudotime, Potency, And RNA Velocity

Current route:

1. Run trajectory only after confirming that the selected cells plausibly form a biological progression.
2. For topology and pseudotime visualization, use `Monocle3` or `slingshot`. For lineage-aware gene testing, add `tradeSeq`.
3. For differentiation potential, use `CytoTRACE` or `CytoTRACE2` only as a potency score, not as proof of lineage direction.
4. For RNA velocity, require spliced and unspliced counts or an equivalent velocity-ready object. Ordinary expression matrices cannot be used. Do not substitute heavily integrated or over-corrected expression for velocity input.
5. Use `scVelo` when Python is acceptable and the assumptions fit the data. Consider DeepVelo or TFvelo only when the question specifically needs their model class and their assumptions can be explained.
6. Anchor roots, terminal states, and direction with biology, time points, known markers, or experimental labels. State when direction remains uncertain.
7. Compare trajectory output with marker gradients, pathway gradients, and sample or condition distribution.
8. For multi-sample or multi-condition trajectories, include sample and condition density along pseudotime and consider condition-aware tools such as `condiments` or `Lamian` when the question requires formal comparison.

Required figures:

- selected lineage UMAP with clusters, samples, and known markers
- trajectory graph or lineage curves, root and terminal state plots, branch labels, pseudotime overlays
- sample, condition, or time-point density along pseudotime
- gene trends along pseudotime, branch-specific heatmaps, `tradeSeq` smoother plots when used
- potency score overlays and group summaries when potency analysis is used
- velocity arrow or streamline plots, latent time, velocity pseudotime, phase portraits, confidence diagnostics, driver-gene views when velocity is used

Primary sources to check:

- Monocle3 trajectory documentation
- slingshot and tradeSeq Bioconductor vignettes
- scVelo documentation
- CytoTRACE or CytoTRACE2 documentation and associated papers
- condiments or Lamian documentation when comparing trajectories across conditions

## Cell-Cell Communication

Current route:

1. Use only biologically meaningful annotated cell groups. Remove low-quality, low-count, or poorly defined groups before inference.
2. Preserve each biological sample before group-level summary. For differential communication, compare sample-level or patient-level results when replicate structure exists.
3. Run `CellChat` for R-first pathway-level network visualization when it fits the question.
4. Use `LIANA` or `LIANA+` when consensus ligand-receptor scoring, multiple resources, cross-condition comparison, or factor analysis of communication programs is needed.
5. Use `NicheNet` when the goal is ligand prioritization connected to target-gene programs in receiver cells.
6. For spatial data, include distance or neighborhood context when supported by the selected tool. Avoid treating transcript-only ligand-receptor predictions as direct physical proof.
7. Check whether results are driven by cell abundance, annotation granularity, sample pooling, or database choice.

Required figures:

- cell-group abundance and expression coverage diagnostics
- global interaction number and interaction strength plots
- source-target heatmaps, bubble plots, chord or circle plots, pathway-specific networks
- incoming and outgoing signaling role plots, contribution plots, centrality or pattern plots when supported
- ligand-target heatmaps and prioritized ligand plots when using NicheNet
- consensus or cross-condition program plots when using LIANA or LIANA+

Primary sources to check:

- CellChat tutorials
- LIANA and LIANA+ documentation
- NicheNet documentation and vignettes
- recent cell-cell communication reviews and benchmarking papers

## Spatial Transcriptomics

Current route:

1. Separate platform-specific preprocessing from downstream R or Python analysis.
2. Fix the object structure before analysis: `SpatialExperiment`, Seurat, AnnData, or Giotto. Preserve image, coordinates, spot or cell segmentation, slide, sample, region, and histology annotations.
3. Run platform-aware QC for counts, detected genes, mitochondrial fraction, tissue coverage, spot or cell density, and image alignment.
4. For R-first Visium or Visium HD projects, use Seurat spatial workflows when sufficient. Use Giotto Suite for richer spatial neighborhoods, multiscale spatial features, and technology-agnostic spatial workflows.
5. Use Squidpy or Scanpy-based tools when Python spatial statistics, image features, or AnnData integration are central.
6. Run deconvolution or label transfer with RCTD, cell2location, CARD, SpatialDWLS, or equivalent tools only when the reference is compatible.
7. Analyze spatially variable genes, domains, niches, cell-type neighborhoods, pathway activity, gradients, tissue structures, and spatial support for single-cell findings.
8. Use SPARK, SPARK-X, SpatialDE, SpatialDE2, nnSVG, MERINGUE, scBSP, SMASH, SpaGene, Splotch, or trendsceek for spatial expression patterns according to scale and model assumptions.
9. Use SLOPER, SpatialPCA, SpaceWalker, sosta, Sopa, FICTURE, CartoScope, or SPICEMIX when gradient, anatomical structure, or high-resolution molecular exploration is central.

Required figures:

- tissue image with spots or cells, QC overlays, sample or region maps
- spatial clusters, domains, regions, and histology-aligned annotations
- spatial feature plots, marker panels, pathway or signature activity maps
- deconvolution maps and cell-type composition summaries when deconvolution is used
- neighborhood enrichment, co-occurrence, proximity, or spatial interaction plots
- spatially variable gene plots, module maps, and selected locus or marker panels
- spatial gradient, anatomical structure, molecular-resolution map, and boundary-support plots when specialized spatial tools are used

Primary sources to check:

- Seurat spatial vignettes
- SpatialExperiment documentation when using Bioconductor spatial containers
- Giotto Suite documentation and recent Giotto Suite papers
- Squidpy tutorials and paper
- cell2location, RCTD, CARD, or SpatialDWLS documentation
- SPARK, SPARK-X, SLOPER, SpatialDE2, scBSP, SMASH, SpaGene, SpatialPCA, sosta, Sopa, and FICTURE documentation or papers when those methods drive claims

## TCR, BCR, And Immune Repertoire

Current route:

1. Verify receptor chain pairing, clonotype definition, contig quality, productive status, sample identity, and whether the data are bulk AIRR or paired single-cell VDJ.
2. Filter non-productive contigs, low-confidence contigs, barcode mismatches, and abnormal multi-chain cells before biological interpretation.
3. Define clonotypes explicitly by CDR3 amino acid, nucleotide sequence, V/J gene plus CDR3, or another stated rule. For BCR, inspect heavy and light chain pairing.
4. Use `scRepertoire` for Seurat-linked clonotype metadata, clonal abundance, diversity, sharing, and overlay plots.
5. Use `Startrac` when expansion, migration, tissue distribution, or state transition is central.
6. Use `immunarch` for bulk repertoire summaries and `scirpy`, `Dandelion`, or `dandelionR` when the Python, AIRR, or receptor-network ecosystem is stronger.
7. Interpret clonal sharing and transition only in light of sampling depth, tissue source, and patient identity.

Required figures:

- clonotype abundance, clonal size distribution, and homeostasis plots
- diversity curves, overlap or sharing heatmaps, repertoire similarity plots
- clonotype UMAP overlays, clone-state coupling plots, clone alluvial plots
- STARTRAC expansion, migration, transition, and tissue-distribution plots when used
- V, D, J gene usage and CDR3-length plots when repertoire composition is central

Primary sources to check:

- scRepertoire vignette and manual
- Dandelion and AIRR documentation when receptor-network or BCR-heavy workflows are used
- STARTRAC papers
- immunarch, scirpy, Dandelion, and AIRR documentation as needed

## CNV And Malignancy Inference

Current route:

1. Use transcriptome-based CNV inference only when tumor biology and normal references make it plausible.
2. Define reference normal cells carefully and document the gene-order file, genome build, denoising parameters, and cluster grouping.
3. Prefer per-sample CNV inference when enough cells exist, then compare patterns across samples. Cross-platform or cross-batch merged CNV inference needs extra caution.
4. Use raw or non-integrated expression data with gene genomic positions. Do not run CNV inference on integrated reductions.
5. Use `infercnv` when a heatmap-centered CNV workflow is desired and a reference group is available.
6. Use `CopyKAT` when tumor-versus-normal separation and aneuploidy calls are the main goal.
7. Cross-check malignant calls with epithelial or tumor markers, patient origin, CNV pattern consistency, and known tumor biology.
8. Do not interpret macrophage or immune apparent CNV signals without careful artifact review.

Required figures:

- reference and target cell annotation plots
- whole-genome CNV heatmap by chromosome and cell group
- malignant or aneuploid call overlay on embedding
- chromosome-level gain and loss summary
- subclone heatmap or dendrogram when subclones are claimed
- marker and CNV concordance plots

Primary sources to check:

- infercnv Bioconductor vignette and Broad documentation
- CopyKAT documentation and source paper
- tumor single-cell papers in the same disease

## ATAC-seq And Single-Cell ATAC-seq

Current route:

1. For bulk ATAC-seq, prefer ENCODE or nf-core style preprocessing when raw data are involved: FastQC, trimming, alignment, duplicate and blacklist filtering, Tn5 handling, peak calling, consensus peaks, read counting, differential accessibility, and MultiQC.
2. Require fragment-size distribution, TSS enrichment, FRiP, duplication, mapping rate, peak count, blacklist fraction, and replicate concordance or IDR when replicates support it.
3. For scATAC-seq, use Signac for Seurat-compatible analysis and ArchR for larger, richer ATAC workflows.
4. Build tile or peak matrices, run LSI, cluster, annotate from gene activity and marker accessibility, then test differential accessibility and motif activity.
5. Keep narrow peaks, broad accessibility regions, and consensus peaks conceptually separate. Differential accessibility needs biological replicates; pooled BAM-only significance is not enough.
6. Add RNA integration, WNN, peak-to-gene links, co-accessibility, footprinting, and browser tracks when the claim needs regulatory interpretation.

Required figures:

- fragment-size histogram, TSS enrichment, FRiP, peak count, mapping and duplication QC, replicate concordance or IDR
- LSI or UMAP embeddings by sample, cluster, and annotation
- gene activity plots, marker peak accessibility, differential accessibility volcano or heatmap
- motif enrichment or deviation plots, footprint plots when supported
- peak-to-gene, co-accessibility, and genome-browser coverage tracks at key loci

Primary sources to check:

- ENCODE ATAC-seq standards and pipeline documentation
- nf-core/atacseq output documentation
- Signac vignettes
- ArchR book and tutorials

## ChIP-seq, CUT&Tag, And CUT&Run

Current route:

1. For raw ChIP-seq data, prefer nf-core/chipseq, ENCODE-style ChIP-seq, or another documented pipeline that preserves QC and reproducibility outputs.
2. For CUT&Tag or CUT&Run, use nf-core/cutandrun or a protocol-appropriate workflow and record spike-in, IgG, input, or control strategy.
3. Separate transcription-factor narrow peaks, narrow histone marks, and broad histone marks. Choose peak calling and downstream summaries accordingly.
4. Require replicate concordance, FRiP or enrichment metrics, duplicate and mapping metrics, control handling, blacklist filtering, and normalized bigWig generation.
5. Use `DiffBind`, `csaw`, or `edgeR`-based strategies for differential binding according to design.
6. Use `ChIPseeker`, `ChIPpeakAnno`, deepTools, or equivalent tools for annotation, enrichment, metaplots, heatmaps, and genome-browser views.

Required figures:

- raw and aligned read QC, fragment or insert-size summaries, FRiP or enrichment metrics, replicate correlation
- peak count and peak-width summaries, IDR or overlap diagnostics when available
- peak annotation pie or bar plots, TSS distribution, genomic coverage plots
- metaplots and signal heatmaps around peaks, TSS, or gene bodies
- differential binding MA or volcano plots, binding heatmaps, PCA or MDS on peak counts
- normalized genome-browser tracks at key loci

Primary sources to check:

- nf-core/chipseq output documentation
- nf-core/cutandrun documentation for CUT&Tag or CUT&Run
- ENCODE ChIP-seq pipeline documentation
- DiffBind vignette
- ChIPseeker vignette

## DNA Methylation

Current route:

1. Identify platform first: 450K, EPIC, EPIC v2, WGBS, RRBS, or targeted bisulfite sequencing.
2. Preserve IDAT files when array data are available. For arrays, use `minfi`, `sesame`, `limma`, `DMRcate`, `missMethyl`, and annotation packages that match the array version.
3. Run sample and probe QC, detection P values, sex check when appropriate, beadcount or intensity checks, SNP and cross-reactive probe filtering, normalization, batch inspection, and cell-composition adjustment when needed.
4. Use beta values for interpretation and figures, and M values for statistical testing when the selected method expects them.
5. When merging 450K, EPIC, and EPIC v2, check manifests and common probes before any combined analysis.
6. Test DMPs and DMRs separately, then connect to genes, CpG island, shore, shelf, enhancer, or regulatory-region context.
7. For WGBS or RRBS, use pipeline-specific alignment, methylation extraction, strand-aware processing, and coverage filters before differential methylation testing.

Required figures:

- sample QC, density plots, MDS or PCA, beta-value distributions, control-probe plots when available
- DMP volcano or Manhattan-style plots, top-CpG heatmaps, CpG island or shore or shelf distribution
- DMR region tracks, regional methylation plots, annotation summaries
- gene-set or CpG-category enrichment plots, cell-composition plots when estimated

Primary sources to check:

- Bioconductor methylationArrayAnalysis workflow
- minfi, sesame, DMRcate, missMethyl documentation
- ENCODE or nf-core methylation pipeline documentation when raw sequencing data are used

## Clinical Cohort, Survival, And Prediction Models

Current route:

1. Define endpoint, time origin, censoring rule, inclusion criteria, missing-data handling, treatment line, molecular measurement timing, and train-validation split before modeling.
2. Start with baseline tables and event summaries before survival models.
3. Use Kaplan-Meier, log-rank tests, and Cox models for simple biomarker analysis. Check proportional hazards assumptions and time-varying effects when relevant.
4. Use competing-risk methods when the endpoint and competing events require them.
5. Use `rms` for richer clinical model diagnostics and nomograms when explicitly needed.
6. Use penalized models only with strict resampling, transparent feature selection, and external validation when possible.
7. Follow TRIPOD or TRIPOD+AI reporting principles for prediction models.
8. Avoid optimized cut-points unless the user explicitly asks for exploratory biomarker thresholds. Preserve continuous-variable analyses when possible.

Required figures:

- cohort flow and baseline summary tables
- Kaplan-Meier curves with risk tables, forest plots, Schoenfeld or proportional-hazards diagnostics when relevant
- risk-score distribution, calibration, decision curve, time-dependent ROC, Brier score, C-index, and nomogram plots when prediction models are used
- subgroup forest plots and sensitivity plots when subgroup claims are made

Primary sources to check:

- survival, survminer, rms, glmnet, timeROC documentation
- TRIPOD and TRIPOD+AI reporting statements

## Clinical Study Design, Sample Size, And Real-World Evidence

Current route:

1. Read `clinical-research.md` for clinical design taxonomy, endpoint, SAP, sample size, safety, PRO, implementation, health economics, translational study logic, and reporting.
2. Read `causal-inference.md` when the task involves observational treatment comparison, external controls, real-world evidence, target trial emulation, or causal claims.
3. Read `clinical-data.md` when data come from EHR, registry, claims, REDCap, OMOP, FHIR, CDISC, SDTM, ADaM, or mapped terminology.
4. Define the population, intervention or exposure, comparator, endpoint, time zero, follow-up, analysis set, missing-data process, and reporting standard before calculation or modeling.
5. Match the design family to the clinical question, endpoint, evidence gap, operational constraints, and reporting standard.
6. For controlled, uncontrolled, adaptive, sequential, diagnostic, prediction, implementation, or health-economic designs, state the assumptions that determine feasibility and interpretation.
7. For target trial emulation, write the target-trial protocol table before extracting data and check time-zero alignment, eligibility, treatment assignment, follow-up, and censoring.
8. Use `parameters.md` for endpoint assumptions, event rates, margins, dropout, matching, weighting, trimming, missing data, and sensitivity settings.

Required figures:

- study schema, participant flow, inclusion and exclusion flow, baseline table, and missingness plot
- sample-size assumptions, power or precision curves, event timeline, and interim boundary or operating-characteristic plots
- endpoint summary, Kaplan-Meier, cumulative incidence, longitudinal, recurrent-event, safety, and PRO plots as applicable
- covariate balance, weight distribution, effective sample size, target-trial alignment, and sensitivity plots for observational or real-world evidence analyses
- reporting checklist table selected from CONSORT, SPIRIT, STROBE, RECORD, STARD, TRIPOD+AI, PROBAST+AI, or relevant extensions

Primary sources to check:

- `clinical-research.md`
- `causal-inference.md`
- `clinical-data.md`
- CONSORT 2025, SPIRIT 2025, ICH E6(R3), ICH E9(R1), STROBE, RECORD, STARD, TRIPOD+AI, PROBAST+AI
- rpact, gsDesign, clinfun, pmsampsize, TrialEmulation, MatchIt, WeightIt, cobalt, OHDSI documentation

## Evidence Synthesis And Genetic Epidemiology

Current route:

1. Read `evidence-synthesis.md` for systematic review, meta-analysis, network meta-analysis, diagnostic or prognostic meta-analysis, MR, and pharmacovigilance.
2. Read `genetic-epidemiology.md` for GWAS, PheWAS, PRS, fine mapping, colocalization, TWAS, QTL, LDSC, and biobank genetics.
3. Define phenotype, exposure, outcome, ancestry, population, effect scale, inclusion criteria, data source, and quality-control rules before analysis.
4. Harmonize identifiers, genome builds, alleles, effect directions, sample overlap, and summary-statistic format before model fitting.
5. Use `parameters.md` for heterogeneity model, effect scale, MR instrument thresholds, GWAS QC, imputation quality, LD reference, PRS clumping, fine-mapping priors, and colocalization priors.

Required figures:

- study selection flow, risk-of-bias summary, forest, funnel, influence, heterogeneity, and network plots for evidence synthesis
- pharmacovigilance disproportionality and signal-prioritization plots when used
- GWAS sample QC, ancestry PCA, QQ, Manhattan, regional association, fine-mapping credible set, colocalization, PRS calibration, stratification, single-cell cell-type-trait association, driver-gene evidence, and validation plots

Primary sources to check:

- `evidence-synthesis.md`
- `genetic-epidemiology.md`
- PRISMA 2020, RoB 2, ROBINS-I, metafor, meta, netmeta, OpenGWAS, TwoSampleMR, PLINK2, SAIGE, REGENIE, PRSice, LDpred2, coloc, susieR, seismicGWAS, scDRS, CELLECT, MAGMA_Celltyping, RolyPoly, LDSC-SEG

## Multi-Omics And Public/Private Validation

Current route:

1. Select one anchor modality and one biological question before integrating.
2. Distinguish paired same-sample multi-omics, partially overlapping assays, and independent cohort integration before choosing a method.
3. Harmonize sample IDs, genome builds, gene IDs, feature names, assay dates, batch labels, and missingness.
4. Run modality-specific QC, normalization, and batch inspection before any joint model.
5. Use Seurat WNN for paired single-cell multimodal data when Seurat is the backbone.
6. Use MOFA2 for unsupervised multi-omics factors and variance decomposition.
7. Use mixOmics or DIABLO when supervised multi-omics feature selection is explicitly needed.
8. Use MultiAssayExperiment or equivalent structures when sample matching across assays is complex.
9. Interpret integrated signals through modality-specific results, then validate in external cohorts, spatial data, clinical data, or orthogonal assays.
10. Use `multiomics.md` for current tool selection, required figures, and single-cell, spatial, proteogenomic, metabolomic, imaging, or host-microbe integration details.

Required figures:

- sample overlap and missingness plots
- modality-specific QC and baseline embeddings
- WNN or integrated embeddings, modality weight plots, feature concordance plots
- MOFA factor plots, variance explained, factor-feature weights, factor-clinical association plots
- mixOmics CIM, correlation circle, circos, and network plots when used
- external validation plots tied to the main integrated signal

Primary sources to check:

- Seurat WNN and multimodal vignettes
- MultiAssayExperiment documentation
- MOFA2 manual and tutorials
- mixOmics and DIABLO documentation
- recent single-cell and cancer multi-omics review papers

## Metagenomics And Microbiome

Current route:

1. Identify assay type, sample source, controls, extraction kit, sequencing platform, primer region when relevant, and host contamination risk.
2. For 16S or ITS, run read QC, primer trimming, ASV inference, chimera removal, taxonomy assignment, diversity analysis, differential abundance, and publication figures with `QIIME 2`, `DADA2`, `mothur`, `phyloseq`, or equivalent tools.
3. For shotgun metagenomics, run read QC, adapter trimming, host removal, taxonomic profiling, functional profiling, and compositional statistics with tools such as `Kraken2`, `Bracken`, `MetaPhlAn`, `HUMAnN`, `mOTUs`, or `sylph`.
4. For MAG work, run assembly, binning, bin refinement, quality assessment, dereplication, taxonomy, annotation, and abundance quantification before biological interpretation.
5. Use compositional-data-aware differential abundance methods and preserve the sample or subject as the inference unit.
6. Connect microbiome features to tumor, immune, metabolite, treatment, or clinical data only after checking batch, antibiotics, diet, site, and time point.

Required figures:

- read QC, filtering-retention, host-removal, and control-contamination plots
- alpha diversity, beta diversity, ordination, and PERMANOVA or constrained ordination plots
- taxonomic composition bars, heatmaps, and differential abundance plots
- functional pathway abundance and coverage plots
- MAG completeness-contamination, taxonomy, abundance, and phylogenomic plots when MAGs are used
- host-microbe association, longitudinal, and validation plots when relevant

Primary sources to check:

- `metagenomics.md`
- QIIME 2, DADA2, MetaPhlAn, HUMAnN, Kraken2, Bracken, ANCOM-BC2, MaAsLin2, and MAG workflow documentation

## Structural Bioinformatics, Docking, Dynamics, And Virtual Screening

Current route:

1. Define target, isoform, mutation, structure source, ligand library, endpoint, and validation evidence.
2. Search experimental structures before using predicted structures.
3. Use current structure prediction tools only after checking supported molecule types, confidence metrics, access, and license.
4. Run docking with explicit receptor preparation, ligand preparation, pocket definition, control redocking when possible, and cross-method review for high-value claims.
5. Add molecular dynamics only when dynamic stability, conformation, membrane context, or binding-site persistence matters.
6. Use ADMET, toxicity, drug-likeness, and chemical diversity filters before prioritizing virtual hits.

Required figures:

- structure confidence, PAE, domain, pocket, interface, and active-site views
- docking pose, 2D interaction, score distribution, pose cluster, and validation plots
- MD energy, RMSD, RMSF, radius of gyration, SASA, hydrogen-bond, contact, PCA, clustering, and free-energy plots
- ADMET, chemical similarity, scaffold diversity, and top-compound summary plots

Primary sources to check:

- `structural.md`
- AlphaFold, Chai-1, Boltz, AutoDock Vina, GNINA, DiffDock, GROMACS, OpenMM, AMBER, RDKit, and ADMET documentation

## Imaging, Segmentation, Radiomics, And Virtual Spatial Omics

Current route:

1. Define modality, file format, resolution, scanner, annotation, label protocol, patient split, and endpoint.
2. For radiomics, preserve segmentation, preprocessing, feature extraction, feature stability, model training, validation, and reporting.
3. For automatic segmentation or contouring, use nnU-Net as a strong default baseline for compatible volumetric medical images; use MONAI, TotalSegmentator, MedSAM, Cellpose, StarDist, QuPath, Hover-Net, Mesmer, or platform-specific models when they better fit the input.
4. For multiplex imaging, run image QC, registration, segmentation, marker quantification, phenotype definition, neighborhood analysis, and spatial statistics. Use phenoptr, phenoptrReports, rtree, inForm, MCMICRO, ASHLAR, steinbock, cytomapper, histoCAT, imcRtools, Squidpy, or Giotto according to exported tables and image structure.
5. For virtual immunofluorescence, virtual staining, or virtual spatial transcriptomics, require measured paired data or a documented compatible pretrained model, then report prediction accuracy and uncertainty.
6. Split train, validation, and test data by patient or slide. Avoid tile-level leakage.

Required figures:

- raw image and channel montage, registration, tissue mask, segmentation, and QC overlays
- radiomics feature stability, model performance, calibration, and validation plots
- segmentation ground truth, prediction, error overlays, Dice, surface Dice, Hausdorff, volume agreement, and failure-case plots
- multiplex cell phenotype maps, marker heatmaps, UMAPs, neighborhood maps, and interaction plots
- measured-versus-predicted marker or expression maps, performance distributions, uncertainty maps, and external validation plots for virtual methods

Primary sources to check:

- `imaging.md`
- nnU-Net, MONAI, TotalSegmentator, Cellpose, StarDist, QuPath, phenoptr, phenoptrReports, CODEX, IMC, MIBI, ST-Net, Hist2ST, STimage, and virtual staining documentation or papers

## General Sequencing And Specialized Omics

Current route:

1. For sequence, alignment, variant, assembly, annotation, primer, and genome-interval tasks, define organism, genome build, reference database, read technology, sample design, and output unit before selecting tools.
2. For raw sequencing and workflow processing, use `upstream.md` and preserve raw QC, workflow logs, MultiQC, reference versions, and output matrices or alignment files.
3. For variant calling, use `variants.md` and preserve raw QC, alignment QC, duplicate or UMI handling, base recalibration or equivalent steps, variant filtering, annotation, and cohort-level summaries.
4. For antigen peptides, HLA, neoantigens, immunopeptidomics, and TCR-pMHC follow-up, use `immunopeptidomics.md`.
5. For genome assembly and annotation, preserve assembly graph or contigs, N50, BUSCO or equivalent completeness, contamination, repeat annotation, gene calls, and functional annotation.
6. For proteomics, phosphoproteomics, PTM analysis, and targeted proteomics, use `proteomics.md`.
7. For metabolomics, lipidomics, isotope tracing, metabolic flux, and metabolic modeling, use `metabolomics.md`.
8. For small RNA, single-cell total RNA, TotalX, CLIP-seq, ribo-seq, epitranscriptomics, alternative splicing, isoforms, long-read transcriptomics, RNA editing, liquid biopsy, cfDNA, ctDNA, CTC, and exosome data, read `specialized-omics.md` and follow assay-specific QC, normalization, identification, quantification, differential testing, annotation, and enrichment routes.
9. For platform-sensitive assays, read `platforms.md`. For parameter-sensitive assays, read `parameters.md`.
10. For flow cytometry, CyTOF, CRISPR screens, Perturb-seq, temporal genomics, ecological genomics, population genetics, phylogenetics, and comparative genomics, preserve assay-specific QC, design, statistical unit, and complete diagnostic figures.

Required figures:

- raw QC, alignment, mapping, duplication, coverage, contamination, and sample-level structure plots
- variant quality, Ti/Tv, allele frequency, annotation, oncoplot, lollipop, mutational signature, CNV, and validation plots when variants are analyzed
- HLA support, peptide candidate flow, MHC binding, immunopeptidomics motif, and antigen evidence matrix plots when antigen peptides are analyzed
- assembly, annotation, BUSCO, genome feature, synteny, phylogeny, and comparative genomics plots when genomes are analyzed
- proteomics raw QC, peptide or protein counts, missingness, normalization, PCA, volcano, heatmap, PTM-site, kinase, and protein network plots when proteomics is analyzed
- metabolomics peak QC, annotation, blank and pooled-QC review, PCA, volcano, heatmap, pathway, lipid class, isotopologue, flux, and model-fit plots when metabolomics or flux is analyzed
- small RNA length, mapping class, miRNA, isomiR, splicing, sashimi, isoform, CLIP, Ribo-seq, RNA modification, RNA editing, fragmentomics, ctDNA, CTC, exosome, and MRD plots when specialized assays are analyzed
- assay-specific PCA, heatmap, volcano, enrichment, pathway, network, and validation plots for specialized omics

Primary sources to check:

- official pipeline documentation for the selected assay
- primary workflow papers and current package documentation
- `tool-issues.md` for version and database risks

## Source Index

Last checked: 2026-05-27.

Use these as starting points, then confirm package versions and task-specific papers at run time:

- DESeq2 vignette: https://www.bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html
- nf-core/rnaseq: https://nf-co.re/rnaseq
- RNA-seq gene-level workflow: https://bioconductor.org/packages/release/workflows/vignettes/rnaseqGene/inst/doc/rnaseqGene.html
- edgeR plus limma RNAseq123 workflow: https://new.bioconductor.org/packages/release/workflows/vignettes/RNAseq123/inst/doc/limmaWorkflow.html
- limma User's Guide: https://www.bioconductor.org/packages/release/bioc/vignettes/limma/inst/doc/usersguide.pdf
- clusterProfiler vignette and book: https://www.bioconductor.org/packages/release/bioc/vignettes/clusterProfiler/inst/doc/clusterProfiler.html
- Seurat v5 integration: https://satijalab.org/seurat/articles/seurat5_integration
- Scanpy documentation: https://scanpy.readthedocs.io/en/latest/
- Seurat WNN: https://satijalab.org/seurat/articles/weighted_nearest_neighbor_analysis.html
- Seurat multimodal workflows: https://satijalab.org/seurat/articles/multimodal_vignette.html
- OSCA basic workflow: https://bioconductor.org/books/release/OSCA.basic/
- Single-cell best practices review: https://www.nature.com/articles/s41576-023-00586-w
- Monocle3 trajectories: https://cole-trapnell-lab.github.io/monocle3/docs/trajectories
- slingshot vignette: https://bioconductor.org/packages/release/bioc/vignettes/slingshot/inst/doc/vignette.html
- tradeSeq workflow: https://bioconductor.org/packages/release/bioc/vignettes/tradeSeq/inst/doc/tradeSeq.html
- scVelo documentation: https://scvelo.readthedocs.io/en/stable/
- DeepVelo paper: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-03148-9
- TFvelo paper: https://www.nature.com/articles/s41467-024-45661-w
- condiments package: https://bioconductor.org/packages/release/bioc/html/condiments.html
- Lamian paper: https://www.nature.com/articles/s41467-023-42841-y
- LIANA documentation: https://saezlab.github.io/liana/
- LIANA+ paper: https://www.nature.com/articles/s41556-024-01469-w
- NicheNet documentation: https://nichenet.be/
- Cell-cell communication review: https://www.nature.com/articles/s41576-023-00685-8
- Seurat spatial vignette: https://satijalab.org/seurat/articles/spatial_vignette
- SpatialExperiment package: https://bioconductor.org/packages/release/bioc/html/SpatialExperiment.html
- Giotto Suite: https://giottosuite.com/
- Squidpy paper: https://www.nature.com/articles/s41592-021-01358-2
- Squidpy tutorials: https://squidpy.readthedocs.io/en/stable/notebooks/tutorials/index.html
- cell2location tutorial: https://cell2location.readthedocs.io/en/latest/notebooks/cell2location_short_demo_colab.html
- scRepertoire vignette: https://new.bioconductor.org/packages/devel/bioc/vignettes/scRepertoire/inst/doc/vignette.html
- Dandelion paper: https://www.nature.com/articles/s41587-023-01734-7
- STARTRAC tumor T-cell dynamics paper: https://pubmed.ncbi.nlm.nih.gov/33900375/
- infercnv vignette: https://master.bioconductor.org/packages/release/bioc/vignettes/infercnv/inst/doc/inferCNV.html
- CopyKAT repository: https://github.com/navinlabcode/copykat
- ENCODE ATAC-seq standards: https://www.encodeproject.org/atac-seq/
- nf-core/atacseq output: https://nf-co.re/atacseq
- Signac documentation: https://stuartlab.org/signac/
- ArchR tutorial: https://www.archrproject.com/bookdown/
- nf-core/chipseq output: https://nf-co.re/chipseq
- nf-core/cutandrun: https://nf-co.re/cutandrun
- DiffBind package: https://bioconductor.org/packages/release/bioc/html/DiffBind.html
- ChIPseeker vignette: https://bioconductor.org/packages/release/bioc/vignettes/ChIPseeker/inst/doc/ChIPseeker.html
- Bioconductor methylation array workflow: https://bioconductor.org/packages/release/workflows/vignettes/methylationArrayAnalysis/inst/doc/methylationArrayAnalysis.html
- minfi vignette: https://bioconductor.org/packages/release/bioc/vignettes/minfi/inst/doc/minfi.html
- DMRcate manual: https://bioconductor.org/packages/release/bioc/html/DMRcate.html
- TRIPOD+AI statement: https://pmc.ncbi.nlm.nih.gov/articles/PMC11019967/
- MOFA2 manual: https://bioconductor.org/packages/release/bioc/html/MOFA2.html
- mixOmics documentation: https://mixomics.org/
