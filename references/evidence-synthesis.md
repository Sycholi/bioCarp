# Evidence Synthesis

Use this file for systematic reviews, scoping reviews, meta-analysis, network meta-analysis, diagnostic meta-analysis, prognostic meta-analysis, Mendelian randomization, colocalization-linked evidence review, pharmacovigilance, and guideline evidence summaries.

## Intake

Before implementation, verify:

- review question: intervention, diagnostic, prognostic, exposure, biomarker, omics, method benchmark, safety, pharmacovigilance, or genetic causality
- framework: PICO, PECO, PICOS, PICOTS, SPIDER, or method-review question
- study types, databases, date range, language, inclusion criteria, exclusion criteria, outcome definitions, and extraction fields
- whether quantitative synthesis is appropriate
- risk of bias tool, certainty framework, and reporting guideline

## Systematic Review And Meta-Analysis

Current route:

1. Write the review question, eligibility criteria, database search, screening rule, extraction template, and risk-of-bias plan before extracting results.
2. Use PRISMA 2020 for reporting.
3. Use RoB 2 for randomized trials, ROBINS-I for nonrandomized intervention studies, QUADAS-2 for diagnostic accuracy, PROBAST+AI for prediction models, ROBIS for reviews, and AMSTAR 2 for review quality when appropriate.
4. Use fixed-effect, random-effects, multilevel, robust variance, Bayesian, or narrative synthesis according to heterogeneity and data structure.
5. Use network meta-analysis only when transitivity, consistency, and network geometry are defensible.
6. Use publication bias, small-study effect, influence, leave-one-out, and subgroup analyses when supported.

Primary tools:

- revtools, litsearchr, RISmed, rentrez, easyPubMed, Rayyan export, Zotero export, ASReview
- metafor, meta, netmeta, gemtc, BUGSnet, bayesmeta, dmetar, robvis, metadat, mada, diagmeta
- PRISMA2020, DiagrammeR, ggplot2, forestplot, clubSandwich

Required figures:

- PRISMA flow diagram
- search and screening summary
- risk-of-bias traffic light and summary
- forest plot, funnel plot, influence plot, Baujat plot, leave-one-out plot
- GRADE or certainty table when needed
- network plot, league table, rank plot, and inconsistency plots for network meta-analysis
- diagnostic SROC, sensitivity-specificity forest, and threshold plots for diagnostic meta-analysis

## Mendelian Randomization And Genetic Evidence

Current route:

1. Define exposure, outcome, ancestry, sample overlap, instrument source, clumping rule, and harmonization rule.
2. Check instrumental variable assumptions.
3. Use IVW, MR-Egger, weighted median, weighted mode, MR-PRESSO, radial MR, multivariable MR, Steiger filtering, and leave-one-out sensitivity when suitable.
4. Add colocalization or fine-mapping when exposure and outcome signals are in the same locus.
5. Avoid causal language when instruments are weak, pleiotropy is strong, sample overlap is uncontrolled, ancestry is mismatched, or colocalization is absent for locus-specific claims.

Primary tools:

- OpenGWAS, TwoSampleMR, MendelianRandomization, MR-PRESSO, RadialMR, MVMR, MRlap, coloc, susieR, gwasglue, ieugwasr, PLINK, LDlinkR

Required figures:

- instrument selection flow
- SNP-exposure and SNP-outcome association plots
- MR scatter, forest, funnel, leave-one-out, and radial plots
- heterogeneity and pleiotropy diagnostics
- colocalization posterior plot and locus plot when used

## Pharmacovigilance And Safety Signal Detection

Current route:

1. Define product, event, MedDRA term level, comparator, time window, duplicate handling, and reporting period.
2. Use spontaneous-reporting data for signal detection, not incidence estimation.
3. Use disproportionality metrics such as reporting odds ratio, proportional reporting ratio, information component, empirical Bayes geometric mean, and Bayesian shrinkage when appropriate.
4. Review label, known safety profile, confounding by indication, stimulated reporting, missing denominators, and duplicate reports before interpretation.
5. Use EHR, registry, claims, or trial data for incidence or risk estimation when available.

Primary resources and tools:

- FAERS, OpenFDA, VigiBase when access exists, EudraVigilance, MedDRA, CTCAE
- openFDA API, faers, PhViD, pharmacovigilance, AE reporting tools, OMOP safety packages

Required figures:

- report flow and deduplication summary
- event frequency by year, sex, age, seriousness, and reporter type
- disproportionality volcano or signal plot
- product-event heatmap
- known-versus-new safety signal table

## Source Index

Last checked: 2026-05-28.

- PRISMA 2020: https://www.prisma-statement.org/prisma-2020-statement
- RoB 2: https://methods.cochrane.org/risk-bias-2
- ROBINS-I: https://methods.cochrane.org/robins-i
- STARD and QUADAS resources: https://www.equator-network.org/reporting-guidelines/stard/
- TRIPOD+AI: https://www.bmj.com/content/385/bmj.q902
- metafor: https://www.metafor-project.org/
- netmeta: https://cran.r-project.org/package=netmeta
- robvis: https://mcguinlu.shinyapps.io/robvis/
- OpenGWAS: https://opengwas.io/
- TwoSampleMR: https://mrcieu.github.io/TwoSampleMR/
- MendelianRandomization: https://pmc.ncbi.nlm.nih.gov/articles/PMC5510723/
- openFDA FAERS: https://open.fda.gov/apis/drug/event/
