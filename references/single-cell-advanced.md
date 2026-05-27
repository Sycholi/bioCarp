# Single-Cell Advanced

Use this file when `index.md` selects advanced single-cell, spatial, perturbation, foundation-model, virtual-cell, drug-prediction, or training-course guidance.

This file is a working knowledge map. Before implementing any named tool, verify the current paper, repository, documentation, version, input format, model assumptions, and license. Do not use a tool only because it is new or named by the user.

## Tool Verification Gate

For every named or emerging tool:

1. Confirm the exact tool name. Similar names often refer to unrelated projects.
2. Find the primary paper, official documentation, official repository, or package page.
3. Check whether the method is peer-reviewed, preprint-only, code-only, or course material.
4. Check input requirements, model assumptions, supported species, supported modalities, output type, and required reference database.
5. Run a small validation or example when the task will depend on the result.
6. Label output as exploratory when the tool is new, weakly benchmarked, trained outside the disease context, or dependent on proprietary or unstable resources.

Examples:

- `SCIPAC` is a phenotype-associated cell method that combines scRNA-seq with bulk expression and phenotype data.
- `Scissor` is an earlier phenotype-associated cell method that links single-cell data with bulk phenotype data.
- `scPAS` is another phenotype-associated subpopulation method and should be compared with SCIPAC or Scissor only after checking inputs and endpoint fit.
- `scALPI` appears to refer to a GitLab single-cell analysis pipeline. Verify its wiki, scripts, and usage before treating it as a method standard.
- `scTenifoldNet` and `scTenifoldKnk` are gene-regulatory network and virtual knockout tools. Verify whether the task requires network perturbation rather than expression-only scoring.
- `SLOPER` is a spatial transcriptomics gradient-estimation method. Use it only when the question depends on spatial gradient direction, magnitude, or boundary structure.
- `SPARK` and `SPARK-X` are spatial expression pattern methods. Use them for spatially variable genes, then check selected genes on tissue maps.
- `scDecorr` is a feature-decorrelation representation learning method for single-cell integration. Compare it with established integration metrics before choosing it over routine routes.
- `TotalX` is a single-cell total RNA profiling protocol, not a downstream package. Treat it as an assay-specific preprocessing and QC route.
- `PSGRN` and `RegDiffusion` are GRN inference tools. PSGRN is linked to perturbational single-cell data; RegDiffusion uses diffusion-model logic for GRN inference.
- `TrendCatcher` is a longitudinal RNA-seq and scRNA-seq trend-analysis package. Use it when time-course trend classes matter.
- `scSurv` and `scSurvival` connect single-cell states with survival outcomes. Use patient-level survival metadata and keep clinical model diagnostics visible.
- `seismicGWAS` links GWAS summary statistics with single-cell expression for genetically implicated cell-type and driver-gene analysis.
- `phenoptr` and `phenoptrReports` are multiplex imaging and inForm-linked analysis tools. Route these through `imaging.md`.
- If a named tool cannot be verified from a reliable source, do not invent a workflow for it. Record it as unresolved and use a verified method family.

## Practical Training-Course Layer

When the user asks for routine or broad single-cell analysis, absorb the practical structure used in reputable training material, not only method papers.

Use this basic logic:

1. Define the biological question, sample design, metadata, and unit of inference before running tools.
2. Start from raw or minimally processed matrices when possible.
3. Perform staged QC and make diagnostic plots before filtering.
4. Treat filtering thresholds as dataset-specific decisions. Record the distribution, threshold, removed-cell counts, and biological reason.
5. Normalize, select features, reduce dimensions, cluster, annotate, and test hypotheses in that order unless the dataset structure forces a different route.
6. Keep sample-level and patient-level structure visible throughout analysis.
7. Interpret clusters through marker evidence, sample composition, and disease context.
8. Avoid turning exploratory embeddings into causal claims.

Training sources to use:

- Yale single-cell R hands-on workshop and Yale bioinformatics core pipeline descriptions
- Broad single-cell workshop
- Harvard single-cell support and workshop materials
- OSCA and Bioconductor single-cell books
- Seurat and Scanpy official tutorials
- disease-specific recent papers with public code

## Single-Cell RNA-seq QC And Preprocessing

Current route:

1. Preserve raw counts, filtered counts, sample metadata, chemistry version, tissue handling, dissociation or nuclei protocol, genome build, feature annotation, and Cell Ranger or equivalent version.
2. Read `platforms.md` when the data come from 10x, BD, MGI, BGI, DNBelab, Singleron, Parse, ScaleBio, Fluent, SMART-seq, split-pool, nuclei, fixed-cell, FFPE, documented vendor-specific, or spatial-linked workflows.
3. Read `parameters.md` before setting QC thresholds, doublet rate, ambient correction strength, normalization, integration, dimensions, clustering resolution, and marker thresholds.
4. Run empty-droplet and barcode-level review when raw droplet matrices are available.
5. Review ambient RNA contamination with `SoupX`, `CellBender`, `DecontX`, or package-specific alternatives when marker leakage, high background, damaged tissue, nuclei data, or dissociation artifacts are plausible.
6. Review doublets or multiplets with `scDblFinder`, `DoubletFinder`, `Scrublet`, `Solo`, or hashtag/genotype demultiplexing when available.
7. Check sample identity, sex markers, species-mixing markers, mitochondrial fraction, ribosomal fraction, hemoglobin genes, dissociation stress genes, cell-cycle scores, total counts, detected genes, and batch composition.
8. Apply thresholds after plotting each metric by sample. Avoid one global threshold when samples have different quality distributions.
9. Preserve a QC manifest with before-after cell counts per sample and reason for each filtering decision.
10. After preliminary clustering, evaluate cluster quality and cell-state heterogeneity with marker coherence, cluster purity, silhouette or average silhouette width, graph connectivity, entropy-based metrics, and `ROGUE` when the question depends on cluster purity or subtype definition.
11. For integrated objects, evaluate batch mixing and biological separation with `LISI` metrics such as iLISI and cLISI, plus kBET, ASW, graph connectivity, marker preservation, and sample or patient composition. Do not optimize batch mixing alone when it erases real biology.
12. For snRNA-seq, adjust mitochondrial expectations and ambient RNA review. For CITE-seq, multiome, or hashtag data, include modality-specific QC.

Required figures:

- platform, chemistry, vendor summary, barcode rank, sample-retention, mapping, saturation, and raw pipeline summary plots when available
- per-sample counts, detected genes, mitochondrial, ribosomal, hemoglobin, stress, and cell-cycle distributions
- scatter plots for counts versus genes and counts versus mitochondrial fraction
- empty-droplet, ambient RNA, and doublet diagnostic plots when those tools are used
- before-after UMAP or PCA by sample and QC class
- removed-cell summary bar plot and QC manifest table
- parameter before-after plots for central QC and integration choices
- cluster quality plots: marker coherence, silhouette or ASW, cluster size distribution, ROGUE score distribution or heatmap when used
- integration metric plots: iLISI, cLISI, kBET rejection rate, graph connectivity, batch mixing by sample and biology-preservation views when integration is used

Primary tools:

- EmptyDrops or Cell Ranger empty-droplet calls for droplet filtering
- SoupX, CellBender, DecontX for ambient RNA
- scDblFinder, DoubletFinder, Scrublet, Solo, hashtag or genotype demultiplexing for doublets
- Seurat, Scanpy, scater, scran, SingleCellExperiment for core QC handling
- ROGUE for entropy-based cluster purity and heterogeneity review
- LISI, scIB, kBET, ASW, silhouette, graph connectivity, NMI, ARI, and related metrics for integration and clustering assessment

## Normalization, Integration, Clustering, And Annotation

Current route:

1. Choose normalization from data structure: log-normalization, `SCTransform`, scran deconvolution, Scanpy normalization, or model-based workflows.
2. Do not regress out biological variables blindly. Cell cycle, mitochondrial fraction, ribosomal fraction, and stress scores should be regressed only when they are technical confounders for the stated question.
3. Use integration only when batch effects interfere with biological comparison. Inspect unintegrated and integrated embeddings.
4. Select dimensions using variance, elbow, marker stability, and batch-mixing diagnostics.
5. Run resolution sweeps and clustering stability checks. Use Leiden, Louvain, Seurat graph clustering, PhenoGraph, or package-native clustering as appropriate.
6. Evaluate resolution and annotation quality with ROGUE, silhouette or ASW, marker coherence, cluster size, nearest-neighbor graph connectivity, NMI or ARI across resolution sweeps, and reference-label agreement when suitable.
7. Evaluate integration with iLISI, cLISI, kBET, ASW, graph connectivity, cell-type separation, marker preservation, and sample or patient composition. Prefer a balance between technical mixing and biological structure preservation.
8. When self-supervised or deep-learning integration is requested, check `scDecorr`, `scDREAMER`, `scConfluence`, or scVI-family methods against the same integration and marker-preservation metrics.
9. If a user names `phiClust` or another uncommon clustering method, verify the exact tool and documentation before use.
10. Annotate with manual markers plus one or more reference tools when useful. Treat automated labels as draft labels.
11. For tumor data, distinguish malignant cells, normal epithelial cells, immune cells, stromal cells, and cycling or stressed states before fine annotation.

Required figures:

- unintegrated and integrated PCA or UMAP by sample, batch, condition, chemistry, and tissue
- resolution sweep, cluster tree or stability plots when clusters drive the claim
- ROGUE score plots, silhouette or ASW plots, cluster purity or heterogeneity heatmaps, and marker-coherence panels when cluster identity drives the claim
- iLISI, cLISI, kBET, ASW, graph connectivity, batch mixing, and marker-preservation plots when integration is used
- marker dot plots, violin plots, feature plots, heatmaps, and reference-label confusion plots
- annotation evidence panels for every final label
- cell fraction by sample or patient

Primary tools:

- Seurat v5, Harmony, RPCA, scVI, scANVI, scArches, Scanpy, SingleCellExperiment
- scDecorr, scDREAMER, scConfluence, and verified representation-learning integration tools when routine integration is insufficient
- SingleR, CellTypist, Azimuth, scANVI, Garnett, scmap, reference atlas transfer
- scType, scGate, UCell, AUCell, CellAssign, ProjecTILs, Symphony, popV, scPoli, treeArches, CASSIA, and manual marker panels for annotation and state scoring
- PhenoGraph or verified graph-clustering alternatives when standard clustering is not sufficient
- ROGUE, LISI, scIB, kBET, silhouette or ASW, graph connectivity, NMI, ARI, clustree, and clusterExperiment when clustering or integration quality needs formal review

## CITE-seq, ADT, And Single-Cell Multi-Omics

Use this module when protein, chromatin, methylation, perturbation, or other modalities are paired with single-cell RNA or partly paired across related datasets.

Current route:

1. Run modality-specific QC before integration. For ADT, check background, isotype controls, antibody panel, tag swapping, and protein count distributions.
2. For CITE-seq, use dsb, totalVI, Seurat WNN, CiteFuse, muon, or other verified routes according to object structure and batch design.
3. For RNA plus ATAC multiome, use Seurat WNN, Signac, ArchR, MultiVI, scGLUE, Cobolt, MOJITOO, or SnapATAC2 according to pairing, scale, and regulatory question.
4. For unpaired modalities, use scGLUE, Cobolt, LIGER, scJoint, scBridge, scMaui, scDART, UnionCom, Multigrate, scArches, or related tools only after checking assumptions and maintenance status.
5. Keep modality weights, modality-specific signal, missing-modality imputation, and feature concordance visible.

Required figures:

- modality-specific QC, ADT background, antibody signal, fragment or peak QC, and missingness plots
- integrated embedding by sample, batch, condition, annotation, and modality
- modality weight or contribution plots
- RNA-protein, RNA-ATAC, gene activity, peak-to-gene, motif-to-expression, and marker concordance panels
- iLISI, cLISI, kBET, ASW, graph connectivity, marker preservation, and modality mixing diagnostics
- imputation diagnostics when a missing modality is inferred

Primary tools:

- Seurat WNN, Signac, ArchR, dsb, CiteFuse, totalVI, MultiVI, muon, Multigrate
- scGLUE, Cobolt, MOJITOO, LIGER, scJoint, scBridge, scMaui, scDART, UnionCom, scArches, Portal, SnapATAC2

## Trajectory, Fate, And Velocity Extensions

Use this module when the task needs fate probability, vector field, transition matrix, optimal transport, diffusion pseudotime, or terminal-state prioritization beyond a basic pseudotime plot.

Current route:

1. Confirm that the selected cells plausibly represent a biological process before running trajectory tools.
2. Use CellRank when terminal fate probabilities, absorption probabilities, and driver genes are central.
3. Use dynamo when vector-field reconstruction, acceleration, curvature, or perturbation-linked dynamics fit the data and assumptions.
4. Use Palantir, Waddington-OT, FateID, destiny or DPT, PAGA, or CellRouter when their model and input fit the question.
5. Use TrendCatcher, tradeSeq, condiments, or Lamian when longitudinal trend classes, differential trajectories, or time-course expression programs are central.
6. Anchor direction with time, markers, lineage labels, velocity, perturbation, or experimental design. State uncertainty when direction is not resolved.

Required figures:

- selected-cell embedding by sample, condition, cluster, and key markers
- lineage graph, diffusion map, vector field, transition matrix, fate probability, terminal state, and driver-gene plots as supported
- pseudotime or latent-time distribution by sample and condition
- gene trends, branch heatmaps, and terminal-state marker panels
- time-course trend-class plots, fitted curves, and gene-set summaries when TrendCatcher or related trend tools are used
- tool-specific diagnostics and uncertainty plots

Primary tools:

- CellRank, dynamo, velocyto, Palantir, Waddington-OT, FateID, destiny or DPT, PAGA, CellRouter, Monocle3, slingshot, tradeSeq, scVelo, TrendCatcher, condiments, Lamian

## Gene Regulatory Network And Regulon Analysis

Use this module when the question depends on TF networks, enhancer-to-gene links, regulon activity, perturbation targets, or regulatory mechanism.

Current route:

1. Choose GRN tools by input modality: expression-only, ATAC-only, multiome, perturbation, or time-course.
2. Use SCENIC or pySCENIC for expression-based regulon discovery and activity scoring.
3. Use SCENIC+, Pando, CellOracle, scGLUE, Signac, ArchR, chromVAR, Cicero, or SnapATAC2 when chromatin or multiome evidence is available.
4. Use GRNBoost2, GENIE3, PIDC, or Inferelator when network inference itself is the main method and assumptions are checked.
5. Use PSGRN, CellOracle, Scribe, SINGE, or verified perturbation-aware tools when interventional, temporal, or pseudotemporal data support causal or directional network claims.
6. Use RegDiffusion, PMF-GRN, scSGL, scMGATGRN, SCODE, SINCERITIES, LEAP, or TENET only after checking training data, benchmark setting, input scale, and maintenance status.
7. Validate regulators with motif evidence, target expression, perturbation evidence, literature, and cell-state specificity.

Required figures:

- regulon activity UMAP, heatmap, and cell-type distribution
- TF-target network or target-gene evidence plots
- motif enrichment or motif deviation plots when ATAC data exist
- peak-to-gene and TF-to-target support plots when multiome data exist
- perturbation or external evidence panels when used
- network benchmark, edge-confidence, perturbation-recovery, or pseudotime-direction diagnostics when advanced GRN methods are used

Primary tools:

- SCENIC, pySCENIC, SCENIC+, GRNBoost2, GENIE3, PIDC, Inferelator, Pando, CellOracle, scGLUE, chromVAR, Cicero, Signac, ArchR
- PSGRN, RegDiffusion, Scribe, SINGE, PMF-GRN, scSGL, scMGATGRN, SCODE, SINCERITIES, LEAP, TENET when the data and validation plan fit

## Phenotype-Associated Cell Methods

Use when scRNA-seq has limited sample count but a matched or comparable bulk cohort has phenotype, survival, stage, response, or quantitative endpoint.

Current route:

1. Harmonize genes between single-cell and bulk data.
2. Confirm that the bulk phenotype is biologically compatible with the single-cell tissue and disease state.
3. Use Scissor, SCIPAC, scPAS, PACells, DEGAS, scSurv, scSurvival, or related methods according to phenotype type and output required.
4. Keep the bulk prediction model, phenotype label, clinical covariates, and cross-validation visible.
5. Compare phenotype-associated cells with cell type, cluster, pathway activity, CNV status, sample, and patient composition.
6. Treat results as hypothesis-generating unless validated in independent single-cell, spatial, clinical, or perturbation data.

Required figures:

- bulk model performance or cross-validation summary
- UMAP colored by phenotype-association score or class
- association score by cell type, cluster, sample, and condition
- marker and pathway plots for phenotype-associated states
- hazard contribution, survival-stratified cell-state, and spatial hazard maps when survival-oriented tools are used
- validation plots in external cohort or spatial data when available

Primary tools:

- Scissor
- SCIPAC
- scPAS
- DEGAS
- scSurv and scSurvival for survival-oriented single-cell state analysis
- PACells for scATAC-to-bulk ATAC phenotype association when appropriate

## Foundation Models, Virtual Cells, And In Silico Perturbation

Use this module for single-cell foundation models, virtual knockout, virtual cells, cell-state prediction, or gene-regulatory perturbation.

Current route:

1. Confirm whether the model operates on raw counts, normalized expression, ranked genes, tokens, GRNs, multimodal features, or embeddings.
2. Check whether the training corpus covers the species, tissue, disease, assay, and perturbation type.
3. Do not treat foundation-model predictions as biological validation. Use them for prioritization, embedding, annotation support, perturbation hypothesis generation, or candidate ranking.
4. For virtual perturbation, compare with real Perturb-seq, CROP-seq, CRISPR, drug perturbation, knockout, or literature evidence when possible.
5. Record model version, checkpoint, gene vocabulary, preprocessing, and prompt or perturbation settings.

Required figures:

- embedding or latent-space visualization before and after model use
- predicted perturbation effect size, direction, and uncertainty when available
- top genes, pathways, regulons, and cell states affected by virtual perturbation
- comparison against known perturbation signatures or external datasets
- failure or out-of-distribution diagnostics when available

Primary tools:

- Geneformer
- scGPT
- scFoundation
- UCE or related single-cell foundation models when verified
- scTenifoldNet and scTenifoldKnk for GRN comparison and virtual knockout
- CellOracle or related GRN-based perturbation tools when regulatory network context is required

## Drug Prediction And Drug Repurposing

Use this module when the task asks for candidate drugs, reversal signatures, drug sensitivity, chemical perturbation, or therapeutic prioritization.

Current route:

1. Define the disease or target cell-state signature before querying drug resources.
2. Decide whether the goal is signature reversal, drug sensitivity, compound class prediction, target prioritization, or combination therapy.
3. Use CMap or LINCS L1000, DrugReflector, scDrug, scDrug+, scDrugPrio, drug2cell, DepMap, GDSC, PRISM, DrugBank, ChEMBL, Open Targets, CTD, or DGIdb according to the question.
4. Keep training domain and assay mismatch explicit. A cancer cell-line model does not automatically validate primary tumor cell response.
5. Prioritize drugs only after checking target expression in the relevant cell type, direction of disease signature, druggability, known mechanism, toxicity, clinical status, and independent evidence.
6. Treat drug predictions as candidate ranking, not treatment recommendation.

Required figures:

- disease or target-cell signature heatmap and pathway summary
- drug ranking table and score distribution
- CMap or LINCS connectivity heatmap when used
- predicted IC50, AUC, sensitivity, or class-score heatmap by cell state when supported
- target expression plots in relevant cell types
- evidence matrix across CMap, LINCS, DepMap, GDSC, PRISM, DrugBank, Open Targets, CTD, and literature

Primary tools and resources:

- CMap and LINCS L1000
- DrugReflector
- scDrug and scDrug+
- scDrugPrio
- drug2cell
- DepMap, GDSC, PRISM, DrugBank, ChEMBL, Open Targets, CTD, DGIdb

## Perturbation Databases And Single-Cell Perturbation Screens

Use this module for Perturb-seq, CROP-seq, CRISPR screens, sci-Plex, ECCITE-seq, Perturb-ATAC, SHARE-seq, drug perturbation screens, or public perturbation resources.

Current route:

1. Preserve guide RNA, perturbation ID, target gene, MOI, guide assignment confidence, UMI counts, cell barcode, sample, batch, treatment dose, time point, and control labels.
2. Filter low-confidence guide assignments, multiplets, failed perturbations, and cells without valid perturbation labels.
3. Separate guide-level QC, perturbation-level aggregation, cell-state analysis, and differential response modeling.
4. Use non-targeting controls, safe-targeting controls, and multiple guides per gene when available.
5. Model perturbation effects at guide, gene, cell type, and pathway levels. Include replicate and batch when available.
6. Use public resources such as scPerturb, PerturBase, Replogle-scale Perturb-seq, LINCS, CMap, and DepMap to support interpretation.
7. For perturbation prediction or response transfer, use GEARS, CPA, chemCPA, CellOT, scVIDR, RespondOS, scGen, or related tools only after checking perturbation type, training domain, and validation evidence.
8. For differential abundance or composition effects, use Milo, miloDE, scCODA, MASC, DA-seq, MELD, Augur, or replicate-aware models according to design.

Required figures:

- guide assignment and perturbation coverage plots
- cells per guide, guides per gene, and perturbation balance plots
- embedding by perturbation, control, and cell state
- perturbation effect volcano, heatmap, and pathway summary
- guide concordance and replicate concordance plots
- benchmark or external perturbation signature comparison when available
- differential abundance, response prediction, or perturbation transfer diagnostics when those tools are used

Primary tools and resources:

- Seurat Mixscape
- pertpy Mixscape and Augur
- scGen, GEARS, CPA, chemCPA, CellOT, scVIDR, RespondOS, or verified perturbation-prediction models when prediction is required
- Milo, miloDE, scCODA, MASC, DA-seq, MELD for abundance or composition changes when design supports them
- scPerturb
- PerturBase
- Replogle genome-scale Perturb-seq datasets
- LINCS and CMap perturbation signatures

## Spatial Algorithms And Neighborhood Analysis

Use this module when spatial claims depend on domains, neighborhoods, niches, adjacency, co-localization, spatially variable genes, deconvolution, or cell-cell interaction in tissue.

Current route:

1. Identify platform resolution first: Visium, Visium HD, Slide-seq, MERFISH, Xenium, CosMx, Stereo-seq, DBiT-seq, CODEX, or imaging mass cytometry.
2. Preserve tissue image, segmentation, coordinates, cell or spot area, slide, sample, region, batch, and histology labels.
3. Build spatial graphs appropriate to the platform: radius, kNN, Delaunay, grid adjacency, or segmentation-derived contact graph.
4. Run domain or niche detection with Seurat, Giotto, Squidpy, BANKSY, CellCharter, BayesSpace, SpaGCN, GraphST, PRECAST, STAGATE, DeepST, SEDR, SpaSEG, stLearn, or verified alternatives.
5. Run neighborhood enrichment, co-occurrence, spatial autocorrelation, spatially variable genes, proximity, hotspot, and cell-type adjacency tests as needed. Use SPARK, SPARK-X, SpatialDE, SpatialDE2, nnSVG, MERINGUE, scBSP, SMASH, SpaGene, Splotch, or trendsceek according to scale and model fit.
6. Use RCTD, cell2location, CARD, SpatialDWLS, Tangram, stereoscope, DestVI, SPOTlight, STdeconvolve, SpatialDecon, STRIDE, NMFreg, SpaOTsc, novoSpaRc, CellTrek, CytoSPACE, or equivalent tools for deconvolution or mapping only when references match.
7. For differential abundance or differential neighborhoods, use sample-aware designs and tools such as Milo when the graph-neighborhood framework fits.
8. Use SLOPER, SpaceWalker, SpatialPCA, sosta, SpatialFeatureExperiment, Sopa, FICTURE, CartoScope, SPICEMIX, or other verified tools when the task asks for gradients, anatomical structure, molecular-resolution maps, or specialized spatial exploration.
9. For spatial communication or microenvironment modeling, use COMMOT, SpaTalk, MISTy, MultiNicheNet, NicheCompass, MEBOCOST, NATMI, or Tensor-cell2cell when spatial coordinates, conditions, or metabolic communication support the question.

Required figures:

- tissue image with QC, clusters, domains, and regions
- graph or neighborhood construction diagnostic
- spatial domain maps from selected algorithms
- neighborhood enrichment, co-occurrence, proximity, or adjacency plots
- spatially variable gene maps and autocorrelation summaries
- gradient vector, gradient magnitude, spatial boundary, and tissue-structure plots when SLOPER, SpaceWalker, or related gradient tools are used
- deconvolution maps, cell-type abundance maps, and reference-fit diagnostics
- spatial interaction or ligand-receptor plots when supported
- spatial domain, spatially variable gene, denoising, and spatial communication diagnostics from the selected tool

Primary tools:

- Seurat spatial, SpatialExperiment, Giotto, Squidpy
- BANKSY, CellCharter, BayesSpace, SpaGCN, GraphST, PRECAST, STAGATE, DeepST, SEDR, SpaSEG, stLearn, SpatialDE, SpatialDE2, nnSVG, MERINGUE, Splotch, SpotClean
- SPARK, SPARK-X, scBSP, SMASH, SpaGene, trendsceek for spatial expression pattern detection
- SLOPER, SpaceWalker, SpatialPCA, sosta, SpatialFeatureExperiment, Sopa, FICTURE, CartoScope, SPICEMIX for gradients, anatomical structures, molecular-resolution exploration, or spatial representation learning when verified
- RCTD, cell2location, CARD, SpatialDWLS, Tangram, stereoscope, DestVI, SPOTlight, STdeconvolve, SpatialDecon, STRIDE, NMFreg, SpaOTsc, novoSpaRc, CellTrek, CytoSPACE
- COMMOT, SpaTalk, MISTy, MultiNicheNet, NicheCompass, MEBOCOST, NATMI, Tensor-cell2cell
- Milo or equivalent neighborhood differential abundance tools

## Source Index

Last checked: 2026-05-28.

- Single-cell best practices review: https://www.nature.com/articles/s41576-023-00586-w
- OSCA: https://bioconductor.org/books/release/OSCA/
- Yale single-cell R workshop: https://ysph.yale.edu/event/single-cell-rna-seq-data-analysis-and-visualization-using-r-a-hands-on-workshop/
- Yale bioinformatics core: https://medicine.yale.edu/genetics/research/ycga/bioinformatics
- Broad single-cell workshop: https://broadinstitute.github.io/2020_scWorkshop/
- Harvard single-cell support practices: https://pmc.ncbi.nlm.nih.gov/articles/PMC6938040/
- SoupX: https://github.com/constantAmateur/SoupX
- CellBender: https://cellbender.readthedocs.io/
- DecontX: https://bioconductor.org/packages/release/bioc/html/celda.html
- scDblFinder: https://bioconductor.org/packages/release/bioc/html/scDblFinder.html
- DoubletFinder: https://github.com/chris-mcginnis-ucsf/DoubletFinder
- Scrublet: https://github.com/swolock/scrublet
- DropletUtils: https://bioconductor.org/packages/release/bioc/html/DropletUtils.html
- miQC: https://bioconductor.org/packages/release/bioc/html/miQC.html
- scuttle: https://bioconductor.org/packages/release/bioc/html/scuttle.html
- scran: https://bioconductor.org/packages/release/bioc/html/scran.html
- CellTypist: https://www.celltypist.org/
- Azimuth: https://azimuth.hubmapconsortium.org/
- scANVI: https://docs.scvi-tools.org/en/stable/user_guide/models/scanvi.html
- totalVI: https://docs.scvi-tools.org/en/latest/user_guide/models/totalvi.html
- MultiVI: https://docs.scvi-tools.org/en/latest/user_guide/models/multivi.html
- muon: https://muon.scverse.org/
- scGLUE: https://scglue.readthedocs.io/
- scDecorr paper: https://www.nature.com/articles/s41598-026-50586-z
- TotalX paper: https://www.nature.com/articles/s41587-026-03068-6
- PSGRN repository: https://github.com/GuanLab/PSGRN
- RegDiffusion repository: https://github.com/TuftsBCB/RegDiffusion
- TrendCatcher documentation: https://jaleesr.github.io/TrendCatcher/
- scSurv paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC12797213/
- scSurvival paper: https://aacrjournals.org/cancerdiscovery/article/16/5/931/784405/scSurvival-Single-Cell-Survival-Analysis-of
- seismicGWAS documentation: https://ylaboratory.github.io/seismic/
- SPARK paper: https://www.nature.com/articles/s41592-019-0701-7
- SPARK repository: https://github.com/xzhoulab/SPARK
- SLOPER note and source pointer: https://chitra-lab.github.io/2025/12/01/sloper/
- CellRank: https://cellrank.readthedocs.io/
- dynamo: https://dynamo-release.readthedocs.io/
- COMMOT paper: https://www.nature.com/articles/s41592-022-01728-4
- MISTy paper: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02663-5
- MultiNicheNet: https://github.com/saeyslab/multinichenetr
- NicheCompass: https://github.com/Lotfollahi-lab/nichecompass
- SCENIC: https://scenic.aertslab.org/
- SCENIC+: https://scenicplus.readthedocs.io/
- pySCENIC: https://pyscenic.readthedocs.io/
- Pando: https://quadbiolab.github.io/Pando/
- SCIPAC paper: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-024-03263-1
- Scissor repository: https://github.com/sunduanchen/Scissor
- scPAS documentation: https://aiminxie.github.io/scPAS/
- Geneformer: https://huggingface.co/ctheodoris/Geneformer
- scGPT: https://github.com/bowang-lab/scGPT
- scTenifoldNet: https://github.com/cailab-tamu/scTenifoldNet
- DrugReflector source: https://github.com/Cellarity/drugreflector
- DrugReflector checkpoints: https://zenodo.org/records/17437512
- scDrug paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC9747355/
- scDrug+ paper: https://www.sciencedirect.com/science/article/pii/S0753332224009545
- scPerturb database: https://www.sanderlab.org/scPerturb/
- scPerturb paper: https://www.nature.com/articles/s41592-023-02144-y
- PerturBase paper: https://academic.oup.com/nar/article/53/D1/D1099/7815638
- Replogle Perturb-seq paper: https://pubmed.ncbi.nlm.nih.gov/35688146/
- pertpy documentation: https://pertpy.readthedocs.io/
- GEARS repository: https://github.com/snap-stanford/GEARS
- CPA: https://github.com/theislab/cpa
- chemCPA: https://github.com/theislab/chemCPA
- CMap L1000 paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC5990023/
- CMap CLUE: https://clue.io/cmap
- DepMap: https://depmap.org/
- Open Targets: https://platform.opentargets.org/
- CTD 2025 update: https://pmc.ncbi.nlm.nih.gov/articles/PMC11701581/
- BANKSY paper: https://www.nature.com/articles/s41588-024-01664-3
- BANKSY Bioconductor package: https://bioconductor.org/packages/release/bioc/html/Banksy.html
- CellCharter documentation: https://cellcharter.readthedocs.io/
- Milo paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC7617075/
- Tangram: https://github.com/broadinstitute/Tangram
- cell2location: https://cell2location.readthedocs.io/
- SPOTlight: https://bioconductor.org/packages/release/bioc/html/SPOTlight.html
- STAGATE: https://github.com/zhanglabtools/STAGATE
- GraphST: https://github.com/JinmiaoChenLab/GraphST
- scALPI GitLab project: https://gitlab.com/pwirapati/scalpi
