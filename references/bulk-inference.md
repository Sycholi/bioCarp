# Bulk Functional Inference

Use this file when `index.md` selects bulk RNA-seq, microarray, proteomics, phosphoproteomics, methylation-derived signatures, or pseudobulk analyses that need transcription factor activity, pathway activity, kinase activity, immune or stromal deconvolution, cell-state projection, co-expression modules, signature scoring, or phenotype interpretation.

Before implementation, verify the current package documentation, reference database version, species support, identifier requirements, input scale, and recent disease-specific publication practice.

## General Route

1. Start from a clean expression matrix and sample metadata.
2. Record whether the matrix is raw counts, TPM, FPKM, CPM, logCPM, variance-stabilized counts, normalized microarray intensity, proteomics, or phosphoproteomics.
3. Harmonize gene identifiers. Preserve a mapping table and list dropped or duplicated genes.
4. Check sample outliers, batch, phenotype balance, and covariates before any activity inference.
5. Decide whether the biological question needs differential expression, single-sample scoring, regulator activity, pathway activity, deconvolution, co-expression, or external signature projection.
6. Run more than one method family when a major claim depends on a latent inferred quantity such as TF activity or immune abundance.
7. Validate direction against known markers, source literature, independent cohorts, single-cell data, spatial data, or perturbation evidence when available.

Required figures:

- input matrix QC, PCA or MDS, sample correlation heatmap, and batch or phenotype overlay
- method-specific score heatmap, score distribution, and group comparison plot
- volcano or ranked-statistic plot when scores are tested between groups
- sample-level association with clinical variables, phenotype, or survival when relevant
- concordance plot across methods or databases when multiple inference routes are used
- validation plot in external cohort or orthogonal modality when available

## Transcription Factor Activity

Use when the result should infer regulator activity rather than TF mRNA abundance.

Current route:

1. Use differential statistics or normalized expression as input according to the method.
2. Use curated TF-target networks such as DoRothEA, CollecTRI, OmniPath, TRRUST, MSigDB TF targets, or package-specific regulons.
3. Use `decoupleR`, `dorothea`, `viper`, `VIPER`, `metaVIPER`, or related methods according to data type and resource.
4. Prefer signed and weighted networks when available.
5. Filter low-confidence regulons only after checking whether the disease or species needs broader coverage.
6. Check whether inferred activity matches target genes, perturbation data, chromatin evidence, or known biology.

Required figures:

- TF activity heatmap across samples
- top TF activity volcano or ranked plot
- TF-target network or target-gene heatmap for key TFs
- activity versus TF expression scatter plot to show why expression alone is insufficient
- regulon coverage and confidence summary
- cross-resource concordance plot when multiple TF resources are used

Common sources:

- decoupleR TF activity vignette
- DoRothEA
- CollecTRI via OmniPath
- VIPER and metaVIPER documentation
- disease-specific papers using TF activity inference

## Pathway And Signaling Activity

Use when the question asks whether a pathway is active, suppressed, or associated with phenotype at sample level.

Current route:

1. Choose single-sample scoring, enrichment of DE statistics, or model-based activity inference according to the question.
2. Use `decoupleR` with PROGENy, MSigDB, Reactome, KEGG, Hallmark, OmniPath, or curated pathway resources.
3. Use `GSVA`, ssGSEA, `singscore`, `fgsea`, `clusterProfiler`, `ReactomePA`, `gage`, `pathview`, or `sparrow` when they fit the input and output.
4. Keep gene set version fixed. Record pathway database, release date, organism, and gene ID type.
5. Distinguish pathway activity, enrichment, and expression of member genes. These are not the same claim.

Required figures:

- pathway activity heatmap
- group comparison boxplot or violin plot for selected pathways
- pathway score volcano or ranked plot
- GSEA running-score plots for core pathways
- ridge, dot, bar, cnet, emap, or term-similarity plots for enriched terms
- pathway diagram with `pathview` or equivalent when mechanistic interpretation needs gene-level placement

Common sources:

- decoupleR pathway activity vignette
- PROGENy documentation
- GSVA Bioconductor vignette
- singscore Bioconductor vignette
- clusterProfiler book

## Kinase, Phosphoprotein, And Proteomics Activity

Use when proteomics or phosphoproteomics is available, or when transcriptomics is being used only as weak support for signaling hypotheses.

Current route:

1. Confirm whether the input is transcript, protein, phosphosite, or PTM-level data.
2. Use kinase-substrate databases and methods through `decoupleR`, OmniPath, PTM-SEA, KSEA, or package-specific resources when supported.
3. Keep phosphosite identifiers, protein identifiers, species, and localization clear.
4. Treat kinase activity from transcriptomics as indirect unless supported by phosphoproteomics or perturbation data.

Required figures:

- phosphosite or protein QC and missingness
- kinase activity heatmap and ranked plot
- substrate heatmap for key kinases
- pathway or network plot for major signaling modules
- comparison against transcriptomic pathway activity when both layers exist

## Immune, Stromal, And Cell-Type Deconvolution

Use when bulk tissue composition matters.

Current route:

1. Decide whether the goal is immune score, stromal score, absolute fraction, relative fraction, cell-type score, or cell-type-specific expression.
2. Use marker-score methods and deconvolution methods with their outputs interpreted separately.
3. Use `immunedeconv` for unified access to TIMER, xCell, MCP-counter, EPIC, quanTIseq, and CIBERSORT when license and input support it.
4. Use CIBERSORTx when custom signature matrices, cell fractions, or high-resolution mode are needed and the web or Docker workflow is feasible.
5. Use `MuSiC`, `BisqueRNA`, `SCDC`, BayesPrism, BSEQ-sc, DWLS, or related tools when a single-cell reference is available and compatible.
6. Use ESTIMATE or similar tumor purity and stromal or immune scoring methods when broad tumor microenvironment scores are sufficient.
7. Check expected cell types, species, tissue, platform, log scale, non-log scale, and gene symbols before running.
8. Benchmark or compare multiple methods when the claim depends on composition.

Required figures:

- deconvolution input QC and signature-gene coverage
- cell fraction or score stacked bar plot by sample
- heatmap of cell-type abundance or scores
- group comparison plots for major cell types
- method-concordance heatmap or correlation plot across deconvolution methods
- cell-type marker validation plot
- association with purity, clinical variables, survival, or pathway scores when relevant

Common sources:

- CIBERSORTx documentation
- immunedeconv documentation
- xCell, MCP-counter, EPIC, quanTIseq, TIMER, ESTIMATE papers
- MuSiC, BisqueRNA, BayesPrism, SCDC, DWLS documentation
- recent tissue-specific deconvolution benchmarking papers

## Co-Expression, Modules, And Network Analysis

Use when the question asks for coordinated gene programs, modules, hub genes, phenotype-linked networks, or sample-level latent structure.

Current route:

1. Use enough samples for stable network inference. Avoid WGCNA on very small cohorts unless explicitly exploratory.
2. Filter low-expression and low-variance genes before network construction.
3. Choose signed or unsigned network, soft power, dynamic tree cut, merge threshold, and module size based on diagnostics.
4. Relate module eigengenes to phenotype, cell composition, pathway activity, and survival where relevant.
5. Do not force known genes into a module by tuning parameters to fit a desired result.

Required figures:

- sample dendrogram and outlier plot
- soft-threshold power plot
- gene dendrogram and module color plot
- module eigengene correlation heatmap
- module-trait correlation heatmap
- hub-gene network or kME versus gene-significance plot
- enrichment plot for key modules

Common sources:

- WGCNA documentation
- hdWGCNA documentation when single-cell or pseudobulk module analysis is needed
- recent disease-specific WGCNA papers only when they report reproducible parameter choices

## Publication Practice

When using bulk inference in a manuscript-oriented analysis:

1. State that inferred activities and deconvolved proportions are computational estimates.
2. Report package versions, database versions, gene sets, confidence cutoffs, and input transformations.
3. Show both global summary plots and selected mechanism plots.
4. Compare at least two independent signals when making strong claims, for example TF activity plus target-gene expression, deconvolution plus marker genes, pathway activity plus GSEA.
5. Avoid claiming direct cell abundance or protein activity from bulk RNA-seq without validation.
6. Use single-cell, spatial, IHC, flow cytometry, perturbation data, or external cohorts to support high-value claims.

## Source Index

Last checked: 2026-05-27.

- decoupleR Bioconductor package: https://www.bioconductor.org/packages/release/bioc/html/decoupleR.html
- decoupleR pathway activity in bulk RNA-seq: https://bioconductor.org/packages/release/bioc/vignettes/decoupleR/inst/doc/pw_bk.html
- decoupleR transcription factor activity in bulk RNA-seq: https://bioc.r-universe.dev/articles/decoupleR/tf_bk.html
- decoupleR paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC9710656/
- CollecTRI via OmniPathR: https://r.omnipathdb.org/reference/collectri.html
- decoupler OmniPath resources: https://decoupler.readthedocs.io/en/latest/api/op.html
- decoupler bulk enrichment tutorial: https://decoupler.readthedocs.io/en/latest/notebooks/bulk/rna.html
- DoRothEA and PROGENy benchmarking: https://pmc.ncbi.nlm.nih.gov/articles/PMC7017576/
- GSVA vignette: https://www.bioconductor.org/packages/release/bioc/vignettes/GSVA/inst/doc/GSVA.html
- singscore package: https://www.bioconductor.org/packages/release/bioc/html/singscore.html
- immunedeconv documentation: https://omnideconv.org/immunedeconv/articles/immunedeconv.html
- immunedeconv paper: https://pubmed.ncbi.nlm.nih.gov/32124323/
- CIBERSORTx: https://cibersortx.stanford.edu/
- MuSiC tutorial: https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/bulk-music/tutorial.html
- GSVA single-sample method documentation: https://master.bioconductor.org/packages/release/bioc/vignettes/GSVA/inst/doc/GSVA.html
- WGCNA module eigengene documentation: https://rdrr.io/cran/WGCNA/man/moduleEigengenes.html
