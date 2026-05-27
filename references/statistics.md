# Statistics And Visualization

Use this file for downstream statistics, figure construction, model diagnostics, report tables, publication plots, and cross-module visual grammar.

## Intake

Before implementation, verify:

- unit of inference: sample, patient, animal, cell, spot, region, clone, peptide, metabolite, microbe, structure, image, or slide
- design: paired, repeated measures, nested, batch-balanced, longitudinal, survival, case-control, perturbation, dose-response, or multi-cohort
- endpoint type: binary, continuous, count, compositional, time-to-event, ordinal, high-dimensional, image-level, spatial, or trajectory-based
- required figure type, journal-style need, color palette, statistical annotation, and data table source

## Statistical Modeling

Current route:

1. Preserve the correct biological unit. Do not use cell-level rows as independent samples when the design is patient-level.
2. Use linear models, generalized linear models, mixed models, survival models, permutation tests, rank tests, compositional methods, or resampling according to endpoint and design.
3. Adjust multiple testing with method appropriate to the family of tests.
4. Report effect size, confidence interval, adjusted P value, sample count, and model formula whenever possible.
5. Check assumptions and model diagnostics before interpreting significance.
6. For clinical study planning, sample size, target trial emulation, external controls, evidence synthesis, or genetic epidemiology, read the specific companion file before modeling.

Primary tools:

- base R, stats, broom, car, emmeans, multcomp, lme4, glmmTMB, nlme, geepack
- survival, survminer, rms, riskRegression, pec, timeROC, pROC, glmnet
- vegan, ANCOMBC, ALDEx2, MaAsLin2, compositions, propr for compositional data
- metafor for meta-analysis
- coin, exactRankTests, permutation, boot, rsample for nonparametric or resampling routes

Companion files for design-specific statistics:

- `clinical-research.md` for single-arm, two-arm, sample size, power, SAP, safety, PRO, and reporting
- `causal-inference.md` for target trial emulation, real-world evidence, matching, weighting, and sensitivity analysis
- `clinical-data.md` for EHR, registry, REDCap, OMOP, FHIR, CDISC, and terminology data quality
- `evidence-synthesis.md` for meta-analysis, network meta-analysis, MR, and pharmacovigilance
- `genetic-epidemiology.md` for GWAS, PRS, fine mapping, colocalization, QTL, and biobank statistics
- `parameters.md` for parameter effects and sensitivity checks

Required figures:

- design and sample-count summary
- model diagnostics, residual plots, QQ plots, calibration, confusion matrix, ROC or PR, and decision-curve plots when relevant
- effect-size forest plots
- subgroup and sensitivity plots
- correlation, concordance, Bland-Altman, and agreement plots when comparing assays or methods
- sample-size, power, operating-characteristic, balance, weight, target-trial, forest, funnel, Manhattan, QQ, regional, PRS, and colocalization plots when those companion routes are used

## Visualization Tools

Primary tools:

- ggplot2, ggpubr, ggrepel, ggforce, ggbeeswarm, ggdist, ggalluvial, ggraph, tidygraph
- ComplexHeatmap, pheatmap, circlize, EnrichedHeatmap
- EnhancedVolcano, ggrepel, ggpointdensity
- UpSetR, ComplexUpset
- patchwork, cowplot, gridExtra, multipanelfigure
- ggtree, treeio, ape, phytools for phylogenetic and tree plots
- Gviz, karyoploteR, ggbio, plotgardener, trackViewer, IGV snapshots for genome tracks
- maftools, ComplexHeatmap oncoPrint, circlize for cancer mutation plots
- plotly, htmlwidgets, DT, reactable when interactive review is useful

Required checks:

1. Confirm the plotted table matches the statistical table.
2. Confirm group order, labels, units, legends, color scales, and missing-value handling.
3. Confirm figure dimensions, aspect ratio, resolution, label clipping, panel balance, and text size.
4. Use consistent palettes across related figures.
5. Save source table and plotting code for every final figure.

## Reporting Tables

Primary tools:

- data.table, dplyr, tidyr, readr, vroom, arrow, duckdb
- gt, gtsummary, flextable, kableExtra, DT, reactable
- renv, sessioninfo, pak, BiocManager, conda-lock when environment tables are needed

Required outputs:

- sample table after filtering
- analysis manifest
- figure manifest
- method table with package versions
- source and reference table
- blocked-analysis table when data are insufficient

## Source Index

Last checked: 2026-05-28.

- ggplot2: https://ggplot2.tidyverse.org/
- ComplexHeatmap: https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html
- ComplexHeatmap reference: https://jokergoo.github.io/ComplexHeatmap-reference/book/
- EnhancedVolcano: https://bioconductor.org/packages/release/bioc/html/EnhancedVolcano.html
- UpSetR paper: https://academic.oup.com/bioinformatics/article/33/18/2938/3884387
- ggtree: https://yulab-smu.top/treedata-book/
- riskRegression: https://cran.r-project.org/package=riskRegression
- pec: https://cran.r-project.org/package=pec
- metafor: https://www.metafor-project.org/
- lme4: https://cran.r-project.org/package=lme4
- glmmTMB: https://cran.r-project.org/package=glmmTMB
- rpact: https://www.rpact.org/
- TrialEmulation: https://causal-lda.r-universe.dev/TrialEmulation/TrialEmulation.pdf
- PLINK2: https://www.cog-genomics.org/plink/2.0/
