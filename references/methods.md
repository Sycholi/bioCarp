# Methods

Use this file for concise route and package selection after the request has been classified with `routing.md`.

Before implementation, use `index.md` to load the required companion files. This file chooses among common routes; companion files define current module workflows, advanced single-cell and spatial methods, bulk functional inference, figure requirements, and issue review.

Read `tools.md` as well when the user asks for broader package-family comparison, last-decade or last-two-decade method trends, or explicit strengths-versus-weaknesses across tools.

## Bulk Differential Expression

### Upstream FASTQ Processing

Use `upstream.md` before differential analysis when:

- raw FASTQ, BCL, BAM, CRAM, mzML, vendor MS files, or raw imaging files are the starting point
- the project needs standardized QC, alignment, quantification, matrix generation, or workflow deployment
- sample-sheet, lane, barcode, reference, or chemistry choices affect the result

### nf-core/rnaseq

Use when:

- raw FASTQ files need standardized RNA-seq preprocessing, gene counts, MultiQC, and versioned pipeline outputs

### limma

Use when:

- matrix is already normalized or microarray-like
- design is moderately complex
- speed matters

Strengths:

- mature and stable
- flexible design matrices
- strong for microarray and transformed expression data

### edgeR

Use when:

- count data are available
- library-size differences matter
- sample size is modest

Strengths:

- strong count-model foundation
- reliable dispersion modeling

### DESeq2

Use when:

- count matrix is clean
- a familiar publication-standard workflow is preferred
- shrinkage and straightforward result reporting matter

Strengths:

- highly recognizable in biomedical papers
- clean result objects

## Single-Cell Integration

### Scanpy or Bioconductor SingleCellExperiment

Use when:

- AnnData or SingleCellExperiment is already the natural object format
- Python or Bioconductor statistics are more appropriate than a Seurat-only workflow

### Seurat v5 Layer Integration, RPCA, Or Harmony

Use when:

- the task should follow the established R-first code style
- metadata-aware batch correction is enough
- figure production must stay close to the user's established style
- the object is already Seurat-based and downstream modules are R-first

Strengths:

- dominant pattern in the project-style reference
- easy handoff to downstream Seurat modules
- Seurat v5 layer-aware workflows are preferred for new Seurat projects when the object structure fits

### scVI

Use when:

- batch structure is strong
- cross-dataset integration is difficult
- Python interop is acceptable

Strengths:

- strong latent integration
- robust for heterogeneous cohorts

Cost:

- more environment complexity than Seurat plus Harmony

### CITE-seq, Multiome, And Single-Cell Multi-Omics

Use `multiomics.md` when:

- RNA and ADT, RNA and ATAC, methylation and RNA, or other modalities are paired or partly paired
- totalVI, MultiVI, Seurat WNN, Signac, ArchR, scGLUE, Cobolt, MOJITOO, muon, or Multigrate may be needed
- the analysis needs modality weights, missing-modality imputation, RNA-protein concordance, RNA-ATAC links, or cross-modal label transfer

## Cell Annotation

### Manual Marker Annotation

Use when:

- the biological question depends on fine-grained interpretation
- the user wants transparent oncology-specific labeling

Strengths:

- strongest alignment with the user's library
- easy to defend with marker panels and plots

### CellTypist or Similar Reference Tools

Use when:

- a first-pass label transfer is needed
- large or noisy datasets need rapid annotation

Best practice:

- treat automated labels as draft labels
- verify with marker expression before final naming

### Scoring And Gate-Based Annotation

Use when:

- a known immune, tumor, stromal, or functional state can be represented by marker sets or gating rules
- UCell, AUCell, scGate, scType, ProjecTILs, Symphony, popV, scPoli, or reference mapping adds useful evidence

Best practice:

- keep manual marker panels and automated calls side by side
- do not rename clusters from one automated label without marker support

## Pathway and Enrichment

### clusterProfiler

Use when:

- the goal is ORA, KEGG, GO, or GSEA in a familiar R workflow

Strengths:

- dominant in the user's library
- integrates well with `org.Hs.eg.db`, `org.Mm.eg.db`, and enrichplot

### fgsea

Use when:

- preranked enrichment should be fast
- many gene sets must be evaluated

### GseaVis or Custom GSEA Plotting

Use when:

- the final manuscript figure needs refined enrichment presentation

## Trajectory and State Transition

### Monocle3

Use when:

- a trajectory backbone and pseudotime visualization are needed

### slingshot plus tradeSeq

Use when:

- lineage-aware statistics matter
- smooth expression trends across pseudotime are needed

### CytoTRACE

Use when:

- the question is differentiation potential rather than a full lineage graph

### condiments or Lamian

Use when:

- trajectory differences across samples, groups, or conditions need formal comparison

### scVelo, DeepVelo, or TFvelo

Use when:

- spliced and unspliced counts exist and velocity-specific assumptions are satisfied
- DeepVelo or TFvelo is justified by the biological question and model assumptions

### CellRank, dynamo, Palantir, Waddington-OT, or destiny

Use when:

- terminal fate probabilities, vector-field dynamics, diffusion pseudotime, or transport-based fate mapping are central
- the data contain suitable time, differentiation, perturbation, or state-transition information

## Cell-Cell Communication

### CellChat

Use when:

- pathway-level ligand-receptor structure and network visualization are needed
- compatibility with the user's current codebase matters

Strengths:

- already common in the established analysis workflow

### NicheNet or Other Prior-Knowledge Tools

Use when:

- the goal is prioritizing ligand-to-target programs rather than only plotting networks

### LIANA or LIANA+

Use when:

- consensus ligand-receptor scoring across multiple methods or resources is needed
- cross-condition communication programs need a systematic comparison
- Python or mixed R/Python interop is acceptable

### COMMOT, SpaTalk, MISTy, MultiNicheNet, NicheCompass, or Tensor-cell2cell

Use when:

- spatial coordinates, condition-aware communication, multi-sample communication programs, or microenvironment modeling are required
- transcript-only communication results need spatial or target-program context

## CNV and Malignancy Inference

### infercnv

Use when:

- transcriptome-based CNV inference is sufficient
- reference normal cells are available

### fastCNV or Related Faster Tools

Use when:

- quicker iteration is needed
- the user already has a compatible local workflow

## TCR and BCR

### scRepertoire

Use when:

- clonotype integration with Seurat metadata is needed

### Startrac

Use when:

- tissue distribution, expansion, or transition metrics matter
- immune-ecology interpretation is central

### immunarch, scirpy, or Dandelion

Use when:

- bulk AIRR, Python AnnData, or richer receptor-network workflows are needed
- the local Seurat-linked scRepertoire route does not cover the required repertoire question

## Spatial Transcriptomics

### Seurat Spatial

Use when:

- the project is Visium-like and R-first
- the main need is spatial visualization, label transfer, or single-cell result support

### Giotto Suite

Use when:

- spatial neighborhoods, domains, multiscale analysis, image-aware structure, or platform-agnostic spatial workflows are central

### Squidpy or Scanpy Spatial

Use when:

- Python AnnData workflows, image features, co-occurrence, ligand-receptor, or neighborhood statistics are the strongest fit

### RCTD, cell2location, CARD, or SpatialDWLS

Use when:

- spot or region deconvolution is needed and a compatible single-cell reference exists

### DestVI, SPOTlight, STdeconvolve, SpatialDecon, STRIDE, Tangram, CellTrek, or CytoSPACE

Use when:

- spot-level, cell-level, or cross-platform spatial mapping needs a route beyond the default deconvolution tools
- the selected method matches platform resolution and reference structure

### SpatialExperiment

Use when:

- Bioconductor-native spatial data management is preferable before method-specific analysis

### STAGATE, DeepST, SEDR, SpaSEG, SpatialDE, nnSVG, or MERINGUE

Use when:

- spatial domain detection, spatially variable gene testing, or spatial graph representation is the main question
- the tool has current documentation and fits the platform resolution

## ATAC-seq and scATAC-seq

### nf-core/atacseq or ENCODE ATAC pipeline

Use when:

- raw bulk ATAC-seq reads need standardized preprocessing, QC, peak calling, consensus peaks, and differential accessibility-ready outputs

### Signac

Use when:

- scATAC-seq or multiome analysis should stay close to Seurat
- gene activity, motif analysis, coverage plots, and WNN integration are sufficient

### ArchR

Use when:

- large scATAC-seq projects need richer ATAC-native workflows, peak-to-gene links, motif deviations, trajectories, and browser tracks

### SnapATAC2, chromVAR, Cicero, TOBIAS, HOMER, MEME, or MACS3

Use when:

- large scATAC-seq, motif deviation, co-accessibility, footprinting, motif discovery, or updated peak calling is central

## ChIP-seq, CUT&Tag, and CUT&Run

### nf-core/chipseq or ENCODE-style pipelines

Use when:

- raw chromatin-profiling reads need reproducible preprocessing, QC, peak calling, normalized tracks, and reports

### nf-core/cutandrun

Use when:

- CUT&RUN or CUT&Tag raw reads need protocol-aware preprocessing, QC, peak calling, and normalized tracks

### DiffBind

Use when:

- differential binding from a peak count matrix and replicate-aware design is the main task

### ChIPseeker or ChIPpeakAnno

Use when:

- peak annotation, genomic distribution, average profiles, heatmaps, and enrichment plots are needed

## DNA Methylation

### minfi or sesame

Use when:

- Illumina methylation arrays require QC, normalization, and beta or M value processing

### DMRcate, limma, or missMethyl

Use when:

- DMPs, DMRs, or methylation-aware enrichment are needed

## Variants, HLA, And Antigen Peptides

### GATK, DeepVariant, Strelka2, Mutect2, or nf-core/sarek

Use when:

- germline or somatic SNV and indel discovery starts from WGS, WES, panel, or RNA-seq data
- standardized QC, variant calling, filtering, and annotation are required

### CNVkit, FACETS, PureCN, Sequenza, ASCAT, Manta, Delly, or GISTIC2

Use when:

- copy number, allele-specific copy number, structural variants, recurrent peaks, or tumor purity and ploidy are central

### OptiType, arcasHLA, HLA-HD, Polysolver, pVACtools, NetMHCpan, MHCflurry, MixMHCpred, or BigMHC

Use when:

- HLA typing, antigen peptide prediction, neoantigen prioritization, immunopeptidomics, or TCR-pMHC follow-up is requested

## Survival and Cohort Balancing

### survival plus survminer

Use when:

- KM and Cox are the main clinical outputs

### MatchIt

Use when:

- observational imbalance materially affects the clinical comparison
- the design truly calls for matching

### rms, glmnet, timeROC, or decision-curve tools

Use when:

- prediction modeling, penalized signatures, calibration, time-dependent discrimination, or clinical utility plots are explicitly requested

Use TRIPOD or TRIPOD+AI reporting principles when the task produces a prediction model.

## Multi-Omics Integration

### Seurat WNN

Use when:

- paired single-cell multimodal data are already in a Seurat-compatible structure

### MOFA2

Use when:

- unsupervised factors, variance decomposition, and cross-modality signal discovery are the main needs

### mixOmics or DIABLO

Use when:

- supervised multi-omics feature selection or group discrimination is explicitly needed

### MultiAssayExperiment

Use when:

- sample matching across assays is complex and needs a formal container

### totalVI, MultiVI, scGLUE, Cobolt, MOJITOO, muon, or MEFISTO

Use when:

- CITE-seq, RNA-ATAC multiome, unpaired single-cell modalities, missing-modality imputation, spatial or time-aware factors, or Python scverse workflows are better suited than a Seurat-only route

## Metagenomics And Microbiome

### QIIME 2, DADA2, or mothur

Use when:

- 16S rRNA or ITS amplicon reads need ASV or OTU processing, taxonomy assignment, diversity analysis, and publication figures

### Kraken2 plus Bracken

Use when:

- shotgun metagenomics needs fast read-level taxonomic profiling and species abundance estimates

### MetaPhlAn, mOTUs, or sylph

Use when:

- marker-based or containment-based taxonomic profiling is better suited to the database, compute, or cross-study comparability requirement

### HUMAnN

Use when:

- shotgun data need gene-family and pathway-level functional profiling

### ANCOM-BC2, ALDEx2, MaAsLin2, or LinDA

Use when:

- microbiome differential abundance or metadata association must account for compositionality, sparsity, covariates, or repeated measures

### MEGAHIT, metaSPAdes, metaFlye, CheckM2, GTDB-Tk, or DRAM

Use when:

- assembly, MAG reconstruction, genome quality assessment, microbial taxonomy, or functional annotation is central

### KneadData, decontam, StrainPhlAn, inStrain, VirSorter2, VIBRANT, CheckV, geNomad, PICRUSt2, AMRFinderPlus, ResFinder, or VFDB

Use when:

- contamination control, strain analysis, viral metagenomics, functional prediction, resistome, or virulence analysis is central

## Proteomics, Metabolomics, And Flux

### MaxQuant, FragPipe, MSFragger, DIA-NN, Spectronaut, OpenMS, or nf-core/quantms

Use when:

- raw DDA, DIA, LFQ, TMT, iTRAQ, PRM, SRM, or targeted proteomics needs identification, quantification, and QC

### MSstats, MSstatsTMT, MSstatsPTM, DEP, proDA, PhosR, PTM-SEA, or KSEA

Use when:

- differential protein abundance, TMT analysis, PTM analysis, phosphoproteomics, or kinase activity from proteomics data is needed

### XCMS, MZmine, MS-DIAL, GNPS, MetaboAnalystR, SIRIUS, HMDB, or LIPID MAPS

Use when:

- untargeted metabolomics, lipidomics, annotation, compound class analysis, or metabolite pathway analysis is needed

### IsoCor, AccuCor, INCA, OpenFLUX2, COBRApy, COBRA Toolbox, cameo, scFEA, or Compass

Use when:

- isotope correction, isotope tracing, 13C metabolic flux analysis, flux balance analysis, or single-cell metabolism inference is requested

## Structural Biology And Virtual Screening

### AlphaFold, ColabFold, AlphaFold 3, Chai-1, or Boltz

Use when:

- protein, complex, nucleic-acid, or biomolecular interaction structure prediction is needed and current tool support matches the molecule type

### AutoDock Vina, GNINA, Smina, rDock, or DiffDock

Use when:

- molecular docking, pose prediction, or structure-based virtual screening is needed

### GROMACS, OpenMM, AMBER, or NAMD

Use when:

- molecular dynamics is needed for stability, conformation, membrane context, binding-site persistence, or free-energy analysis

### RDKit, DeepChem, Therapeutics Data Commons, SwissADME, or ADMET tools

Use when:

- ligand preparation, library filtering, QSAR, ADMET, toxicity, or chemical-space analysis is needed

## Imaging, Segmentation, And Virtual Spatial Omics

### nnU-Net

Use when:

- automatic segmentation or contouring is needed for compatible CT, MRI, PET, or other volumetric medical images

### MONAI, TotalSegmentator, MedSAM, or SAM-derived models

Use when:

- medical image segmentation needs task-specific pretrained models, deep-learning pipelines, or broad organ segmentation

### Cellpose, StarDist, QuPath, Hover-Net, Mesmer, or ilastik

Use when:

- nuclei, cell, tissue, or multiplex-image segmentation is needed

### pyradiomics or radiomics pipelines

Use when:

- radiomics feature extraction, feature stability, and imaging model construction are central

### CODEX, MIBI, IMC, CyCIF, or multiplex IF analysis tools

Use when:

- measured multiplex tissue imaging needs channel QC, segmentation, phenotyping, and spatial statistics

### ST-Net, Hist2ST, HisToGene, THItoGene, iStar, STimage, or FineST

Use when:

- virtual spatial transcriptomics or histology-to-expression prediction is requested and paired validation exists

## Statistics And Visualization

### ComplexHeatmap, EnhancedVolcano, UpSetR, circlize, ggtree, maftools, Gviz, or plotgardener

Use when:

- publication-grade heatmaps, volcano plots, set intersections, circular plots, tree plots, oncoplots, or genome tracks are required

### lme4, glmmTMB, emmeans, metafor, riskRegression, pec, pROC, or timeROC

Use when:

- mixed models, marginal comparisons, meta-analysis, prediction metrics, calibration, ROC, or time-to-event model evaluation are required

## Practical Rule

Prefer tools that satisfy all three conditions:

1. fit the biological question
2. match the data structure
3. stay close to the user's existing project style

Only switch to a newer or less familiar tool when it clearly improves scientific fit or robustness.
