# R And Bioinformatics Python Style

## Purpose

This file stores the analysis-script style for R code and bioinformatics Python code. It must not expose local directory names, private project names, absolute paths, or machine-specific structure.

## Core Style

- Prefer linear, script-first analysis.
- Use one main script per analysis stage unless splitting improves clarity.
- Keep code readable from data loading to final figure.
- Use `=` for new R assignments.
- Set random seeds near the top of every R or bioinformatics Python analysis script.
- Avoid helper functions, classes, generic APIs, wrapper functions, and reusable pipeline frameworks for routine analysis steps.
- Use functions only for identical repeated plotting, export, or package-required callback blocks. Keep them short and local to the script.
- Run direct package calls in the visible analysis sequence so parameters, intermediate objects, and outputs are easy to audit.
- Keep manual biological curation visible and documented.
- Save intermediate objects when they mark meaningful analysis states.
- Save final tables and figures with clear names.

## Startup Pattern

Use an explicit startup block when writing R scripts:

```r
rm(list = ls())
gc()
set.seed(23112647)
```

Then load packages and set project paths in a clear, project-relative way. Avoid hard-coded private absolute paths in reusable scripts and reports.

Use an explicit startup block when writing bioinformatics Python scripts:

```python
import random
import numpy as np

random.seed(23112647)
np.random.seed(23112647)
```

If `torch`, `tensorflow`, `jax`, `scanpy`, `scvi-tools`, or another package has its own seed control, set it in the same startup block and record the value.

## Package Pattern

Common analysis stacks include:

- tidyverse-style table handling
- Seurat or SingleCellExperiment for single-cell analysis
- Harmony, RPCA, scVI, or similar integration methods when justified
- clusterProfiler, fgsea, enrichplot, or related enrichment tools
- CellChat, LIANA, NicheNet, or related communication tools
- scRepertoire, Startrac, immunarch, scirpy, or Dandelion for repertoire work
- survival, survminer, rms, glmnet, or related clinical tools
- reticulate when Python tools are required from an R-first workflow
- Scanpy, AnnData, scvi-tools, Squidpy, pandas, numpy, scipy, scikit-learn, PyTorch, or package-specific Python stacks when the selected method requires Python

Choose tools by scientific fit first. Use familiar stacks when fit is comparable.

## Workflow Shape

Preferred sequence:

1. load data and metadata
2. check sample identity and grouping
3. run QC
4. normalize and model
5. save key intermediate objects
6. generate required tables
7. generate complete figure set
8. inspect figures
9. write Chinese interpretation and methods report

Do not convert this sequence into a general-purpose pipeline unless the task explicitly asks for reusable software. For ordinary data analysis, the script should document one complete run.

## Output Pattern

- Use `saveRDS` for stateful R objects.
- Use `write.csv` or `write.table` for final tables.
- Use `ggsave` or package-specific devices for figures.
- Prefer PDF for publication figures and PNG for quick review when useful.
- Use UTF-8 Chinese filenames for explanation files and output figures unless a real encoding problem appears.

## Refreshing The Abstract Style Scan

Refresh the machine-generated style scan only from representative scripts that are safe to summarize:

```bash
python3 scripts/summarize_code_style.py \
  --repo <analysis-script-directory> \
  --output references/r-style-scan.md
```

The generated scan must not include private absolute paths.
