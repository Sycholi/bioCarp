# Reference Index

Use this file first after `SKILL.md`. It maps task types to the smallest set of reference files needed for an analysis.

## Core Layers

Read these in order:

1. `routing.md` for request intake, data-type routing, and paper-oriented output logic.
2. `r-style.md` for the abstract R analysis code style before writing substantial R scripts.
3. `coverage.md` for complete capability scope.
4. `execution.md` for sub-agent use, goal handling, tool deployment, figure inspection, result interpretation, and phase documentation.
5. `learning.md` for user-level assessment, proactive method suggestions, bug learning, and method updates.
6. `platforms.md` when platform, chemistry, instrument, acquisition mode, sample handling, or run design affects the result.
7. `parameters.md` when threshold, normalization, integration strength, model setting, database, or software option can change the conclusion.
8. `methods.md` for concise package choice.
9. `workflows.md` for current module-level QC, modeling, figure, and source requirements.
10. `tools.md` when the task needs method-family comparison or a newer challenger route.
11. `upstream.md`, `variants.md`, `immunopeptidomics.md`, `multiomics.md`, `epigenomics.md`, `proteomics.md`, `metabolomics.md`, `clinical-research.md`, `causal-inference.md`, `clinical-data.md`, `evidence-synthesis.md`, `genetic-epidemiology.md`, `specialized-omics.md`, `statistics.md`, or another modality file when the task enters that specific domain.
12. `tool-issues.md` before using version-sensitive, web-service, fast-moving, or error-prone tools.

## Task-Specific Layers

### Literature, Public Data, And Study Design

Use:

- `literature.md`
- `public-data.md`
- `data-assessment.md`
- `clinical-research.md` for protocol, endpoint, sample size, implementation, health economics, translational, or clinical reporting questions
- `causal-inference.md` for target trial emulation, real-world evidence, external controls, or causal claims
- `clinical-data.md` for EHR, registry, REDCap, OMOP, FHIR, CDISC, SDTM, ADaM, terminology, or clinical data quality
- `evidence-synthesis.md` for systematic reviews, meta-analysis, network meta-analysis, Mendelian randomization, or pharmacovigilance

Triggers:

- disease-specific or modality-specific study design
- public dataset reproduction
- "what can this dataset do?"
- last-decade method or paper landscape
- public validation cohort selection
- interventional, observational, adaptive, master-protocol, diagnostic, prognostic, prediction, implementation, health-economic, translational, or real-world evidence study design
- sample-size, power, target trial emulation, or clinical data standardization

### Current Module Execution

Use:

- `workflows.md`
- `execution.md`
- `methods.md`
- `tools.md`
- `platforms.md` when platform or chemistry can change QC, processing, or interpretation
- `parameters.md` when thresholds, normalization, integration, peak calling, search, annotation, or model settings can change the result

Triggers:

- bulk RNA-seq or microarray
- scRNA-seq
- spatial transcriptomics
- TCR or BCR
- CNV or malignancy inference
- ATAC-seq, scATAC-seq, ChIP-seq, CUT&Tag, CUT&Run, or methylation
- sequence analysis, alignment, variant calling, genome assembly, genome annotation, Hi-C, long-read sequencing, RNA biology, proteomics, metabolomics, flow cytometry, CRISPR screens, or phylogenetics
- survival, prediction modeling, clinical cohorts
- clinical study design, sample size, target trial emulation, registry, EHR, claims, OMOP, FHIR, CDISC, systematic review, meta-analysis, GWAS, PRS, or biobank genetics
- multi-omics integration

### Upstream Sequencing And Workflow Processing

Use:

- `platforms.md`
- `parameters.md`
- `upstream.md`
- `workflows.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- FASTQ-to-count, FASTQ-to-BAM, FASTQ-to-matrix, FASTQ-to-peak, FASTQ-to-ASV, FASTQ-to-VCF, FASTQ-to-protein, or raw data processing
- demultiplexing, sample-sheet review, lane merging, adapter trimming, alignment, quantification, UMI handling, MultiQC, or workflow deployment
- nf-core, Nextflow, Snakemake, Cell Ranger, Space Ranger, STARsolo, alevin-fry, kallisto-bustools, simpleaf, Velocyto, bcl-convert, bcl2fastq, FastQC, MultiQC, STAR, Salmon, kallisto, featureCounts, or tximport
- 10x Genomics, BD Rhapsody, MGI, BGI, DNBelab, Singleron, Parse, ScaleBio, Fluent, SMART-seq, split-pool, Visium, Visium HD, Xenium, CosMx, MERSCOPE, MERFISH, Stereo-seq, Slide-seq, DNBSEQ, Illumina, Nanopore, PacBio, Orbitrap, timsTOF, Q-TOF, triple quadrupole, MALDI, NMR, or documented vendor-specific platforms

### Variants, HLA, Antigen Peptides, And Immunopeptidomics

Use:

- `variants.md`
- `immunopeptidomics.md`
- `upstream.md` when raw WGS, WES, RNA-seq, or MS data are used
- `proteomics.md` when immunopeptidomics LC-MS/MS data are used
- `statistics.md`
- `tool-issues.md`

Triggers:

- germline variants, somatic variants, MAF, VCF, CNV, SV, fusion, MSI, TMB, mutational signatures, tumor purity, clonality, or variant annotation
- HLA typing, HLA loss, antigen peptide prediction, neoantigen, pVACtools, NetMHCpan, MHCflurry, MixMHCpred, BigMHC, PRIME, HLAthena, IEDB, immunopeptidomics, MhcVizPipe, or TCR-pMHC follow-up
- GATK, Mutect2, HaplotypeCaller, DeepVariant, Strelka2, Manta, Delly, CNVkit, FACETS, PureCN, Sequenza, ASCAT, GISTIC2, VEP, ANNOVAR, SnpEff, maftools, SigProfiler, OptiType, arcasHLA, HLA-HD, or Polysolver

### Advanced Single-Cell And Spatial Methods

Use:

- `platforms.md` when chemistry, sample handling, or platform-specific pipeline matters
- `parameters.md` when QC threshold, doublet rate, ambient correction, normalization, integration, dimensions, or clustering resolution matters
- `single-cell-advanced.md`
- `multiomics.md` for CITE-seq, multiome, cross-modal integration, and reference mapping
- `epigenomics.md` for scATAC, motif, footprinting, and regulatory interpretation
- `tool-issues.md`
- `workflows.md`

Triggers:

- single-cell QC, ambient RNA, doublets, normalization, integration, clustering, or annotation
- DropletUtils, miQC, scuttle, scater, scran, batchelor, FastMNN, BBKNN, Scanorama, STARsolo, kallisto-bustools, kb-python, alevin-fry, Cell Ranger ARC, or Space Ranger
- CITE-seq, ADT, dsb, CiteFuse, totalVI, MultiVI, muon, Multigrate, scGLUE, Cobolt, scJoint, scBridge, scMaui, scDART, UnionCom, scTriangulate, scConfluence, scDecorr, scDREAMER, or MEFISTO
- scType, scGate, UCell, AUCell, CellAssign, ProjecTILs, Symphony, popV, scPoli, treeArches, or CASSIA
- phenotype-associated cell methods such as Scissor, SCIPAC, scPAS, PACells, DEGAS, scSurv, or scSurvival
- foundation models, virtual cells, virtual knockout, or in silico perturbation
- Geneformer, scGPT, scFoundation, scTenifoldNet, scTenifoldKnk, CellOracle, PSGRN, RegDiffusion, Scribe, SINGE, or related tools
- drug prediction, drug repurposing, DrugReflector, scDrug, scDrug+, scDrugPrio, or drug2cell
- perturbation databases, Perturb-seq, CROP-seq, sci-Plex, ECCITE-seq, Perturb-ATAC, SHARE-seq, Mixscape, pertpy, GEARS, CPA, chemCPA, CellOT, scVIDR, scCODA, MASC, DA-seq, or MELD
- trajectory, time-course, and velocity tools such as CellRank, dynamo, velocyto, Palantir, Waddington-OT, FateID, destiny or DPT, CellRouter, TrendCatcher, condiments, and Lamian
- cell-cell and spatial communication tools such as COMMOT, SpaTalk, NATMI, SingleCellSignalR, iTALK, CellCall, MISTy, MEBOCOST, MultiNicheNet, NicheCompass, or Tensor-cell2cell
- advanced spatial algorithms, niches, adjacency, neighborhood enrichment, BANKSY, CellCharter, Milo, BayesSpace, SpaGCN, GraphST, PRECAST, STAGATE, DeepST, SEDR, SpaSEG, SpatialDE, SpatialDE2, SPARK, SPARK-X, SLOPER, scBSP, SMASH, SpaGene, SpatialPCA, Sopa, FICTURE, CartoScope, sosta, SpaceWalker, nnSVG, MERINGUE, DestVI, SPOTlight, STdeconvolve, SpatialDecon, STRIDE, SpaOTsc, novoSpaRc, CellTrek, or CytoSPACE
- single-cell and GWAS integration tools such as seismicGWAS, scDRS, CELLECT, MAGMA_Celltyping, RolyPoly, or LDSC-SEG
- emerging named tools such as scALPI that require name and source verification

### Clinical Research, Real-World Evidence, And Clinical Data Standards

Use:

- `clinical-research.md`
- `causal-inference.md` when observational comparisons, external controls, or target trial emulation are involved
- `clinical-data.md` when EHR, registry, claims, REDCap, OMOP, FHIR, CDISC, or terminology mapping is involved
- `parameters.md` when endpoint, time zero, sample-size assumptions, matching, weighting, trimming, or missing-data settings affect the result
- `statistics.md`
- `tool-issues.md`

Triggers:

- interventional, observational, diagnostic, prognostic, prediction, implementation, health-services, health-economic, translational, randomized, nonrandomized, cluster, crossover, stepped-wedge, factorial, adaptive, basket, umbrella, platform, registry, pragmatic, decentralized, device, surgical, behavioral, digital-health, or external-control study
- sample size, power, precision, interim analysis, operating characteristics, endpoint design, SAP, safety analysis, PRO, quality-of-life analysis, clinical prediction, diagnostic accuracy, or reporting checklist
- target trial emulation, clone-censor-weight, matching, weighting, TMLE, g-methods, instrumental variables, difference-in-differences, self-controlled designs, real-world evidence, or external controls
- REDCap, OMOP CDM, ATLAS, WhiteRabbit, Achilles, DataQualityDashboard, FHIR, CDISC SDTM, ADaM, CDASH, Define-XML, MedDRA, CTCAE, WHO Drug, ICD, SNOMED CT, LOINC, RxNorm, or ATC

### Evidence Synthesis And Genetic Epidemiology

Use:

- `evidence-synthesis.md`
- `genetic-epidemiology.md`
- `parameters.md`
- `statistics.md`
- `public-data.md`
- `tool-issues.md`

Triggers:

- systematic review, scoping review, meta-analysis, diagnostic meta-analysis, prognostic meta-analysis, network meta-analysis, umbrella review, pharmacovigilance, FAERS, VigiBase-style signal detection, or Mendelian randomization
- GWAS, PheWAS, PRS, fine mapping, colocalization, TWAS, eQTL, pQTL, mQTL, sQTL, LDSC, genetic correlation, heritability, ancestry, imputation, UK Biobank, FinnGen, OpenGWAS, dbGaP, GWAS Catalog, seismicGWAS, scDRS, CELLECT, MAGMA_Celltyping, RolyPoly, or LDSC-SEG

### Specialized RNA, Long-Read, And Liquid-Biopsy Assays

Use:

- `specialized-omics.md`
- `platforms.md`
- `parameters.md`
- `upstream.md` when raw sequencing or raw signal files are used
- `statistics.md`
- `tool-issues.md`

Triggers:

- small RNA, miRNA, piRNA, tRNA fragment, lncRNA, circRNA, alternative splicing, isoform, long-read transcriptomics, single-cell total RNA, TotalX, VASA-seq, Smart-seq-total, SUPeR-seq, CLIP-seq, RIP-seq, Ribo-seq, epitranscriptomics, RNA editing, cfDNA, ctDNA, CTC, exosome RNA, liquid biopsy, fragmentomics, or MRD analysis

### Bulk Functional Inference

Use:

- `bulk-inference.md`
- `statistics.md`
- `workflows.md`
- `tool-issues.md`

Triggers:

- transcription factor activity
- pathway or signaling activity
- kinase, proteomics, or phosphoproteomics activity
- decoupleR, DoRothEA, PROGENy, CollecTRI, OmniPath, VIPER, GSVA, ssGSEA, singscore, or WGCNA
- immune, stromal, or cell-type deconvolution
- CIBERSORTx, immunedeconv, xCell, MCP-counter, EPIC, quanTIseq, TIMER, MuSiC, BisqueRNA, BayesPrism, SCDC, DWLS, or ESTIMATE
- bulk-to-single-cell interpretation

### Epigenomics And Chromatin Regulation

Use:

- `epigenomics.md`
- `upstream.md` when raw data are used
- `multiomics.md` when linked to RNA, protein, variants, or spatial data
- `statistics.md`
- `tool-issues.md`

Triggers:

- ATAC-seq, scATAC-seq, CUT&Tag, CUT&Run, ChIP-seq, histone marks, TF binding, DNA methylation, bisulfite sequencing, Hi-C, HiChIP, PLAC-seq, Micro-C, promoter capture, chromatin interaction, motif, footprinting, co-accessibility, peak-to-gene links, or regulatory networks
- MACS2, MACS3, deepTools, HOMER, MEME, FIMO, TOBIAS, chromVAR, Cicero, SnapATAC2, JASPAR, TFBSTools, motifmatchr, Bismark, methylKit, DSS, bsseq, ChAMP, RnBeads, HiC-Pro, Juicer, cooler, HiCExplorer, FitHiC, or cooltools

### Proteomics, Metabolomics, And Metabolic Flux

Use:

- `proteomics.md`
- `metabolomics.md`
- `multiomics.md` when integrating with RNA, variants, microbiome, imaging, or clinical data
- `upstream.md` when raw MS or raw sequencing data are used
- `bulk-inference.md` for kinase, pathway, and regulator activity
- `statistics.md`
- `tool-issues.md`

Triggers:

- DDA, DIA, TMT, iTRAQ, LFQ, PRM, SRM, targeted proteomics, phosphoproteomics, PTM analysis, proteogenomics, peptide evidence, MaxQuant, FragPipe, MSFragger, DIA-NN, Spectronaut, OpenMS, Proteome Discoverer, Skyline, MSstats, MSstatsTMT, MSstatsPTM, DEP, PhosR, or QFeatures
- metabolomics, lipidomics, untargeted LC-MS, GC-MS, NMR, targeted metabolite panels, isotope tracing, metabolic flux analysis, fluxomics, FBA, scFEA, Compass, COBRApy, COBRA Toolbox, INCA, OpenFLUX2, XCMS, MZmine, MS-DIAL, GNPS, MetaboAnalystR, SIRIUS, HMDB, LIPID MAPS, IsoCor, or AccuCor

### Multi-Omics Integration

Use:

- `multiomics.md`
- the modality files selected by the actual data types
- `statistics.md`
- `tool-issues.md`

Triggers:

- paired or unpaired bulk multi-omics, single-cell multi-omics, CITE-seq, multiome, scNMT-seq, spatial multi-omics, imaging multi-omics, proteogenomics, metabolomics integration, host-microbe integration, feature concordance, factor analysis, subtype discovery, cross-modality label transfer, or missing-modality imputation
- MOFA2, MEFISTO, MultiAssayExperiment, mixOmics, DIABLO, SNFtool, iClusterPlus, Seurat WNN, totalVI, MultiVI, muon, scGLUE, Cobolt, MOJITOO, LIGER, scJoint, Multigrate, or scArches

### Metagenomics And Microbiome

Use:

- `metagenomics.md`
- `metabolomics.md` when microbial metabolite, flux, or pathway integration is involved
- `multiomics.md` when host omics, clinical, imaging, or metabolite data are linked
- `workflows.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- 16S rRNA, ITS, shotgun metagenomics, metatranscriptomics, virome, or long-read metagenomics
- microbiome diversity, composition, differential abundance, network, or ecological analysis
- Kraken2, Bracken, MetaPhlAn, HUMAnN, QIIME 2, DADA2, mothur, ANCOM-BC2, ALDEx2, MaAsLin2, LEfSe, phyloseq, vegan, microbiomeMarker, KneadData, decontam, StrainPhlAn, inStrain, PICRUSt2, AMRFinderPlus, ResFinder, VFDB, VirSorter2, VIBRANT, CheckV, or geNomad
- MAGs, microbial assembly, microbial annotation, GTDB-Tk, CheckM2, dRep, Prokka, Bakta, DRAM, CARD, dbCAN, or eggNOG
- host-microbe, tumor microbiome, therapy-response microbiome, or microbiome multi-omics integration

### Structural Bioinformatics And Drug Screening

Use:

- `structural.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- protein structure prediction, protein complex prediction, antibody-antigen structure, protein-DNA, protein-RNA, protein-ligand, or ligand-binding pocket analysis
- molecular docking, molecular dynamics, free-energy estimation, virtual screening, ADMET, QSAR, ligand preparation, or chemoinformatics
- AlphaFold, ColabFold, AlphaFold 3, Chai-1, Boltz, AutoDock Vina, GNINA, DiffDock, GROMACS, OpenMM, AMBER, RDKit, or DeepChem

### Imaging And Virtual Spatial Omics

Use:

- `imaging.md`
- `statistics.md`
- `workflows.md`
- `methods.md`
- `tools.md`
- `tool-issues.md`

Triggers:

- pathology imaging, radiomics, pathomics, WSI, H&E, IHC, IF, mIF, MxIF, CODEX, MIBI, IMC, CyCIF, or CyTOF-linked tissue analysis
- automatic segmentation, automatic contouring, radiotherapy structure generation, nnU-Net, MONAI, TotalSegmentator, MedSAM, Cellpose, StarDist, QuPath, Hover-Net, Mesmer, or ilastik
- multiplex imaging analysis tools such as phenoptr, phenoptrReports, rtree, inForm, histoCAT, imcRtools, MCMICRO, ASHLAR, or steinbock
- virtual multiplex immunofluorescence, virtual staining, H&E-to-marker prediction, label-free-to-stain prediction, or sequential IHC virtual multiplexing
- virtual spatial transcriptomics, histology-to-gene-expression prediction, spatial expression imputation, ST-Net, Hist2ST, HisToGene, THItoGene, iStar, BLEEP, STimage, or FineST

### Didactic Or Target-Driven Sensitivity Work

Use:

- `sensitivity.md`
- `statistics.md`
- `data-assessment.md`

Triggers:

- teaching data
- self-test data
- requested target signal is weak or absent
- threshold or grouping choices may be tuned for demonstration

## Tool Issue Layer

Use `tool-issues.md` whenever any of these are true:

- the tool changed object format recently
- the tool depends on web login, model checkpoints, Docker, or a remote service
- the task uses a new, preprint, code-only, or lightly benchmarked method
- the same error appears in GitHub issues, Bioconductor Support, Biostars, CSDN, or package forums
- a workaround changes the data object, assay layer, normalization, or scientific output

Record checked issues and selected workarounds in the project output.

## Execution Layer

Use `execution.md` for every executable analysis.

It controls:

- sub-agent assignment and integration
- goal tracking when explicitly requested or already active
- default tool deployment and installation records
- figure inspection and figure regeneration
- per-figure interpretation
- phase reports and state recovery files

## Learning Layer

Use `learning.md` for every analysis and consultation.

It controls:

- beginner, intermediate, and experienced user assessment
- direct correction of incorrect assumptions
- proactive tool, data type, public dataset, and validation suggestions
- provisional user preference records
- recurring bug and error records
- new tool version, new workflow, and new literature update records

## Output Artifacts

Each real analysis should produce the relevant subset:

- `分析状态.md`
- main analysis script
- key intermediate RDS, CSV, TSV, or AnnData files
- final tables
- complete figure set
- `图表清单.md`
- `图表解读.md`
- `方法学说明.md`
- `工具部署记录.md`
- `参考文献与依据.md`
- `工具问题记录.md` when applicable
- `阶段报告.md` with result analysis, interpretation, methods, references, and limitations
- `限制说明.md` for blocked or exploratory branches

## Learning Artifacts

Maintain these skill-level records:

- `user-profile.md`
- `bug-log.md`
- `method-updates.md`

## Maintenance Rule

When adding a new reference file, update this map and `SKILL.md`.

When adding a new tool family, place method workflow in the most specific reference file and add only a trigger here. Avoid duplicating detailed workflows in multiple files.
