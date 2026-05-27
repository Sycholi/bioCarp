# Multi-Omics Integration

Use this file for bulk multi-omics, single-cell multi-omics, CITE-seq, multiome, scNMT-seq, spatial multi-omics, proteogenomics, metabolomics integration, host-microbe integration, and public/private cohort validation.

## Intake

Before implementation, verify:

- modality list, sample overlap, same-cell pairing, same-sample pairing, time point, tissue site, patient identity, batch, platform, and missingness
- feature mapping between gene, transcript, protein, peak, methylation probe, metabolite, microbe, pathway, image feature, and clinical endpoint
- primary question: clustering, factor discovery, subtype discovery, feature selection, prediction, mechanism, validation, or visualization
- whether integration should preserve biology, remove batch, transfer labels, impute missing modality, infer regulatory links, or test association

## Core Route

Current route:

1. Run modality-specific QC, normalization, feature filtering, and sample-level review before integration.
2. Choose an anchor question and anchor modality. Integration without a biological question often produces hard-to-interpret factors.
3. Separate paired same-cell data, paired same-sample data, partially overlapping cohorts, and independent validation cohorts.
4. Use integration metrics and biological checks together. High technical mixing can weaken true biological separation.
5. Validate integrated results in modality-specific outputs before claiming a mechanism.

Required figures:

- sample overlap, missingness, and metadata consistency plots
- modality-specific PCA, UMAP, QC, and group structure plots
- feature mapping and identifier-loss summary
- integrated embedding, factor, network, or subtype plots
- modality contribution, loading, weight, or feature-importance plots
- external validation, orthogonal evidence, and sensitivity plots

## Bulk Multi-Omics

Current route:

1. Use `MultiAssayExperiment` or equivalent structures for partially matched cohorts.
2. Use `MOFA2` or MEFISTO for unsupervised factors, variance decomposition, sample grouping, time, or spatial context when appropriate.
3. Use `mixOmics`, DIABLO, sparse PLS, or block-PLS when supervised feature selection is explicitly requested.
4. Use iClusterPlus, SNF, Similarity Network Fusion, NEMO, or cancer subtype tools when subtype discovery is central.
5. Use pathway-level or regulator-level integration when feature-level dimensions are too high or sample size is limited.

Required figures:

- sample overlap and missingness map
- MOFA factor values, variance explained, factor-feature weights, and factor-phenotype association
- DIABLO CIM, circos, network, correlation circle, and feature stability plots
- subtype consensus, silhouette, survival, clinical association, and marker plots
- pathway-level integration heatmap and network plots

## Single-Cell Multi-Omics

Current route:

1. For paired RNA and protein, use Seurat WNN or totalVI according to object ecosystem, protein panel, and batch structure.
2. For paired RNA and ATAC, use Seurat WNN, Signac, ArchR, MultiVI, MOJITOO, Cobolt, or scGLUE according to pairing, scale, and regulatory question.
3. For unpaired modalities, use scGLUE, LIGER, Cobolt, MultiVI, scArches, Portal, or other verified alignment methods only after checking assumptions.
4. For CITE-seq, preserve ADT QC, isotype controls, background correction, protein normalization, and RNA-protein discordance.
5. For multiome, preserve fragments, peak calls, gene activity, motif activity, peak-to-gene links, chromVAR deviation, and RNA evidence.
6. For scNMT or methylation-linked data, preserve modality-specific sparsity and feature definitions before integration.

Primary tools:

- Seurat WNN, Signac, ArchR, MOJITOO
- totalVI and MultiVI from scvi-tools
- scGLUE, Cobolt, LIGER, Harmony, scArches, Portal, scJoint when verified
- Azimuth, CellTypist, scANVI, scArches for reference mapping and label transfer

Required figures:

- modality-specific QC and embeddings
- integrated embedding by modality, sample, batch, condition, and annotation
- modality weight or contribution plots
- RNA-protein, RNA-ATAC, peak-to-gene, motif-to-expression, and gene-activity concordance plots
- integration metric plots such as iLISI, cLISI, kBET, ASW, graph connectivity, marker preservation, and cell-type separation
- missing-modality imputation diagnostics when imputation is used

## Spatial And Imaging Multi-Omics

Current route:

1. Preserve coordinates, image, segmentation, molecular table, and region labels before cross-modal integration.
2. Use spatial deconvolution, mapping, and image-feature integration only when reference data and spatial platform are compatible.
3. Connect imaging, spatial expression, multiplex protein, single-cell references, and clinical data through patient-level or region-level units.
4. For virtual spatial outputs, keep predicted features separate from measured features.

Primary tools:

- RCTD, cell2location, Tangram, CARD, stereoscope, SpatialDWLS
- Squidpy, Giotto, SpatialExperiment, SpatialData
- ST-Net, Hist2ST, HisToGene, THItoGene, iStar, STimage, FineST when paired validation exists

Required figures:

- spatial alignment and image QC
- reference mapping and deconvolution maps
- measured-versus-predicted or measured-versus-inferred feature maps
- neighborhood, region, and spatial factor plots
- external tissue or held-out slide validation

## Cross-Omics Mechanism And Validation

Current route:

1. Translate features into pathways, regulators, cell types, metabolites, microbes, antigens, drug targets, or imaging regions before interpretation.
2. Use regulator and pathway inference from `bulk-inference.md` when direct feature matching is unstable.
3. Link variants, antigen peptides, RNA, protein, metabolite, microbiome, and clinical features only when sample matching and metadata support the claim.
4. Use public cohorts, orthogonal assays, spatial validation, or perturbation data for high-value claims.

Required figures:

- multi-layer evidence matrix
- cross-omics concordance heatmap
- pathway, regulator, antigen, metabolite, or microbial feature network
- cohort validation and sensitivity plots

## Source Index

Last checked: 2026-05-28.

- Seurat WNN: https://satijalab.org/seurat/articles/weighted_nearest_neighbor_analysis.html
- Seurat multimodal: https://satijalab.org/seurat/articles/multimodal_vignette.html
- scvi-tools totalVI: https://docs.scvi-tools.org/
- scvi-tools MultiVI: https://docs.scvi-tools.org/en/latest/user_guide/models/multivi.html
- MultiVI paper: https://www.nature.com/articles/s41592-023-01909-9
- scGLUE documentation: https://scglue.readthedocs.io/
- scGLUE paper: https://www.nature.com/articles/s41587-022-01284-4
- Cobolt paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC8715620/
- MOJITOO paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC9235504/
- MOFA2: https://bioconductor.org/packages/release/bioc/html/MOFA2.html
- MEFISTO: https://biofam.github.io/MOFA2/MEFISTO.html
- MultiAssayExperiment: https://bioconductor.org/packages/release/bioc/html/MultiAssayExperiment.html
- mixOmics and DIABLO: https://mixomics.org/
- Similarity Network Fusion: https://cran.r-project.org/package=SNFtool
