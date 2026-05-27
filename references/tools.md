# Tools

## Contents

1. How to use this file
2. Core selection rule
3. Platform and parameter-sensitive tools
4. Upstream workflow tools
5. Bulk and cohort tools
6. Single-cell tools
7. Spatial and deconvolution tools
8. Immune-repertoire and antigen tools
9. Variant and epigenomics tools
10. Multi-omics tools
11. Proteomics, metabolomics, and flux tools
12. Metagenomics and microbiome tools
13. Clinical research and causal tools
14. Evidence synthesis and genetic epidemiology tools
15. Specialized RNA and liquid-biopsy tools
16. Structural and chemoinformatics tools
17. Imaging and segmentation tools
18. Statistics and visualization tools
19. Selection checklist

## How To Use This File

Use this file when the request asks for:

- a package comparison
- dominant tool families over the last decade or two decades
- strengths and weaknesses of competing methods
- which route should be chosen for a dataset

This file is a family map, not a package encyclopedia. Use it to narrow to a route, then read official package documentation before implementation.

Before implementation, use `index.md` to load the companion files that match the route. Those files define current workflows, advanced methods, bulk inference, figure requirements, and tool issue review.

## Core Selection Rule

Choose the route that satisfies all four conditions:

1. it answers the biological question directly
2. it fits the actual data structure
3. it stays close to the established project code style when scientific fit is comparable
4. it avoids unnecessary environment complexity

Do not switch to a newer package only because it is newer. Switch only when the biological fit, statistical fit, or scale requirement is materially better.

## Platform And Parameter-Sensitive Tools

- vendor pipelines and run reports
  - Best for: preserving chemistry, barcode, UMI, reference, sequencing, MS acquisition, and imaging acquisition assumptions before downstream analysis
  - Examples: Cell Ranger, Cell Ranger ARC, Cell Ranger ATAC, Space Ranger, Xenium Ranger, BD Rhapsody Sequence Analysis Pipeline, ScaleBio Seq Suite, Parse Split Pipe or Trailmaker, Fluent PIPseeker, vendor spatial and imaging software
  - Weaknesses: vendor defaults are not automatically optimal for every biological question
- `MultiQC`, `pmultiqc`, vendor QC summaries, and assay-specific QC dashboards
  - Best for: checking raw run quality and platform-specific failure modes
  - Weaknesses: downstream biological interpretation still requires modality-specific analysis
- sensitivity and parameter-review scripts
  - Best for: checking QC thresholds, integration strength, clustering resolution, peak-calling settings, MS search settings, metabolite peak parameters, matching or weighting choices, PRS LD references, and imaging preprocessing
  - Weaknesses: broad sweeps can add noise; use focused ranges tied to the conclusion

Read `platforms.md` and `parameters.md` before committing to a platform-sensitive or parameter-sensitive route.

## Upstream Workflow Tools

- `nf-core`
  - Best for: standardized Nextflow workflows, containers, MultiQC, and versioned outputs across RNA-seq, scRNA-seq, ATAC, ChIP, methylation, WGS, WES, microbiome, and proteomics
  - Weaknesses: workflow output still needs task-specific downstream interpretation
- `Cell Ranger`, `Cell Ranger ARC`, `Space Ranger`, `Xenium Ranger`
  - Best for: 10x Genomics single-cell, multiome, spatial, and in situ platforms
  - Weaknesses: chemistry, reference, version, and license constraints must be recorded
- `STARsolo`, `alevin-fry`, `simpleaf`, `kallisto-bustools`, `kb-python`
  - Best for: single-cell FASTQ-to-matrix alternatives when reproducibility, speed, or spliced and unspliced output matters
  - Weaknesses: gene-count conventions can differ from Cell Ranger
- `FastQC`, `MultiQC`, `Picard`, `samtools`, `bcftools`, `UMI-tools`
  - Best for: raw QC, alignment QC, file handling, UMI review, and reproducible preprocessing summaries
  - Weaknesses: need assay-specific interpretation

## Bulk And Cohort Tools

### Raw RNA-seq preprocessing

- `nf-core/rnaseq`
  - Best for: FASTQ-to-count RNA-seq workflows with standardized QC, quantification, MultiQC, and versioned outputs
  - Weaknesses: downstream statistical design and biological interpretation still need separate analysis

### Differential expression

- `limma` / `limma-voom`
  - Best for: microarray, normalized expression, complex designs, transformed RNA-seq
  - Strengths: mature, flexible design matrices, very strong publication history
  - Weaknesses: raw-count workflows usually fit better in count-based models
- `edgeR`
  - Best for: count matrices with modest sample sizes or strong library-size differences
  - Strengths: reliable dispersion modeling, transparent count-based assumptions
  - Weaknesses: less preferred when users strongly expect DESeq2-style output objects
- `DESeq2`
  - Best for: publication-standard count workflows with clean group definitions
  - Strengths: widely recognized, shrinkage options, straightforward reporting
  - Weaknesses: slower on very large matrices, not automatically the best choice for every complex design

### Survival and clinical modeling

- `survival` + `survminer`
  - Best for: Kaplan-Meier, Cox, clean clinical reporting
  - Strengths: canonical and interpretable
  - Weaknesses: feature selection and high-dimensional modeling need extra tools
- `rms`
  - Best for: nomograms, calibration, richer regression diagnostics
  - Strengths: strong clinical-modeling toolkit
  - Weaknesses: heavier modeling overhead than simple KM/Cox workflows
- `glmnet`
  - Best for: penalized signatures and high-dimensional feature reduction
  - Strengths: robust regularization
  - Weaknesses: signatures can become unstable without disciplined resampling and validation
- `timeROC`, `survivalROC`
  - Best for: time-dependent ROC reporting
  - Weaknesses: should support, not replace, core survival reasoning
- `MatchIt`
  - Best for: confounding reduction in observational cohorts
  - Weaknesses: matching cannot rescue missing biology or poor endpoint definition

### Clinical trial planning and cohort design

- `rpact`, `gsDesign`, `gsDesign2`
  - Best for: group sequential, adaptive, fixed-sample, binary, continuous, and survival trial design
  - Weaknesses: assumptions and operating characteristics must be explicit
- `clinfun`, `ph2simon`, `OneArmPhaseTwoStudy`, `BOIN`, `dfcrm`, `bcrm`
  - Best for: single-arm phase II, two-stage, Bayesian, and dose-finding designs
  - Weaknesses: historical benchmark and endpoint quality dominate interpretation
- `pmsampsize`, `powerSurvEpi`, `simtrial`, `simr`, `clusterPower`, `CRTsize`, `steppedwedge`, `longpower`
  - Best for: prediction-model, survival, simulation, mixed-model, cluster, stepped-wedge, and longitudinal sample-size planning
  - Weaknesses: formula outputs are only as defensible as the design assumptions

### Bulk deconvolution and microenvironment

- `CIBERSORTx`
  - Best for: reference-based cellular composition estimates from bulk data
  - Strengths: widely cited and familiar to biomedical readers
  - Weaknesses: depends heavily on reference quality and signature transferability
- `EPIC`, `MCP-counter`, `xCell`, `quanTIseq`
  - Best for: quick immune or stromal context
  - Strengths: fast, useful for cohort-wide trends
  - Weaknesses: cell-resolution claims should stay modest
- `MuSiC`, `BisqueRNA`
  - Best for: single-cell-informed deconvolution
  - Strengths: better when matching single-cell reference exists
  - Weaknesses: strong dependence on reference compatibility

### Microarray preprocessing

- `GEOquery`, `affy`, `oligo`, `limma`, `arrayQualityMetrics`, `lumi`, `beadarray`
  - Best for: GEO retrieval, Affymetrix and Illumina array preprocessing, QC, normalization, and platform annotation
  - Weaknesses: probe annotation and platform version can dominate results

## Single-Cell Tools

### Object handling and integration

- `Seurat`
  - Best for: end-to-end R workflows, broad plotting, metadata-centric analysis
  - Strengths: consistent with the established R-first workflow, easy handoff to downstream modules
  - Weaknesses: some advanced scaling or probabilistic integration tasks are better elsewhere
- `Harmony`
  - Best for: metadata-aware batch correction inside Seurat workflows
  - Strengths: practical, familiar, low-friction in R
  - Weaknesses: not a universal answer for every cross-cohort integration problem
- `RPCA` / Seurat anchors
  - Best for: moderate integration tasks where Seurat-native mapping is enough
  - Weaknesses: can over- or under-correct depending on cohort structure
- `LIGER`
  - Best for: factor-based integration across modalities or batches
  - Weaknesses: less aligned to the user's current dominant code style
- `scVI` / `scANVI`
  - Best for: difficult batch structure, large heterogeneous cohorts, probabilistic latent modeling
  - Strengths: strong integration performance
  - Weaknesses: heavier Python dependence and extra environment complexity
- `Scanpy`
  - Best for: AnnData-first workflows, large-scale Python analysis, and interoperability with scVelo, Squidpy, and scirpy
  - Weaknesses: less aligned with the user's R-first plotting style
- `SingleCellExperiment`
  - Best for: Bioconductor-native workflows and sample-aware statistical analysis
  - Weaknesses: less direct handoff to Seurat-specific plotting scripts
- `DropletUtils`, `scuttle`, `scater`, `scran`, `miQC`
  - Best for: droplet detection, core QC, normalization, and Bioconductor-style preprocessing
  - Weaknesses: requires careful object conversion when final workflow is Seurat-based
- `batchelor`, `FastMNN`, `BBKNN`, `Scanorama`
  - Best for: alternative batch handling or Python/Scanpy ecosystems
  - Weaknesses: overcorrection and object handoff need explicit checks
- `ROGUE`, `LISI`, `scIB`, `kBET`, `ASW`, `clustree`
  - Best for: cluster purity, integration quality, batch mixing, biology preservation, and resolution assessment
  - Weaknesses: metrics must be interpreted with marker evidence and sample structure

### Annotation

- Manual marker annotation
  - Best for: oncology projects needing interpretable subtypes and custom state naming
  - Strengths: strongest alignment with the user's style and manuscript defense
  - Weaknesses: slower and dependent on domain knowledge
- `SingleR`
  - Best for: first-pass reference transfer in R
  - Strengths: lightweight and easy to add
  - Weaknesses: final labels still need marker verification
- `CellTypist`
  - Best for: large immune-rich datasets needing rapid draft labels
  - Strengths: fast and practical
  - Weaknesses: draft labels can drift from disease-specific states
- `Azimuth`
  - Best for: reference mapping onto strong Seurat references
  - Weaknesses: less suitable when tumor-specific states dominate
- `scType`, `scGate`, `UCell`, `AUCell`, `CellAssign`, `ProjecTILs`, `Symphony`, `popV`, `scPoli`, `treeArches`
  - Best for: marker-set scoring, gate-based annotation, reference transfer, immune-state annotation, and atlas mapping
  - Weaknesses: automated labels must be checked with marker panels and disease context

### Differential state and marker analysis

- `FindMarkers` / `FindAllMarkers`
  - Best for: pragmatic cluster marker discovery inside Seurat
  - Strengths: direct and familiar
  - Weaknesses: pseudo-replication risk if biological replicate structure matters
- pseudo-bulk with `edgeR`, `DESeq2`, or `limma`
  - Best for: sample-aware differential testing across patient groups
  - Strengths: statistically cleaner for patient-level inference
  - Weaknesses: requires careful aggregation and replicate definition
- `muscat`
  - Best for: multi-sample differential state testing
  - Strengths: explicit design for replicate-aware single-cell comparisons
  - Weaknesses: higher setup cost than quick Seurat marker calls

### Trajectory and state transitions

- `Monocle2`
  - Historical role: classic pseudotime in older papers
  - Weaknesses: older design and fewer advantages for new projects
- `Monocle3`
  - Best for: trajectory graphing with modern workflows
  - Strengths: familiar in many single-cell papers
  - Weaknesses: lineage statistics may still need companion tools
- `slingshot` + `tradeSeq`
  - Best for: lineage-aware pseudotime with formal expression testing
  - Strengths: strong for state-transition questions and gene-trend statistics
  - Weaknesses: setup is less plug-and-play than one-click pseudotime plotting
- `PAGA`
  - Best for: topology-first trajectory reasoning in Scanpy ecosystems
  - Weaknesses: less natural in an R-first project
- `scVelo`
  - Best for: velocity-specific questions with spliced and unspliced data
  - Weaknesses: not appropriate unless velocity assumptions and inputs are satisfied
- `CytoTRACE` / `CytoTRACE2`
  - Best for: differentiation potential rather than explicit branch structure
- `condiments`, `Lamian`
  - Best for: formal comparison of trajectories across conditions or samples
  - Weaknesses: require careful design and sufficient replicate structure
- `DeepVelo`, `TFvelo`
  - Best for: specialized velocity models when their assumptions fit
  - Weaknesses: heavier model assumptions and higher environment cost
- `CellRank`, `dynamo`, `velocyto`, `Palantir`, `Waddington-OT`, `FateID`, `destiny`, `CellRouter`
  - Best for: fate probabilities, vector fields, diffusion pseudotime, transport-based trajectories, or older lineage workflows
  - Weaknesses: require suitable inputs and strong biological anchoring

### Cell-cell communication

- `CellChat`
  - Best for: pathway-level network visualization in R
  - Strengths: already present in the user's style
  - Weaknesses: communication plots should not be overinterpreted as direct mechanistic proof
- `CellPhoneDB`
  - Best for: canonical ligand-receptor interaction testing
  - Strengths: widely known
  - Weaknesses: Python workflow and less aligned with the established R-first style
- `NicheNet`
  - Best for: ligand-to-target prioritization
  - Strengths: stronger when downstream target programs matter
  - Weaknesses: requires more careful biological framing
- `LIANA`
  - Best for: consensus-style ligand-receptor scoring across methods
  - Strengths: broader method harmonization
  - Weaknesses: higher complexity than many projects need
- `COMMOT`, `SpaTalk`, `NATMI`, `SingleCellSignalR`, `iTALK`, `CellCall`, `MISTy`, `MEBOCOST`, `MultiNicheNet`, `NicheCompass`, `Tensor-cell2cell`
  - Best for: spatial communication, condition-aware communication programs, metabolic communication, microenvironment modeling, and multi-sample communication patterns
  - Weaknesses: database choice, spatial assumptions, and sample structure strongly affect conclusions

### CNV and malignancy inference

- `infercnv`
  - Best for: transcriptome-based CNV estimation with reasonable normal references
  - Strengths: highly familiar in cancer single-cell papers
  - Weaknesses: sensitive to reference choice and parameter settings
- `CopyKAT`
  - Best for: tumor-versus-normal separation with inferable aneuploidy
  - Strengths: practical for malignancy calling
  - Weaknesses: not all tumors or datasets fit its assumptions equally well
- `HoneyBADGER`, `CONICSmat`
  - Best for: niche scenarios needing alternative CNV logic
  - Weaknesses: less standard for a shortest-path workflow

## Spatial And Deconvolution Tools

### Spatial preprocessing and exploration

- `Seurat` / `STutility`
  - Best for: R-first spatial handling close to existing Seurat workflows
- `Giotto`
  - Best for: richer spatial network and visualization workflows
  - Weaknesses: larger conceptual overhead
- `squidpy`
  - Best for: Scanpy/Python spatial ecosystems
  - Weaknesses: added Python complexity in an R-first environment
- `SpatialExperiment`
  - Best for: Bioconductor-native spatial object management
  - Weaknesses: usually needs companion tools for rich spatial statistics and plotting

### Spatial statistics and deconvolution

- `SPARK-X`
  - Best for: spatially variable gene testing
- `BayesSpace`
  - Best for: spot-level clustering refinement
- `RCTD`, `cell2location`, `CARD`
  - Best for: cell-type deconvolution into spots
  - Strengths: useful when paired single-cell references exist
  - Weaknesses: conclusions are only as good as reference quality and platform compatibility
- `SpatialDWLS`
  - Best for: Giotto-linked deconvolution workflows
  - Weaknesses: depends on signature quality
- `Squidpy`
  - Best for: Python spatial neighborhood, co-occurrence, image, and ligand-receptor workflows
  - Weaknesses: added Python complexity in an R-first environment
- `DestVI`, `SPOTlight`, `STdeconvolve`, `SpatialDecon`, `STRIDE`, `NMFreg`, `SpaOTsc`, `novoSpaRc`, `CellTrek`, `CytoSPACE`
  - Best for: spatial deconvolution, single-cell-to-space mapping, and spatial reconstruction when the platform and reference fit
  - Weaknesses: inferred mappings require reference compatibility and spatial validation
- `STAGATE`, `DeepST`, `SEDR`, `SpaSEG`, `SpatialDE`, `nnSVG`, `trendsceek`, `MERINGUE`, `Splotch`, `SpotClean`
  - Best for: spatial domain detection, spatially variable genes, spatial graph representation, or spot-level denoising
  - Weaknesses: platform resolution and tissue structure determine method fit

## Immune-Repertoire And Antigen Tools

- `scRepertoire`
  - Best for: Seurat-linked clonotype integration in R
  - Strengths: direct metadata integration
- `Startrac`
  - Best for: expansion, transition, and distribution logic in immune-state studies
  - Strengths: strong when tissue ecology matters
- `immunarch`
  - Best for: bulk or repertoire-centric summaries
- `scirpy`
  - Best for: Python/Scanpy ecosystems
- `Dandelion`
  - Best for: richer single-cell BCR/TCR network and receptor-lineage workflows
  - Weaknesses: extra Python or mixed ecosystem complexity
- `OptiType`, `arcasHLA`, `HLA-HD`, `Polysolver`, `HLAminer`, `Kourami`
  - Best for: HLA typing from WES, WGS, RNA-seq, or targeted HLA inputs
  - Weaknesses: class support, resolution, and input requirements differ
- `pVACtools`, `NetMHCpan`, `MHCflurry`, `MixMHCpred`, `BigMHC`, `PRIME`, `HLAthena`
  - Best for: neoantigen, MHC binding, presentation, and immunogenicity prioritization
  - Weaknesses: predictions need expression, clonality, HLA, normal-tissue, and peptide evidence checks
- `MhcVizPipe`, `GibbsCluster`, `MoDec`
  - Best for: immunopeptidomics QC, motif clustering, and MHC specificity review
  - Weaknesses: search settings and peptide evidence quality dominate outputs

## Variant And Epigenomics Tools

- `GATK`, `DeepVariant`, `Strelka2`, `FreeBayes`, `bcftools`, `Mutect2`
  - Best for: germline and somatic SNV or indel discovery
  - Weaknesses: tumor-normal status, filtering, and reference resources control reliability
- `CNVkit`, `FACETS`, `PureCN`, `Sequenza`, `ASCAT`, `Control-FREEC`, `ichorCNA`
  - Best for: copy number, purity, ploidy, and allele-specific copy number
  - Weaknesses: assay size, normal reference, and tumor purity limit resolution
- `Manta`, `Delly`, `SvABA`, `GRIDSS`, `Sniffles2`, `cuteSV`
  - Best for: short-read and long-read structural variants
  - Weaknesses: breakpoint validation and visualization are required for high-value claims
- `VEP`, `ANNOVAR`, `SnpEff`, `maftools`, `SigProfiler`, `MutationalPatterns`
  - Best for: variant annotation, cancer summaries, and mutational signatures
  - Weaknesses: database versions and transcript choices affect interpretation
- `MACS2`, `MACS3`, `SEACR`, `SICER`, `Genrich`
  - Best for: peak calling across ATAC, ChIP, CUT&Tag, and CUT&Run contexts
  - Weaknesses: mark type and control choice matter
- `deepTools`, `HOMER`, `MEME`, `FIMO`, `TOBIAS`, `chromVAR`, `Cicero`, `SnapATAC2`
  - Best for: signal metaplots, heatmaps, motif discovery, footprinting, motif activity, and co-accessibility
  - Weaknesses: motif and footprint results need matched accessibility and expression checks
- `Bismark`, `methylKit`, `DSS`, `bsseq`, `minfi`, `sesame`, `ChAMP`, `RnBeads`
  - Best for: methylation sequencing and array processing
  - Weaknesses: platform annotation, probe filtering, and coverage shape the result
- `HiC-Pro`, `Juicer`, `cooler`, `HiCExplorer`, `FitHiC`, `cooltools`
  - Best for: Hi-C, Micro-C, contact maps, compartments, loops, and interaction analysis
  - Weaknesses: resolution, depth, and normalization limit claims

## Multi-Omics Tools

- `Signac`
  - Best for: scATAC or multimodal workflows inside Seurat
  - Strengths: minimal friction for Seurat users
- `ArchR`
  - Best for: large-scale scATAC projects with richer ATAC tooling
  - Weaknesses: larger framework shift
- `nf-core/atacseq` and ENCODE ATAC pipeline
  - Best for: raw bulk ATAC-seq preprocessing, QC, consensus peaks, and differential accessibility-ready outputs
  - Weaknesses: pipeline outputs still need biological interpretation in R or Python
- `nf-core/chipseq` and ENCODE ChIP-seq pipelines
  - Best for: raw ChIP-seq, CUT&Tag, or CUT&Run preprocessing, QC, peak calling, and normalized tracks
  - Weaknesses: broad marks, narrow marks, and CUT&Tag protocols need different settings
- `nf-core/cutandrun`
  - Best for: CUT&RUN and CUT&Tag protocol-aware preprocessing, QC, and peak outputs
- `DiffBind`, `csaw`, `ChIPseeker`
  - Best for: differential binding, window-based signal testing, peak annotation, enrichment, metaplots, and heatmaps
- `minfi`, `sesame`, `DMRcate`, `missMethyl`
  - Best for: methylation array QC, normalization, DMPs, DMRs, and methylation-aware enrichment
- `MOFA2`
  - Best for: latent-factor integration across multiple omics
- `mixOmics`
  - Best for: supervised or integrative feature relationships
- `iClusterPlus`
  - Best for: classical cancer multi-omics subtype integration
- Seurat `WNN`
  - Best for: multimodal single-cell integration when Seurat is already the backbone
- `MultiAssayExperiment`
  - Best for: organizing partially matched multi-assay cohorts
- `totalVI`, `MultiVI`, `muon`, `Multigrate`
  - Best for: CITE-seq, multiome, paired and unpaired modality integration, and scverse workflows
  - Weaknesses: GPU and Python environment can be limiting
- `scGLUE`, `Cobolt`, `MOJITOO`, `scJoint`, `scBridge`, `scMaui`, `scDART`, `UnionCom`
  - Best for: single-cell multi-omics, unpaired alignment, regulatory inference, and modality bridging
  - Weaknesses: assumptions and maintenance status require current verification
- `SNFtool`, `NEMO`, `MEFISTO`
  - Best for: bulk subtype integration, network fusion, and spatial or temporal factor models
  - Weaknesses: sample size and missingness shape factor stability

## Proteomics, Metabolomics, And Flux Tools

- `MaxQuant`, `FragPipe`, `MSFragger`, `DIA-NN`, `Spectronaut`, `OpenMS`, `Proteome Discoverer`, `MetaMorpheus`, `PEAKS`
  - Best for: DDA, DIA, LFQ, TMT, iTRAQ, and raw proteomics processing
  - Weaknesses: raw format, search database, FDR, missingness, and peptide grouping require explicit review
- `MSstats`, `MSstatsTMT`, `MSstatsPTM`, `DEP`, `proDA`, `Perseus`, `QFeatures`, `MSnbase`
  - Best for: differential protein, TMT, PTM, and peptide-level statistical analysis
  - Weaknesses: missingness and protein-group ambiguity can dominate results
- `PTM-SEA`, `KSEA`, `PhosR`, `KinasePA`, `decoupleR`
  - Best for: phosphoproteomics, PTM enrichment, and kinase activity
  - Weaknesses: substrate databases and site localization must be checked
- `XCMS`, `MZmine`, `MS-DIAL`, `MetaboAnalystR`, `GNPS`, `SIRIUS`, `MS-FINDER`, `CAMERA`
  - Best for: LC-MS or GC-MS feature detection, alignment, annotation, molecular networking, and statistics
  - Weaknesses: annotation confidence and batch QC must be explicit
- `LipidSearch`, `LipidHunter`, `LipidMatch`, `LIPID MAPS`
  - Best for: lipidomics annotation and lipid-class analysis
  - Weaknesses: adducts and isomers require cautious interpretation
- `IsoCor`, `AccuCor`, `INCA`, `OpenFLUX2`, `13CFLUX2`, `COBRApy`, `COBRA Toolbox`, `cameo`, `scFEA`, `Compass`
  - Best for: isotope correction, 13C flux, FBA, single-cell metabolic inference, and constraint-based modeling
  - Weaknesses: flux claims need labeling design, model fit, and confidence intervals

## Metagenomics And Microbiome Tools

- `QIIME 2`
  - Best for: marker-gene microbiome workflows, metadata-aware visualizations, and documented analysis artifacts
  - Weaknesses: plugin versions and artifact formats need careful recording
- `DADA2`
  - Best for: ASV inference in R or QIIME 2-linked workflows
  - Weaknesses: truncation and quality choices strongly affect retained reads
- `Kraken2` plus `Bracken`
  - Best for: fast shotgun read classification and abundance estimation
  - Weaknesses: database composition can dominate results
- `MetaPhlAn`
  - Best for: marker-gene shotgun profiling and cross-study species-level comparability
  - Weaknesses: may miss organisms outside marker coverage
- `HUMAnN`
  - Best for: gene-family and pathway functional profiling from shotgun data
  - Weaknesses: pathway coverage depends on database and taxonomic profiling
- `ANCOM-BC2`, `ALDEx2`, `MaAsLin2`, `LinDA`
  - Best for: differential abundance and metadata association in compositional microbiome data
  - Weaknesses: methods answer related but distinct statistical questions
- `MEGAHIT`, `metaSPAdes`, `metaFlye`
  - Best for: metagenome assembly
  - Weaknesses: assembly quality depends heavily on depth, complexity, and contamination
- `MetaBAT2`, `MaxBin2`, `CONCOCT`, `DAS Tool`, `CheckM2`, `GTDB-Tk`, `dRep`
  - Best for: MAG binning, refinement, quality assessment, taxonomy, and dereplication
  - Weaknesses: MAG claims need quality thresholds and abundance support
- `KneadData`, `decontam`
  - Best for: host removal, contaminant detection, and low-biomass review
  - Weaknesses: metadata and negative controls are essential
- `StrainPhlAn`, `inStrain`
  - Best for: strain-level profiling and population variation
  - Weaknesses: depth and mapping ambiguity limit confidence
- `VirSorter2`, `VIBRANT`, `CheckV`, `geNomad`
  - Best for: viral metagenomics and viral contig quality review
  - Weaknesses: viral annotation remains database-sensitive
- `PICRUSt2`, `AMRFinderPlus`, `ResFinder`, `VFDB`
  - Best for: function prediction, resistome, and virulence review
  - Weaknesses: marker-gene inferred function is weaker than shotgun functional profiling

## Clinical Research And Causal Tools

- `TrialEmulation`
  - Best for: target trial emulation of observational time-to-event data
  - Weaknesses: requires explicit target trial elements and time-zero alignment
- `MatchIt`, `WeightIt`, `cobalt`, `optmatch`, `CBPS`, `twang`, `PSweight`
  - Best for: matching, weighting, balance diagnostics, and propensity-score workflows
  - Weaknesses: cannot resolve missing design variables or unmeasured factors
- `ipw`, `tmle`, `ltmle`, `drtmle`, `SuperLearner`, `grf`, `DoubleML`, `AIPW`
  - Best for: weighting, doubly robust estimation, TMLE, causal forests, and causal machine learning
  - Weaknesses: target estimand, positivity, and tuning must be checked
- `dagitty`, `EValue`, `episensr`, `tipr`
  - Best for: DAG review and quantitative sensitivity analysis
- `did`, `fixest`, `CausalImpact`, `gsynth`, `Synth`, `rdd`, `ivreg`, `AER`, `SelfControlledCaseSeries`
  - Best for: difference-in-differences, interrupted time series, synthetic controls, regression discontinuity, instrumental variables, and self-controlled designs
- `REDCapR`, `redcapAPI`, `SqlRender`, `DatabaseConnector`, `Achilles`, `DataQualityDashboard`, `CohortDiagnostics`, `FeatureExtraction`, `admiral`, `metacore`, `xportr`, `fhircrackr`
  - Best for: REDCap, OMOP, OHDSI, CDISC, FHIR, and clinical data quality workflows

## Evidence Synthesis And Genetic Epidemiology Tools

- `revtools`, `litsearchr`, `RISmed`, `rentrez`, `ASReview`
  - Best for: literature search, screening support, and review preparation
- `metafor`, `meta`, `netmeta`, `gemtc`, `BUGSnet`, `bayesmeta`, `dmetar`, `robvis`, `mada`, `diagmeta`
  - Best for: pairwise meta-analysis, network meta-analysis, Bayesian meta-analysis, risk-of-bias visualization, diagnostic meta-analysis, and prognostic evidence synthesis
  - Weaknesses: heterogeneity, publication bias, and endpoint differences must be explicit
- `TwoSampleMR`, `MendelianRandomization`, `MR-PRESSO`, `RadialMR`, `coloc`, `susieR`
  - Best for: Mendelian randomization, pleiotropy checks, colocalization, and fine-mapping support
- `PLINK2`, `SAIGE`, `REGENIE`, `BOLT-LMM`, `GEMMA`, `GCTA`, `Hail`, `SNPTEST`
  - Best for: GWAS, rare variant, mixed-model, and large biobank analysis
- `PRSice`, `LDpred2`, `lassosum2`, `PRS-CS`, `SBayesR`
  - Best for: PRS construction and validation
- `FINEMAP`, `SuSiE`, `PolyFun`, `PAINTOR`, `CAVIAR`, `eCAVIAR`, `HyPrColoc`, `SMR`, `FUSION`, `S-PrediXcan`, `MAGMA`, `Pascal`
  - Best for: fine mapping, colocalization, TWAS, gene-level tests, and pathway analysis

## Specialized RNA And Liquid-Biopsy Tools

- `nf-core/smrnaseq`, `miRDeep2`, `sRNAbench`, `miRge`, `miRTrace`, `ShortStack`
  - Best for: small RNA, miRNA, isomiR, piRNA, and related short RNA workflows
- `rMATS`, `MAJIQ`, `SUPPA2`, `DEXSeq`, `JunctionSeq`, `LeafCutter`, `MISO`, `SplAdder`
  - Best for: event-level, transcript-level, and junction-level alternative splicing
- `FLAIR`, `TALON`, `IsoQuant`, `Bambu`, `StringTie2`, `FLAMES`, `TAMA`, `Mandalorion`
  - Best for: long-read transcriptomics and isoform analysis
- `CIRI2`, `CIRCexplorer2`, `find_circ`, `DCC`, `circRNAprofiler`
  - Best for: circRNA discovery and back-splice junction review
- `nf-core/clipseq`, `CLIPper`, `PureCLIP`, `iCount`, `PARalyzer`, `Piranha`, `CTK`, `PEAKachu`
  - Best for: CLIP, RIP, RNA-binding protein targets, motif, and peak analysis
- `nf-core/riboseq`, `RiboTaper`, `RiboCode`, `riboWaltz`, `RiboProfiling`, `ORFquant`, `Ribo-seQC`
  - Best for: Ribo-seq, translation efficiency, ORF discovery, and frame periodicity
- `exomePeak2`, `MeTPeak`, `RADAR`, `Nanopolish`, `Tombo`, `m6Anet`, `EpiNano`, `REDItools`, `SPRINT`, `JACUSA2`
  - Best for: epitranscriptomics, RNA modification, direct RNA evidence, and RNA editing
  - Weaknesses: DNA variant filtering and protocol controls are central

## Structural And Chemoinformatics Tools

- `AlphaFold`, `ColabFold`, `AlphaFold-Multimer`
  - Best for: protein or protein-complex structure prediction when sequence evidence and confidence metrics are suitable
  - Weaknesses: low-confidence regions, conformational states, ligands, and disorder need caution
- `AlphaFold 3`, `Chai-1`, `Boltz`
  - Best for: broader biomolecular interaction prediction, including complexes and selected ligand or nucleic-acid contexts
  - Weaknesses: access, license, molecule support, and benchmark status must be checked for each task
- `AutoDock Vina`, `Smina`, `rDock`
  - Best for: classical molecular docking and virtual screening
  - Weaknesses: score ranking alone is insufficient
- `GNINA`, `DiffDock`
  - Best for: deep-learning-assisted docking or pose prediction
  - Weaknesses: model domain and validation controls matter
- `GROMACS`, `OpenMM`, `AMBER`, `NAMD`
  - Best for: molecular dynamics and simulation diagnostics
  - Weaknesses: setup choices can dominate conclusions
- `RDKit`, `DeepChem`, `Therapeutics Data Commons`, `SwissADME`
  - Best for: ligand preparation, chemical descriptors, QSAR, ADMET, and virtual-screening postprocessing
  - Weaknesses: predictions need experimental or literature validation before biological claims

## Imaging And Segmentation Tools

- `nnU-Net`
  - Best for: strong baseline automatic segmentation in compatible biomedical imaging tasks
  - Weaknesses: label quality, patient-level splits, and inference spacing must be controlled
- `MONAI`
  - Best for: flexible deep-learning medical imaging pipelines
  - Weaknesses: more implementation choices than nnU-Net
- `TotalSegmentator`
  - Best for: broad pretrained CT organ and structure segmentation
  - Weaknesses: task-specific tumors or local protocols still need validation
- `MedSAM` and SAM-derived models
  - Best for: promptable or foundation-model-assisted segmentation
  - Weaknesses: output must be checked against domain annotations
- `pyradiomics`
  - Best for: handcrafted radiomics feature extraction
  - Weaknesses: preprocessing, segmentation, scanner, and feature stability dominate results
- `QuPath`, `Cellpose`, `StarDist`, `Hover-Net`, `Mesmer`, `ilastik`
  - Best for: pathology, nuclei, cell, tissue, and multiplex-image segmentation
  - Weaknesses: marker panel and tissue morphology can require retraining or manual review
- `histoCAT`, `imcRtools`, `Squidpy`, `Giotto`, `CODEX MAV`
  - Best for: multiplex imaging, IMC, CODEX, MIBI, and spatial single-cell tissue analysis
  - Weaknesses: segmentation and channel normalization quality limit downstream conclusions
- `ST-Net`, `Hist2ST`, `HisToGene`, `THItoGene`, `iStar`, `STimage`, `FineST`
  - Best for: virtual spatial transcriptomics and histology-to-expression prediction
  - Weaknesses: outputs are inferred and need measured spatial or orthogonal validation

## Statistics And Visualization Tools

- `ComplexHeatmap`, `pheatmap`, `circlize`, `EnrichedHeatmap`
  - Best for: heatmaps, oncoprints, genomic heatmaps, and multi-panel annotations
  - Weaknesses: matrix scaling and clustering choices need reporting
- `ggplot2`, `ggpubr`, `ggrepel`, `ggforce`, `ggdist`, `ggraph`, `ggalluvial`, `patchwork`, `cowplot`
  - Best for: general publication figures and multi-panel layouts
  - Weaknesses: plot code must preserve source table and group order
- `EnhancedVolcano`, `UpSetR`, `ComplexUpset`, `maftools`, `ggtree`, `Gviz`, `karyoploteR`, `plotgardener`
  - Best for: volcano plots, set intersections, cancer mutation figures, trees, and genome tracks
  - Weaknesses: defaults often need manual checking for label overlap and size
- `lme4`, `glmmTMB`, `emmeans`, `metafor`, `riskRegression`, `pec`, `pROC`, `timeROC`
  - Best for: mixed models, model contrasts, meta-analysis, prediction evaluation, ROC, calibration, and survival prediction
  - Weaknesses: design and sample size determine validity

## Selection Checklist

Before locking the route, answer all of these:

1. What is the actual unit of inference: cell, sample, patient, spot, clonotype, or cohort?
2. Does the default tool family respect that unit of inference?
3. Is a replicate-aware design required?
4. Does the tool fit the available metadata and validation path?
5. Does it materially improve the scientific fit over the user's existing route?
6. Is the environment cost justified?

If the answer to 5 or 6 is weak, stay with the route that is already coherent with the established project style.
