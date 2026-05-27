# Genetic Epidemiology

Use this file for GWAS, PheWAS, PRS, fine mapping, colocalization, TWAS, eQTL, pQTL, mQTL, xQTL, LDSC, genetic correlation, heritability, ancestry review, biobank analysis, and genotype-to-phenotype integration.

## Intake

Before implementation, verify:

- genotype format: PLINK bed, pgen, VCF, BCF, imputed dosage, BGEN, Hail MatrixTable, summary statistics, or QTL table
- phenotype type, ancestry, population structure, relatedness, sex, genotyping array, imputation panel, genome build, allele coding, and sample exclusions
- study type: GWAS, PheWAS, PRS, rare variant, gene-based test, fine mapping, colocalization, TWAS, MR handoff, or xQTL integration
- downstream question: risk prediction, causal evidence, functional prioritization, ancestry comparison, biomarker integration, or public cohort validation

## GWAS And PheWAS

Current route:

1. Run sample QC, variant QC, ancestry and relatedness review, sex check, missingness, heterozygosity, Hardy-Weinberg review, allele frequency, and imputation quality checks.
2. Use PLINK2, SAIGE, REGENIE, BOLT-LMM, GEMMA, GCTA, Hail, or SNPTEST according to outcome, relatedness, scale, and data format.
3. Use population structure adjustment and relatedness handling suited to the cohort.
4. For binary traits with imbalance, prefer methods designed for case-control imbalance when needed.
5. For PheWAS, control phenotype definitions, multiple testing, related outcomes, and code grouping.

Required figures:

- sample and variant QC flow
- ancestry PCA and relatedness plots
- missingness, MAF, HWE, imputation quality, and genomic inflation plots
- Manhattan, QQ, regional association, and locuszoom plots
- phenotype-wide association heatmap or volcano for PheWAS

## PRS And Risk Prediction

Current route:

1. Align genome build, alleles, ancestry, summary statistic source, base and target cohorts, and phenotype definition.
2. Use PRSice, LDpred2, lassosum2, PRS-CS, SBayesR, SCT, or PLINK scoring according to data and ancestry.
3. Split training, tuning, validation, and external validation at participant level.
4. Report discrimination, calibration, reclassification, decision curve, subgroup performance, and ancestry transportability.

Required figures:

- score distribution by group and ancestry
- performance across P-value thresholds or shrinkage parameters
- ROC, PR, calibration, and decision-curve plots
- quantile risk plots and subgroup performance plots

## Fine Mapping, Colocalization, And QTL Integration

Current route:

1. Harmonize alleles, genome build, LD reference, population ancestry, sample overlap, and locus windows.
2. Use coloc, susieR, FINEMAP, SuSiE, PolyFun, PAINTOR, CAVIAR, eCAVIAR, HyPrColoc, SMR, TWAS, FUSION, S-PrediXcan, MAGMA, or Pascal according to question.
3. For locus-level causal claims, check colocalization, fine-mapping credible sets, LD, and tissue relevance.
4. Integrate eQTL, pQTL, mQTL, sQTL, caQTL, chromatin, protein, metabolite, and single-cell evidence when available.

Required figures:

- locus and LD plot
- credible-set and posterior probability plot
- colocalization posterior summary
- eQTL or pQTL effect comparison
- TWAS or gene-based Manhattan plot
- multi-layer evidence matrix for prioritized genes

## Source Index

Last checked: 2026-05-28.

- PLINK 2: https://www.cog-genomics.org/plink/2.0/
- SAIGE: https://github.com/saigegit/SAIGE
- REGENIE: https://rgcgithub.github.io/regenie/
- BOLT-LMM: https://alkesgroup.broadinstitute.org/BOLT-LMM/
- Hail: https://hail.is/
- OpenGWAS: https://opengwas.io/
- TwoSampleMR: https://mrcieu.github.io/TwoSampleMR/
- coloc: https://cran.r-project.org/package=coloc
- susieR: https://stephenslab.github.io/susieR/
- FUSION TWAS: http://gusevlab.org/projects/fusion/
- MAGMA: https://cncr.nl/research/magma/
- PRSice: https://choishingwan.github.io/PRSice/
- LDpred2: https://privefl.github.io/bigsnpr/articles/LDpred2.html
- PRS-CS: https://github.com/getian107/PRScs
