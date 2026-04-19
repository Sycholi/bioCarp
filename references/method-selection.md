# Method Selection

## Bulk Differential Expression

### limma

Use when:

- matrix is already normalized or microarray-like
- design is moderately complex
- speed matters

Strengths:

- mature and stable
- flexible design matrices
- strong for microarray and transformed expression data

### edgeR

Use when:

- count data are available
- library-size differences matter
- sample size is modest

Strengths:

- strong count-model foundation
- reliable dispersion modeling

### DESeq2

Use when:

- count matrix is clean
- a familiar publication-standard workflow is preferred
- shrinkage and straightforward result reporting matter

Strengths:

- highly recognizable in biomedical papers
- clean result objects

## Single-Cell Integration

### Seurat Plus Harmony

Use when:

- the user wants alignment with the existing local codebase
- metadata-aware batch correction is enough
- figure production must stay close to the user's established style

Strengths:

- dominant pattern in `~/r_repo`
- easy handoff to downstream Seurat modules

### scVI

Use when:

- batch structure is strong
- cross-dataset integration is difficult
- Python interop is acceptable

Strengths:

- strong latent integration
- robust for heterogeneous cohorts

Cost:

- more environment complexity than Seurat plus Harmony

## Cell Annotation

### Manual Marker Annotation

Use when:

- the biological question depends on fine-grained interpretation
- the user wants transparent oncology-specific labeling

Strengths:

- strongest alignment with the user's library
- easy to defend with marker panels and plots

### CellTypist or Similar Reference Tools

Use when:

- a first-pass label transfer is needed
- large or noisy datasets need rapid annotation

Best practice:

- treat automated labels as draft labels
- verify with marker expression before final naming

## Pathway and Enrichment

### clusterProfiler

Use when:

- the goal is ORA, KEGG, GO, or GSEA in a familiar R workflow

Strengths:

- dominant in the user's library
- integrates well with `org.Hs.eg.db`, `org.Mm.eg.db`, and enrichplot

### fgsea

Use when:

- preranked enrichment should be fast
- many gene sets must be evaluated

### GseaVis or Custom GSEA Plotting

Use when:

- the final manuscript figure needs refined enrichment presentation

## Trajectory and State Transition

### Monocle3

Use when:

- a trajectory backbone and pseudotime visualization are needed

### slingshot plus tradeSeq

Use when:

- lineage-aware statistics matter
- smooth expression trends across pseudotime are needed

### CytoTRACE

Use when:

- the question is differentiation potential rather than a full lineage graph

## Cell-Cell Communication

### CellChat

Use when:

- pathway-level ligand-receptor structure and network visualization are needed
- compatibility with the user's current codebase matters

Strengths:

- already embedded in the local library

### NicheNet or Other Prior-Knowledge Tools

Use when:

- the goal is prioritizing ligand-to-target programs rather than only plotting networks

## CNV and Malignancy Inference

### infercnv

Use when:

- transcriptome-based CNV inference is sufficient
- reference normal cells are available

### fastCNV or Related Faster Tools

Use when:

- quicker iteration is needed
- the user already has a compatible local workflow

## TCR and BCR

### scRepertoire

Use when:

- clonotype integration with Seurat metadata is needed

### Startrac

Use when:

- tissue distribution, expansion, or transition metrics matter
- immune-ecology interpretation is central

## Survival and Cohort Balancing

### survival plus survminer

Use when:

- KM and Cox are the main clinical outputs

### MatchIt

Use when:

- observational imbalance materially affects the clinical comparison
- the design truly calls for matching

## Practical Rule

Prefer tools that satisfy all three conditions:

1. fit the biological question
2. match the data structure
3. stay close to the user's existing project style

Only switch to a newer or less familiar tool when it clearly improves scientific fit or robustness.
