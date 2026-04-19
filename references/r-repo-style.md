# R Repo Style

## Snapshot

This summary reflects a scan of `~/r_repo` on 2026-04-19.

- 138 R scripts detected across 27 project buckets
- 3051 top-level `=` assignments detected
- 127 `<-` assignments still present in legacy files
- 14 explicit function definitions detected
- Default style is script-first, project-local, and output-driven rather than package-like

Refresh the machine-generated scan with:

```bash
python3 scripts/summarize_r_repo.py --repo ~/r_repo --output references/r-repo-style-scan.md
```

## Dominant Startup Pattern

Repeated startup blocks look like:

```r
rm(list = ls()); gc(); setwd("~/r_repo/project"); set.seed(23112647)
source("~/r_repo/start_up_toolbox.r")
```

Common traits:

- load many packages from one shared bootstrap file
- switch into one study directory immediately
- set a fixed seed once
- rely on explicit file paths inside the project directory

## Common Package Layer

Most frequent packages in the scan:

- tidyverse
- clusterProfiler
- Seurat
- Startrac
- org.Hs.eg.db
- magrittr
- decontX
- reticulate
- org.Mm.eg.db
- enrichplot
- CellChat
- harmony
- survminer
- survival
- SingleCellExperiment

Interpret this as a bias toward immune-oncology single-cell analysis with strong pathway, communication, clonality, and survival components.

## Recurring Workflow Shapes

### Single-Cell Integration and Annotation

Representative files:

- `start_up_toolbox.r`
- `HSS_proj/hss_proj_script_1.r`
- `USP14/script.r`
- `zhangzemin/2.standard pipeline.r`

Recurring pattern:

1. Read multiple `rds` objects or per-batch objects
2. Standardize metadata fields manually
3. Merge objects
4. Normalize, find variable features, scale, run PCA
5. Integrate with Harmony or related methods
6. Run UMAP and neighbors
7. Cluster
8. Annotate with marker-driven `DotPlot`, `FeaturePlot`, and manual renaming
9. Save intermediate objects with `saveRDS`

### Subclustering and Lineage-Specific Deep Dive

Representative files:

- `HSS_proj/hss_proj_script_1.r`
- `TACE_HCC/TACE_HCC_Script.R`
- `XSZ_CD36_CAF/XSZ_CD36_CAF.r`

Recurring pattern:

- subset one lineage
- rerun normalization and integration locally
- recluster at a smaller resolution
- annotate with lineage-specific markers
- derive biologically named subtypes
- compare groups, tissues, or responses inside the lineage

### Public Dataset Harmonization

Representative files:

- `PanNK_PD-1/script_new.r`
- `TCGA/LIHC/script.R`
- `NKlac/GSE206325/GSE206325_script.r`

Recurring pattern:

- read many public datasets into one workspace
- standardize metadata fields such as tissue, time, response, patient, dataset
- keep dataset identity explicit
- remove incompatible assays or slots when needed
- export harmonized objects to `rds`, `h5seurat`, or `h5ad`

### Downstream Immune-Oncology Modules

Representative files:

- `repository/cellchat_process.r`
- `enrichment.r`
- `scvi_boost.r`
- `cache.r`

Recurring modules:

- CellChat communication analysis
- clusterProfiler or fgsea enrichment
- clonotype and tissue-distribution analysis with Startrac or scRepertoire
- CNV inference with infercnv or fastCNV
- scVI integration through `reticulate`

### Clinical Cohort and Survival Analysis

Representative files:

- `SBRT/analyze.r`

Recurring pattern:

- read one spreadsheet or table
- define continuous and factor variables explicitly
- build Table 1 style summaries
- run Kaplan-Meier plots
- run Cox analysis
- use propensity-score matching when the study design calls for it
- save every table and plot directly to CSV or PDF

## Writing Style to Preserve

- Prefer linear scripts over reusable APIs.
- Avoid unnecessary functions unless repetition is substantial.
- Save intermediate objects aggressively.
- Keep filenames explicit and publication-oriented.
- Use direct object names such as `seu`, `markers`, `matched_data`, `cellchat`.
- Accept some manual, visible, biologically motivated curation steps.
- Use `=` for new R assignments even though legacy files still contain some `<-`.

## Output Style to Preserve

- `saveRDS` for stateful intermediate objects
- `write.csv` for final tables and marker lists
- `ggsave` for publication-ready PDF outputs
- project-local files instead of central output registries
- separate script files for requested figures when needed

## Practical Consequence For This Skill

When writing new analyses for this user:

- choose the shortest script that solves the whole task
- avoid turning everything into helper functions
- preserve the user's heavy use of saved intermediates
- keep the analysis traceable from raw object to final figure
- prefer familiar package stacks before introducing new ones
