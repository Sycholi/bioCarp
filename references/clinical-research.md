# Clinical Research

Use this file for medical study design, trial planning, sample size, endpoint definition, protocol logic, statistical analysis plans, clinical prediction studies, diagnostic studies, patient-reported outcomes, safety analysis, and clinical reporting standards.

## Intake

Before implementation, verify:

- study purpose: efficacy, effectiveness, safety, diagnostic accuracy, prognosis, biomarker validation, dose finding, feasibility, pilot work, external validation, or health economics
- design: single-arm, two-arm, multi-arm, randomized, nonrandomized, single-center, multicenter, cluster, crossover, stepped wedge, factorial, adaptive, basket, umbrella, platform, registry, external control, or pragmatic
- endpoint type: response, binary event, continuous outcome, count, time-to-event, recurrent event, competing risk, repeated measure, quality of life, safety, diagnostic accuracy, or composite endpoint
- population, inclusion and exclusion criteria, intervention, comparator, follow-up, visit schedule, missing data process, treatment switching, rescue therapy, and intercurrent events
- intended output: protocol shell, SAP, sample size calculation, simulation, final analysis, reporting checklist, or manuscript figure sequence

## Design Selection

Current route:

1. Define the clinical question before selecting a design.
2. Identify the estimand, endpoint, population, treatment strategies, intercurrent events, and summary measure before writing analysis code.
3. Use randomized two-arm or multi-arm designs when a concurrent control is feasible and ethically acceptable.
4. Use single-arm phase II designs when the goal is early activity screening, rare disease development, biomarker-defined oncology cohorts, or feasibility, and the endpoint has a defensible historical benchmark.
5. Use externally controlled or hybrid-controlled designs only when trial and external patients can be aligned on eligibility, calendar time, endpoint definition, follow-up start, treatment history, and measurement process.
6. Use noninferiority or equivalence only when the margin, active control evidence, assay sensitivity, and clinical context are defensible.
7. Use adaptive, group sequential, basket, umbrella, or platform designs only when interim decisions, multiplicity, operational control, and simulation are specified before data review.
8. For diagnostic or prognostic model studies, follow intended use, target population, index test or model, reference standard, prediction horizon, and clinical decision context.

## Common Designs

- single-arm phase I or phase II: exact binomial, Simon two-stage, Bayesian phase II, response, safety, feasibility, or futility designs
- randomized two-arm superiority: binary, continuous, count, survival, recurrent event, repeated measure, or quality-of-life endpoints
- noninferiority and equivalence: margin justification, constancy assumption, assay sensitivity, per-protocol and intention-to-treat analysis
- cluster and stepped-wedge trials: cluster size, intracluster correlation, time effects, contamination, mixed models, and cluster-level reporting
- crossover and N-of-1 trials: washout, period effect, carryover, within-person variability, and repeated-measure modeling
- factorial trials: interaction, main effects, treatment combinations, and multiplicity
- adaptive and group sequential trials: alpha spending, futility, sample size re-estimation, treatment selection, enrichment, and simulation
- master protocols: basket, umbrella, and platform trials with arm adding, arm stopping, shared controls, subgroup enrichment, and multiplicity
- diagnostic accuracy: sensitivity, specificity, PPV, NPV, AUC, calibration, indeterminate results, and reference-standard review
- clinical prediction: development, internal validation, external validation, model updating, calibration, discrimination, decision curve, and fairness checks

## Sample Size And Power

Current route:

1. State endpoint, scale, null value, alternative value, power, type I error, sidedness, allocation ratio, dropout, follow-up, and analysis set.
2. For single-arm binary endpoints, use exact binomial, Simon two-stage, Bayesian phase II, or precision-based sample size.
3. For two-arm binary, continuous, count, survival, and recurrent-event endpoints, choose formulas or simulation according to endpoint and planned model.
4. For survival endpoints, specify median survival, hazard ratio, accrual, follow-up, dropout, event count, and interim looks.
5. For diagnostic accuracy, power sensitivity, specificity, AUC, paired design, and prevalence separately when needed.
6. For prediction models, use pmsampsize, shrinkage, outcome frequency, number of candidate predictors, expected performance, and validation design.
7. For cluster designs, include intracluster correlation, number of clusters, cluster size variation, and time periods.
8. For high-dimensional omics studies, do not rely on generic sample size formulas alone. Use pilot variance, effect-size range, multiple testing, batch, and validation needs.
9. For complex adaptive designs, run simulation and report operating characteristics.

Primary tools:

- rpact, gsDesign, gsDesign2, clinfun, OneArmPhaseTwoStudy, ph2simon, BOIN, dfcrm, bcrm
- powerSurvEpi, powerMediation, pmsampsize, MKmisc, epiR, TrialSize, samplesize4surveys
- simtrial, simr, clusterPower, CRTsize, steppedwedge, longpower
- PASS, nQuery, EAST, SAS PROC POWER, and validated institutional tools when available

Required outputs:

- assumptions table
- sample size and event count table
- operating-characteristic table
- power curve or precision curve
- accrual and event timeline plot
- interim boundary plot for group sequential or adaptive trials
- dropout and missing-data sensitivity table
- simulation code and seed when simulation is used

## Analysis And Reporting

Current route:

1. Define analysis sets: full analysis, intention-to-treat, modified intention-to-treat, safety, per-protocol, biomarker-evaluable, and response-evaluable populations.
2. Write a concise SAP before final analysis when the task is confirmatory or protocol-like.
3. Align missing data, intercurrent events, treatment switching, and rescue therapy with the estimand.
4. Report baseline table, participant flow, endpoint summary, effect estimates, uncertainty, model diagnostics, and sensitivity analyses.
5. For safety, summarize exposure, adverse events, serious adverse events, adverse events of special interest, laboratory shifts, vital signs, and discontinuations.
6. For quality-of-life or patient-reported outcomes, define scoring, minimally important difference, missing data, and longitudinal model.
7. Use reporting guidelines selected by study design.

Required figures:

- study schema and participant flow
- baseline table and missingness plot
- primary endpoint plot and effect estimate plot
- Kaplan-Meier, cumulative incidence, recurrent event, longitudinal, or repeated-measure plots when endpoints require them
- forest plot, subgroup plot, sensitivity plot, and model diagnostics
- safety overview, AE by grade, AE by organ class, laboratory shift, exposure, and discontinuation plots
- sample-size, power, boundary, or simulation operating-characteristic plots when planning is requested

## Reporting Standards

Use according to design:

- CONSORT 2025 for randomized trials
- SPIRIT for trial protocols
- ICH E6(R3) for good clinical practice principles
- ICH E9(R1) for estimands and sensitivity analysis
- STROBE for observational studies
- RECORD for routinely collected health data
- STARD for diagnostic accuracy
- TRIPOD+AI for prediction models using regression or machine learning
- PROBAST+AI for quality and risk of bias assessment in prediction models
- CONSORT-AI and SPIRIT-AI for AI interventions in trials
- CONSORT extensions for cluster, noninferiority, pragmatic, pilot, harms, and patient-reported outcomes when applicable

## Source Index

Last checked: 2026-05-28.

- CONSORT 2025: https://www.bmj.com/content/389/bmj-2024-081123
- CONSORT 2025 explanation: https://www.bmj.com/content/389/bmj-2024-081124
- ICH E9(R1): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical
- ICH E6(R3): https://www.fda.gov/media/169090/download
- SPIRIT: https://www.spirit-statement.org/
- STROBE: https://www.strobe-statement.org/
- RECORD: https://www.record-statement.org/
- STARD: https://www.equator-network.org/reporting-guidelines/stard/
- TRIPOD+AI: https://www.bmj.com/content/385/bmj.q902
- PROBAST+AI: https://www.bmj.com/content/388/bmj-2024-082505
- rpact: https://www.rpact.org/
- clinfun ph2simon: https://search.r-project.org/CRAN/refmans/clinfun/html/ph2simon.html
- pmsampsize: https://cran.r-project.org/package=pmsampsize
