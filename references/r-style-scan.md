# R Analysis Code Style Scan

This file is an abstracted style snapshot. It does not record local paths, private project names, or machine-specific structure.

## Snapshot

- script-first analysis style
- project-stage scripts preferred over package-like abstraction
- `=` preferred for new R assignments
- frequent use of saved intermediate objects
- final outputs saved as explicit tables and figures

## Common Package Layer

- tidyverse-style table handling
- Seurat and SingleCellExperiment-style object handling
- pathway and enrichment analysis packages
- cell-cell communication packages
- immune repertoire packages
- survival and clinical modeling packages
- reticulate or Python interop when required

## Workflow Tags

- single-cell integration and annotation
- lineage-specific subclustering
- public dataset harmonization
- pathway and enrichment analysis
- cell-cell communication
- clonotype and repertoire analysis
- CNV and malignancy inference
- clinical cohort and survival analysis

## Style Summary

- keep analysis scripts linear and auditable
- avoid unnecessary helper layers
- save intermediate objects after major steps
- keep metadata changes explicit
- keep biological annotation steps visible
- use direct object names
- output figures and tables with clear publication-oriented names
