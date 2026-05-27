# Parameters

Use this file when threshold, normalization, integration strength, model setting, database choice, or software option can change the biological result.

## Parameter Contract

For every parameter-sensitive analysis:

1. record the default value, chosen value, package version, input object, and reason
2. state the expected effect on retained samples, cells, features, reads, peaks, peptides, metabolites, microbes, images, or events
3. run a focused sensitivity check when the conclusion depends on the parameter
4. keep the baseline result before tuning
5. report parameter effects in `方法学说明.md`, `图表清单.md`, and `阶段报告.md`

Required outputs:

- parameter decision table
- before-after count table
- sensitivity plot for central thresholds
- blocked parameter list when data are missing

## Single-Cell Parameters

Important settings:

- empty-droplet FDR, expected cell count, barcode rank threshold, minimum UMI, minimum genes, maximum genes, mitochondrial fraction, ribosomal fraction, hemoglobin fraction, stress score, cell-cycle regression, ambient correction strength, doublet expected rate, integration method, integration features, dimensions, neighbor number, clustering resolution, marker test, and min.pct or logFC thresholds

Expected effects:

- stricter QC removes damaged cells but may remove fragile tumor, stromal, plasma, neutrophil, or rare immune populations
- relaxed QC increases rare-cell retention but can retain debris, doublets, empty droplets, and ambient RNA
- aggressive ambient correction can remove true marker signal when contamination and endogenous expression are not separated
- high integration strength can reduce batch effects and also reduce real disease, tissue, or treatment differences
- clustering resolution changes subtype count and marker specificity; resolution must be checked with ROGUE, silhouette or ASW, marker coherence, and clustree-style stability

Required checks:

- threshold distributions by sample
- removed-cell composition
- unintegrated versus integrated embeddings
- iLISI, cLISI, kBET, ASW, graph connectivity, marker preservation
- cluster size, marker coherence, ROGUE, and reference-label agreement

## Trajectory, Velocity, And Communication Parameters

Important settings:

- trajectory cell subset, root node, terminal state, branch pruning, dimensional reduction, neighbor graph, smoothing, lineage number, pseudotime scaling
- velocity spliced and unspliced matrix source, filtering, moments, neighbors, dynamical model settings, latent time, confidence threshold
- communication cell grouping, minimum cells per group, ligand-receptor database, expression threshold, permutation count, spatial distance, pathway filter, and condition contrast

Expected effects:

- root choice can reverse pseudotime interpretation
- broad cell subsets can create artificial trajectories across unrelated lineages
- velocity on missing or incorrectly generated spliced and unspliced counts is invalid
- cell-group granularity changes communication networks; rare or poorly annotated groups can create unstable interactions
- ligand-receptor database choice changes reported pathways and should be recorded

Required checks:

- biological root and terminal evidence
- sample and condition density along pseudotime
- velocity confidence and phase portraits when supported
- communication abundance diagnostics, pathway contribution, and database note

## Bulk Expression And Enrichment Parameters

Important settings:

- low-count filter, normalization method, design formula, batch terms, paired design, contrasts, dispersion or voom trend, shrinkage method, gene ID mapping, ranking metric, gene-set database, background universe, multiple-testing method, and deconvolution reference

Expected effects:

- low-count filtering changes multiple-testing burden and weak-gene noise
- missing paired or batch terms can inflate group effects
- gene ID mapping changes enrichment, especially when symbols are duplicated or outdated
- background universe changes ORA results
- deconvolution references shape cell-type estimates and should match tissue and platform as closely as possible

Required checks:

- sample PCA or MDS before and after normalization
- mean-variance and dispersion diagnostics
- contrast design table
- enrichment database version and background table

## ATAC, ChIP, CUT&Tag, CUT&Run, And Methylation Parameters

Important settings:

- trimming, mapping quality, duplicate removal, blacklist filtering, fragment size, TSS enrichment, FRiP, peak caller, peak caller q value, narrow or broad peak setting, control input, consensus peak rule, IDR, window size, normalization, motif database, footprinting settings, methylation detection P value, probe filtering, beta or M value choice, coverage cutoff, and DMR smoothing

Expected effects:

- peak caller and q-value settings change accessible or bound regions
- duplicate handling differs across ATAC, ChIP, CUT&Tag, and low-input assays
- consensus peak rules affect differential accessibility or binding
- footprinting is sensitive to Tn5 bias and depth
- methylation probe filtering and platform manifest choice can change DMP and DMR results

Required checks:

- TSS, FRiP, fragment size, replicate concordance, IDR or correlation
- peak count and width distribution
- motif and footprint diagnostics
- methylation density, control probe, DMP and DMR diagnostics

## Variant, HLA, Antigen, And Immunopeptidomics Parameters

Important settings:

- reference genome, interval list, caller, tumor-normal status, allele fraction filter, depth, base quality, mapping quality, panel of normals, germline resource, strand filter, copy-number model, purity and ploidy, HLA caller, peptide length, binding threshold, expression filter, clonality filter, normal-tissue filter, MS search engine, enzyme, FDR, modification, and peptide-spectrum match threshold

Expected effects:

- tumor-only calls have higher false-positive risk without germline filtering
- low depth and low purity reduce variant sensitivity
- HLA caller and resolution affect antigen prediction
- peptide binding thresholds strongly change candidate count
- immunopeptidomics FDR and search settings change peptide evidence and motif quality

Required checks:

- variant QC and filtering summary
- HLA support and concordance when possible
- candidate peptide retention flow
- binding score, expression, clonality, and MS evidence plots

## Proteomics Parameters

Important settings:

- DDA, DIA, diaPASEF, TMT, LFQ, PRM, SRM, raw converter, search engine, spectral library, enzyme, missed cleavages, fixed and variable modifications, protein database, precursor and fragment tolerance, FDR, match-between-runs, normalization, batch correction, missing-value handling, protein grouping, and PTM localization probability

Expected effects:

- search database and FDR affect identification count
- match-between-runs can increase quantification and also propagate weak identifications
- TMT channel layout and reference channel affect group comparison
- imputation can create artificial separation when missingness is group-related
- PTM claims depend on site localization and peptide evidence

Required checks:

- identification counts, FDR, missingness, normalization, PCA, batch, channel balance, and imputation sensitivity
- peptide-to-protein and PTM-site evidence tables

## Metabolomics, Lipidomics, And Flux Parameters

Important settings:

- raw conversion, centroiding, peak picking, m/z tolerance, retention-time alignment, gap filling, blank filtering, pooled-QC correction, internal-standard normalization, batch correction, adduct grouping, isotope grouping, annotation library, MS/MS score, ion mode, lipid class rules, isotope correction, tracer purity, natural abundance correction, flux model, objective, constraints, and confidence interval settings

Expected effects:

- peak picking and alignment define the feature table and can change all downstream results
- blank filtering and pooled-QC correction reduce technical features but can remove low-abundance biology
- adduct and isotope grouping affect metabolite counts
- annotation confidence controls how strong pathway interpretation can be
- flux estimates depend on tracer design, time points, model structure, and fit quality

Required checks:

- total ion current or feature count QC
- blank and pooled-QC plots
- retention-time drift and batch plots
- annotation confidence table
- isotopologue distribution, flux fit, and uncertainty plots

## Metagenomics Parameters

Important settings:

- primer trimming, truncation length, expected error, chimera removal, host removal, contaminant filtering, database, classifier, confidence threshold, compositional method, rarefaction choice, normalization, PERMANOVA formula, MAG assembly k-mer, binning method, bin refinement, completeness, contamination, taxonomy database, and functional database

Expected effects:

- DADA2 truncation and expected error thresholds change ASV retention
- database choice changes taxonomy names and resolution
- host removal and contaminant filtering are central for low-biomass samples
- rarefaction can discard reads; compositional methods often fit differential abundance better
- MAG thresholds determine which genomes are biologically interpretable

Required checks:

- read retention, negative-control review, alpha and beta diversity, taxonomy database version, differential method note, MAG quality plots

## Clinical, Causal, And Evidence Parameters

Important settings:

- endpoint definition, time zero, censoring rule, analysis set, effect measure, alpha, power, sidedness, allocation ratio, historical benchmark, noninferiority margin, dropout, event rate, interim boundary, matching method, weighting method, trimming, positivity threshold, target trial eligibility, follow-up window, missing-data method, and risk-of-bias rule

Expected effects:

- time-zero mismatch can create immortal time bias
- cut-point optimization can overstate biomarker effects
- weighting and trimming change the target population
- sample-size assumptions control feasibility and operating characteristics
- meta-analysis model, effect scale, and heterogeneity method change pooled estimates

Required checks:

- endpoint and time-zero table
- sample-size assumptions and power curves
- baseline balance, weight distribution, effective sample size
- missingness and sensitivity plots
- forest, funnel, influence, and heterogeneity plots for evidence synthesis

## GWAS, PRS, And Genetic Epidemiology Parameters

Important settings:

- sample missingness, variant missingness, minor allele frequency, Hardy-Weinberg filter, relatedness, ancestry, imputation quality, phenotype model, principal components, kinship, LD pruning, genome-wide threshold, fine-mapping credible set, colocalization priors, PRS clumping, LD reference, threshold grid, and ancestry-matched validation

Expected effects:

- ancestry mismatch can distort association and PRS performance
- imputation quality and MAF filters change variant set and rare-variant reliability
- LD reference affects PRS, fine mapping, and colocalization
- phenotype definition and relatedness handling affect test calibration

Required checks:

- sample and variant QC, ancestry PCA, QQ, lambda or LDSC intercept, Manhattan, regional association, PRS calibration, and validation plots

## Imaging And Structural Parameters

Important settings:

- image resolution, resampling, color normalization, tile size, tissue mask, segmentation threshold, train-validation-test split, augmentation, scanner or center batch, radiomics bin width, docking protonation, ligand tautomer, receptor preparation, docking grid, exhaustiveness, scoring function, MD force field, water model, ion setting, timestep, equilibration, and simulation length

Expected effects:

- tile-level splitting can overstate model performance when patient-level split is required
- segmentation errors propagate into radiomics and spatial phenotype results
- docking grid and protonation change pose ranking
- short MD trajectories are mainly stability checks and need cautious interpretation

Required checks:

- patient-level split table
- segmentation overlay and error plots
- radiomics stability and scanner checks
- docking control, pose cluster, and MD diagnostic plots

## Source Discipline

Parameter choices must be checked against:

- official package documentation
- current package vignettes
- primary workflow papers
- disease-specific recent papers
- issue trackers when the option is version-sensitive

If package documentation and recent papers differ, record the difference and choose the route that fits the input data and study design.
