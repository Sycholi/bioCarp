# Causal Inference

Use this file for observational comparative effectiveness, target trial emulation, real-world evidence, external controls, propensity scores, weighting, matching, marginal structural models, g-methods, instrumental variables, negative controls, difference-in-differences, self-controlled designs, and causal machine learning.

## Intake

Before implementation, verify:

- clinical question, treatment strategies, comparator, eligibility criteria, time zero, assignment rule, follow-up, outcome, censoring, and causal contrast
- data source: EHR, registry, claims, trial extension, external control, administrative data, disease cohort, biobank, OMOP, or linked omics-clinical data
- exposure timing, outcome timing, baseline adjustment variables, time-varying treatment, time-varying confounding, competing events, missingness, and measurement process
- whether the goal is causal effect estimation, prediction, association, external control construction, sensitivity analysis, or hypothesis generation

## Target Trial Emulation

Current route:

1. Specify the target trial protocol before extracting observational data.
2. Define eligibility criteria, treatment strategies, treatment assignment, time zero, follow-up, outcome, causal contrast, analysis plan, and sensitivity analyses.
3. Align eligibility, treatment assignment, and follow-up start. This prevents immortal time and related design biases.
4. Use clone-censor-weight, sequential target trial emulation, or landmark design when treatment can start over time.
5. Check positivity, exchangeability, consistency, measurement quality, and missingness.
6. Report how each target trial element maps to observed data.

Primary tools:

- TrialEmulation, survival, data.table, WeightIt, MatchIt, cobalt, ipw, survey, SuperLearner, tmle, ltmle, drtmle, grf
- OHDSI CohortMethod, PatientLevelPrediction, SelfControlledCaseSeries, EvidenceSynthesis, ATLAS, FeatureExtraction when data use OMOP

Required figures:

- target trial protocol table
- flow from source population to analytic cohort
- treatment initiation and time-zero alignment plot
- follow-up and censoring summary
- covariate balance plot before and after design adjustment
- weighted or matched survival, risk, or outcome plots
- sensitivity analysis plots for design choices and assumptions

## Observational Comparative Effectiveness

Current route:

1. Draw or describe a causal diagram before selecting adjustment variables.
2. Define target population and effect measure.
3. Use matching, weighting, stratification, regression adjustment, doubly robust estimation, TMLE, or g-formula according to data structure.
4. For multiple treatments, use generalized propensity scores, overlap weighting, multinomial models, or multi-arm methods.
5. Use time-varying methods when treatment, confounding, or censoring changes during follow-up.
6. Use negative controls, falsification endpoints, E-values, tipping-point analysis, and quantitative bias analysis for sensitivity.

Primary tools:

- dagitty, MatchIt, WeightIt, cobalt, optmatch, CBPS, twang, PSweight, survey, ipw, tmle, ltmle, drtmle, SuperLearner, grf, DoubleML, AIPW, causalweight, EValue, episensr, tipr

Required figures:

- DAG or variable role table
- propensity score overlap and weight distribution
- love plot and standardized mean difference plot
- effective sample size table
- outcome model diagnostics
- effect estimate forest plot
- E-value, tipping-point, negative-control, or bias-analysis plots when relevant

## External Controls And Real-World Evidence

Current route:

1. Use external controls when concurrent randomization is infeasible, unethical, or scientifically limited, and when external data can approximate the trial comparator.
2. Align eligibility, calendar time, treatment history, endpoint definition, assessment schedule, follow-up, and data completeness between trial and external controls.
3. Use patient-level matching, weighting, outcome modeling, Bayesian borrowing, commensurate priors, meta-analytic predictive priors, or hybrid control approaches when justified.
4. Quantify residual differences and sensitivity to unmeasured factors.
5. State that nonrandomized external controls have residual bias risk even after design adjustment.

Required figures:

- trial-versus-external data source comparison
- eligibility and attrition flow
- baseline balance before and after matching or weighting
- endpoint ascertainment and follow-up comparability plots
- primary effect estimate and sensitivity plots
- external control data quality and missingness report

## Quasi-Experimental And Self-Controlled Designs

Use when randomization is unavailable and the exposure process supports a design-based analysis.

Current route:

1. Use difference-in-differences when treated and comparison groups have credible pre-intervention trend comparability.
2. Use interrupted time series when intervention timing is defined and pre/post observations are sufficient.
3. Use regression discontinuity when assignment has a known cutoff with local comparability.
4. Use instrumental variables when a defensible instrument exists.
5. Use self-controlled case series or case-crossover for transient exposures and acute outcomes when assumptions fit.

Primary tools:

- did, fixest, CausalImpact, gsynth, Synth, rdd, ivreg, AER, ivtools, SelfControlledCaseSeries, survival, geepack

Required figures:

- pre-trend plot and event-time plot
- interrupted time-series plot with fitted segments
- discontinuity plot around threshold
- instrument balance and first-stage diagnostics
- self-controlled exposure-risk window plot
- placebo and falsification plots

## Source Index

Last checked: 2026-05-28.

- Target trial framework review: https://pmc.ncbi.nlm.nih.gov/articles/PMC11936718/
- JAMA target trial emulation: https://jamanetwork.com/journals/jama/fullarticle/2799678
- TARGET reporting statement: https://pmc.ncbi.nlm.nih.gov/articles/PMC13084563/
- FDA RWE program: https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
- FDA non-interventional RWE guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/real-world-evidence-considerations-regarding-non-interventional-studies-drug-and-biological-products
- FDA externally controlled trials guidance list: https://www.fda.gov/science-research/clinical-trials-and-human-subject-protection/clinical-trials-guidance-documents
- TrialEmulation package: https://causal-lda.r-universe.dev/TrialEmulation/TrialEmulation.pdf
- MatchIt: https://kosukeimai.github.io/MatchIt/
- WeightIt: https://ngreifer.github.io/WeightIt/
- cobalt: https://ngreifer.github.io/cobalt/
- EValue: https://cran.r-project.org/package=EValue
- OHDSI CohortMethod: https://ohdsi.r-universe.dev/CohortMethod/doc/manual.html
