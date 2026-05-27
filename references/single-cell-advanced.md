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
2. Run empty-droplet and barcode-level review when raw droplet matrices are available.
3. Review ambient RNA contamination with `SoupX`, `CellBender`, `DecontX`, or package-specific alternatives when marker leakage, high background, damaged tissue, nuclei data, or dissociation artifacts are plausible.
4. Review doublets or multiplets with `scDblFinder`, `DoubletFinder`, `Scrublet`, `Solo`, or hashtag/genotype demultiplexing when available.
5. Check sample identity, sex markers, species-mixing markers, mitochondrial fraction, ribosomal fraction, hemoglobin genes, dissociation stress genes, cell-cycle scores, total counts, detected genes, and batch composition.
6. Apply thresholds after plotting each metric by sample. Avoid one global threshold when samples have different quality distributions.
7. Preserve a QC manifest with before-after cell counts per sample and reason for each filtering decision.
8. For snRNA-seq, adjust mitochondrial expectations and ambient RNA review. For CITE-seq, multiome, or hashtag data, include modality-specific QC.

Required figures:

- per-sample counts, detected genes, mitochondrial, ribosomal, hemoglobin, stress, and cell-cycle distributions
- scatter plots for counts versus genes and counts versus mitochondrial fraction
- empty-droplet, ambient RNA, and doublet diagnostic plots when those tools are used
- before-after UMAP or PCA by sample and QC class
- removed-cell summary bar plot and QC manifest table

Primary tools:

- EmptyDrops or Cell Ranger empty-droplet calls for droplet filtering
- SoupX, CellBender, DecontX for ambient RNA
- scDblFinder, DoubletFinder, Scrublet, Solo, hashtag or genotype demultiplexing for doublets
- Seurat, Scanpy, scater, scran, SingleCellExperiment for core QC handling

## Normalization, Integration, Clustering, And Annotation

Current route:

1. Choose normalization from data structure: log-normalization, `SCTransform`, scran deconvolution, Scanpy normalization, or model-based workflows.
2. Do not regress out biological variables blindly. Cell cycle, mitochondrial fraction, ribosomal fraction, and stress scores should be regressed only when they are technical confounders for the stated question.
3. Use integration only when batch effects interfere with biological comparison. Inspect unintegrated and integrated embeddings.
4. Select dimensions using variance, elbow, marker stability, and batch-mixing diagnostics.
5. Run resolution sweeps and clustering stability checks. Use Leiden, Louvain, Seurat graph clustering, PhenoGraph, or package-native clustering as appropriate.
6. If a user names `phiClust` or another uncommon clustering method, verify the exact tool and documentation before use.
7. Annotate with manual markers plus one or more reference tools when useful. Treat automated labels as draft labels.
8. For tumor data, distinguish malignant cells, normal epithelial cells, immune cells, stromal cells, and cycling or stressed states before fine annotation.

Required figures:

- unintegrated and integrated PCA or UMAP by sample, batch, condition, chemistry, and tissue
- resolution sweep, cluster tree or stability plots when clusters drive the claim
- marker dot plots, violin plots, feature plots, heatmaps, and reference-label confusion plots
- annotation evidence panels for every final label
- cell fraction by sample or patient

Primary tools:

- Seurat v5, Harmony, RPCA, scVI, scANVI, scArches, Scanpy, SingleCellExperiment
- SingleR, CellTypist, Azimuth, scANVI, Garnett, scmap, reference atlas transfer
- PhenoGraph or verified graph-clustering alternatives when standard clustering is not sufficient

## Phenotype-Associated Cell Methods

Use when scRNA-seq has limited sample count but a matched or comparable bulk cohort has phenotype, survival, stage, response, or quantitative endpoint.

Current route:

1. Harmonize genes between single-cell and bulk data.
2. Confirm that the bulk phenotype is biologically compatible with the single-cell tissue and disease state.
3. Use Scissor, SCIPAC, scPAS, or related methods according to phenotype type and output required.
4. Keep the bulk prediction model, phenotype label, clinical covariates, and cross-validation visible.
5. Compare phenotype-associated cells with cell type, cluster, pathway activity, CNV status, sample, and patient composition.
6. Treat results as hypothesis-generating unless validated in independent single-cell, spatial, clinical, or perturbation data.

Required figures:

- bulk model performance or cross-validation summary
- UMAP colored by phenotype-association score or class
- association score by cell type, cluster, sample, and condition
- marker and pathway plots for phenotype-associated states
- validation plots in external cohort or spatial data when available

Primary tools:

- Scissor
- SCIPAC
- scPAS
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

Required figures:

- guide assignment and perturbation coverage plots
- cells per guide, guides per gene, and perturbation balance plots
- embedding by perturbation, control, and cell state
- perturbation effect volcano, heatmap, and pathway summary
- guide concordance and replicate concordance plots
- benchmark or external perturbation signature comparison when available

Primary tools and resources:

- Seurat Mixscape
- pertpy Mixscape and Augur
- scGen, GEARS, CPA, or verified perturbation-prediction models when prediction is required
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
4. Run domain or niche detection with Seurat, Giotto, Squidpy, BANKSY, CellCharter, BayesSpace, SpaGCN, GraphST, PRECAST, stLearn, or verified alternatives.
5. Run neighborhood enrichment, co-occurrence, spatial autocorrelation, spatially variable genes, proximity, hotspot, and cell-type adjacency tests as needed.
6. Use RCTD, cell2location, CARD, SpatialDWLS, Tangram, stereoscope, or equivalent tools for deconvolution or mapping only when references match.
7. For differential abundance or differential neighborhoods, use sample-aware designs and tools such as Milo when the graph-neighborhood framework fits.

Required figures:

- tissue image with QC, clusters, domains, and regions
- graph or neighborhood construction diagnostic
- spatial domain maps from selected algorithms
- neighborhood enrichment, co-occurrence, proximity, or adjacency plots
- spatially variable gene maps and autocorrelation summaries
- deconvolution maps, cell-type abundance maps, and reference-fit diagnostics
- spatial interaction or ligand-receptor plots when supported

Primary tools:

- Seurat spatial, SpatialExperiment, Giotto, Squidpy
- BANKSY, CellCharter, BayesSpace, SpaGCN, GraphST, PRECAST, stLearn
- RCTD, cell2location, CARD, SpatialDWLS, Tangram, stereoscope
- Milo or equivalent neighborhood differential abundance tools

## Source Index

Last checked: 2026-05-27.

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
- CellTypist: https://www.celltypist.org/
- Azimuth: https://azimuth.hubmapconsortium.org/
- scANVI: https://docs.scvi-tools.org/en/stable/user_guide/models/scanvi.html
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
- CMap L1000 paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC5990023/
- CMap CLUE: https://clue.io/cmap
- DepMap: https://depmap.org/
- Open Targets: https://platform.opentargets.org/
- CTD 2025 update: https://pmc.ncbi.nlm.nih.gov/articles/PMC11701581/
- BANKSY paper: https://www.nature.com/articles/s41588-024-01664-3
- BANKSY Bioconductor package: https://bioconductor.org/packages/release/bioc/html/Banksy.html
- CellCharter documentation: https://cellcharter.readthedocs.io/
- Milo paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC7617075/
- scALPI GitLab project: https://gitlab.com/pwirapati/scalpi
