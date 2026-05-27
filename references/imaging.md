# Imaging

Use this file for pathology imaging, radiomics, pathomics, medical image segmentation, automatic contouring, multiplex immunofluorescence, CODEX, MIBI, imaging mass cytometry, CyTOF-linked tissue analysis, virtual multiplex immunofluorescence, virtual staining, histology-to-spatial transcriptomics prediction, and virtual spatial omics.

## Intake

Before implementation, verify:

- image type: CT, MRI, PET, ultrasound, WSI, H&E, IHC, IF, mIF, MxIF, CODEX, MIBI, IMC, CyCIF, Xenium image, Visium image, or label-free microscopy
- file format, resolution, magnification, channel names, stain panel, bit depth, tile structure, compression, scanner, and batch
- paired data: segmentation masks, contours, DICOM RTSTRUCT, cell table, spatial transcriptomics, IHC, mIF, scRNA-seq, clinical labels, regions of interest, pathologist annotations, radiologist annotations, or treatment planning structures
- endpoint: cell phenotyping, spatial neighborhood, automatic contouring, radiomics, virtual staining, virtual mIF, virtual spatial transcriptomics, prognosis, treatment response, or validation figure
- whether the task is analysis of measured imaging data or prediction of unmeasured markers

## Measured Multiplex Imaging

Current route:

1. Preserve raw images, channel metadata, panel design, exposure settings, tissue masks, segmentation masks, and cell tables.
2. Run image QC for blur, saturation, tissue folds, background, autofluorescence, channel spillover, registration, and batch effects.
3. Segment nuclei and cells with method appropriate to the platform. Use existing validated masks when available.
4. Quantify marker intensities, normalize channels, define cell phenotypes, and preserve marker evidence.
5. Analyze cell abundance, co-expression, neighborhoods, cell-cell contacts, spatial statistics, and tissue regions.
6. Use pathology review or marker panels to validate phenotypes before biological interpretation.

Required figures:

- raw channel montage and composite images
- tissue mask, segmentation mask, and cell boundary overlays
- marker intensity QC and channel normalization plots
- cell phenotype UMAP or t-SNE, marker heatmap, and phenotype evidence panels
- spatial cell maps, neighborhood maps, contact graphs, and interaction heatmaps
- region-level composition plots and group comparisons

## Virtual Multiplex Immunofluorescence And Virtual Staining

Current route:

1. Treat virtual mIF or virtual staining as prediction unless matched measured stains validate it.
2. Require paired training data or a documented pretrained model with compatible tissue, stain, scanner, and resolution.
3. Split by patient or slide, not by adjacent tiles from the same slide, when evaluating model performance.
4. Compare virtual channels with measured IF, IHC, mIF, or expert annotation using pixel-level, cell-level, and region-level metrics.
5. Use the virtual result for screening or hypothesis generation unless validation supports quantitative use.
6. Record model architecture, checkpoint, training data, preprocessing, stain normalization, and uncertainty estimation.

Required figures:

- input H&E or label-free image and predicted virtual channel montage
- measured versus predicted channel overlays when paired data exist
- pixel-level correlation, SSIM or PSNR, and cell-level marker concordance plots
- cell phenotype concordance and spatial pattern concordance plots
- uncertainty or error heatmap
- external-slide validation plots

## Virtual Spatial Transcriptomics

Use this module when the task predicts spatial gene expression, cell abundance, pathway activity, or tissue niches from histology or other imaging data.

Current route:

1. Confirm whether the task is measured spatial transcriptomics analysis, super-resolution, imputation, or histology-to-expression prediction.
2. Require paired histology and spatial transcriptomics for training, tuning, or credible validation.
3. Use tools or model families such as ST-Net, Hist2ST, HisToGene, THItoGene, iStar, BLEEP, STimage, FineST, or pathology-foundation-model-based regressors only after verifying current code and model access.
4. Evaluate per gene, per pathway, per cell type, and per region. A global correlation alone is insufficient.
5. Mark virtual spatial output as inferred and separate it from measured spatial data in plots and text.
6. Validate key claims with measured spatial data, IHC, mIF, single-cell references, or external slides when possible.

Required figures:

- histology tile or WSI overview with tissue masks
- measured versus predicted spatial expression maps for selected genes
- predicted pathway or cell-type abundance maps
- per-gene and per-sample performance distribution
- residual or uncertainty spatial maps
- region-level concordance and clinical association plots
- external cohort or held-out tissue validation plots

## Radiomics And Pathomics

Current route:

1. Keep image acquisition, preprocessing, segmentation, feature extraction, and model evaluation separate.
2. Use IBSI-aware radiomics principles when extracting handcrafted features.
3. For pathology foundation models or WSI deep learning, split at patient level and preserve tile-to-slide aggregation logic.
4. Report calibration, discrimination, decision-curve or clinical utility only when labels and sample size support it.
5. Link imaging signatures to molecular, single-cell, spatial, microbiome, or clinical features only after checking cohort alignment.

Required figures:

- segmentation or region annotation QC
- feature distribution and batch plots
- model performance with ROC, PR, calibration, and decision-curve plots when relevant
- attention, heatmap, or tile-level attribution plots for WSI models
- imaging-molecular association plots and external validation plots

## Automatic Segmentation And Contouring

Use this module for tumor segmentation, organ-at-risk contouring, pathology tissue segmentation, nuclei or cell segmentation, radiotherapy structure generation, and batch segmentation QC.

Current route:

1. Define segmentation target, imaging modality, label protocol, annotator source, label hierarchy, and clinical tolerance before model selection.
2. For medical imaging, use `nnU-Net` as the default baseline when data are volumetric and labels are compatible. Use MONAI, TotalSegmentator, MedSAM, SAM-derived models, or task-specific models only when they improve fit or are required by data type.
3. For pathology and multiplex images, use Cellpose, StarDist, QuPath, ilastik, Hover-Net, Mesmer, or platform-specific segmenters according to nuclear, membrane, cytoplasm, and tissue context.
4. Split train, validation, and test sets at patient level. Avoid tile-level leakage.
5. Preserve preprocessing, spacing, resampling, intensity normalization, patch size, class labels, and postprocessing.
6. Evaluate with Dice, Jaccard, Hausdorff distance, surface Dice, sensitivity, precision, volume difference, and clinically relevant dose or region metrics when applicable.
7. Perform visual review across best, median, and worst cases. Do not report only aggregate metrics.

Required figures:

- annotation protocol diagram or label summary
- image, ground truth, prediction, and error-overlay panels
- Dice or surface Dice distribution by class and cohort
- Hausdorff or boundary-error plots
- confusion or overlap plots for multiclass segmentation
- volume or area correlation and Bland-Altman plots
- failure-case montage and QC table
- radiotherapy contour comparison and dose-volume histogram changes when treatment planning is involved

## Source Index

Last checked: 2026-05-27.

- CODEX support: https://help.codex.bio/codex/mav/overview
- nnU-Net paper: https://www.nature.com/articles/s41592-020-01008-z
- nnU-Net repository: https://github.com/MIC-DKFZ/nnUNet
- MONAI: https://monai.io/
- TotalSegmentator repository: https://github.com/wasserth/TotalSegmentator
- PyRadiomics documentation: https://pyradiomics.readthedocs.io/en/stable/index.html
- IBSI radiomics standard paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC7193906/
- Cellpose paper: https://www.nature.com/articles/s41592-020-01018-x
- StarDist paper: https://arxiv.org/abs/1806.03535
- QuPath paper: https://www.nature.com/articles/s41598-017-17204-5
- IMC analysis review: https://pmc.ncbi.nlm.nih.gov/articles/PMC10115470/
- MIBI tumor microenvironment paper: https://www.nature.com/articles/s41374-020-0417-4
- MIBI-TOF reproducibility paper: https://www.nature.com/articles/s41374-022-00778-8
- high-dimensional tissue imaging with MIBI review: https://pmc.ncbi.nlm.nih.gov/articles/PMC11244641/
- ST-Net paper: https://www.nature.com/articles/s41551-020-0578-x
- Hist2ST paper: https://academic.oup.com/bib/article/23/5/bbac297/6645485
- spatial expression prediction benchmark: https://www.nature.com/articles/s41467-025-56618-y
- STimage paper: https://www.nature.com/articles/s41467-026-68487-0
- FineST paper: https://www.nature.com/articles/s41467-026-70528-7
- virtual multiplex IF example: https://arxiv.org/abs/2505.10294
