# Clinical Research

Use this file for medical study design, clinical trial planning, observational and real-world study planning, sample size, endpoint definition, protocol logic, statistical analysis plans, clinical prediction studies, diagnostic studies, implementation studies, health economics, patient-reported outcomes, safety analysis, and clinical reporting standards.

## Intake

Before implementation, verify:

- study purpose: efficacy, effectiveness, safety, dose finding, pharmacokinetics, pharmacodynamics, diagnostic accuracy, screening, prognosis, prediction, biomarker validation, feasibility, pilot work, external validation, implementation, quality improvement, health economics, surveillance, natural history, or evidence generation for regulation or clinical practice
- design family: interventional, observational, diagnostic, prognostic, prediction-model, implementation, health-services, health-economics, qualitative, mixed-methods, registry, real-world evidence, translational, or evidence-synthesis handoff
- design structure: parallel, single-group, controlled, multi-arm, factorial, crossover, cluster, stepped wedge, split-body, N-of-1, adaptive, sequential, master protocol, pragmatic, external-control, registry-based, decentralized, or hybrid
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
8. Use dynamic-treatment or optimization designs only when the treatment sequence, tailoring variables, re-randomization rule, and decision points are defined.
9. For diagnostic, screening, prognostic, or prediction-model studies, follow intended use, target population, index test or model, reference standard, prediction horizon, and clinical decision context.
10. For implementation, quality-improvement, device, digital-health, surgical, or behavioral studies, define the setting, intervention components, adoption or fidelity outcomes, learning curve, contamination risk, and feasibility endpoints.

## Design Taxonomy

Select from these design families before writing code or a protocol.

### Drug, biologic, device, surgical, behavioral, and digital-health trials

- phase 0 or exploratory clinical pharmacology: microdose, biomarker, pharmacokinetic, pharmacodynamic, mechanism, and assay-readiness designs
- first-in-human and phase I: 3+3, accelerated titration, continual reassessment method, modified toxicity probability interval, Bayesian optimal interval, escalation with overdose control, dose expansion, food-effect, drug-drug interaction, QT, and special-population designs
- phase Ib and early combination trials: dose escalation, dose expansion, safety run-in, interaction review, pharmacokinetic interaction, and early efficacy signal designs
- phase II: single-group activity screening, Simon two-stage, randomized phase II, selection or pick-the-winner, randomized discontinuation, futility, signal-seeking, biomarker-enriched, and proof-of-concept designs
- phase II/III and phase III: seamless, group sequential, superiority, noninferiority, equivalence, add-on, active-control, placebo-control, dose-ranging, multi-arm multi-stage, and confirmatory efficacy designs
- phase IV and post-authorization: post-marketing safety, comparative effectiveness, risk minimization, pregnancy or special-population registry, long-term extension, and pragmatic effectiveness designs
- device and procedure studies: feasibility, pivotal device, usability, learning-curve, operator effect, registry-based, single-arm performance goal, randomized device, and surgical innovation designs
- behavioral, rehabilitation, nutrition, public-health, and digital-health trials: complex intervention, factorial optimization, SMART, MOST, micro-randomized, stepped-care, remote or decentralized, wearable-sensor, and implementation-linked designs

### Randomization and allocation structures

- individually randomized parallel-group designs
- single-group, nonrandomized controlled, matched controlled, and historical-control designs
- multi-arm, multi-stage, factorial, fractional factorial, and platform randomization
- crossover, cluster crossover, split-mouth, split-body, paired-organ, and N-of-1 designs
- cluster randomized, stepped-wedge cluster randomized, cluster nonrandomized, and community intervention designs
- stratified, blocked, minimization, covariate-adaptive, response-adaptive, and Bayesian adaptive randomization
- expertise-based, preference, Zelen, wait-list, delayed-start, withdrawal, randomized discontinuation, and enrichment designs

### Adaptive, sequential, and master-protocol designs

- group sequential efficacy, futility, or safety monitoring
- blinded or unblinded sample-size re-estimation
- adaptive dose finding, adaptive enrichment, adaptive population selection, adaptive treatment selection, and adaptive randomization
- seamless phase I/II, phase II/III, biomarker-adaptive, and platform-adaptive designs
- basket, umbrella, platform, multi-arm multi-stage, rolling-arm, shared-control, and Bayesian borrowing designs
- SMART and dynamic treatment regimen trials with multiple treatment decision points
- micro-randomized trials for just-in-time adaptive interventions
- response-adaptive and Bayesian predictive-probability designs

### Observational, registry, and real-world study designs

- descriptive, cross-sectional, ecological, surveillance, and natural-history studies
- prospective, retrospective, ambidirectional, inception, exposure-defined, and disease-defined cohort studies
- case-control, nested case-control, case-cohort, density-sampled, incidence-density, and test-negative designs
- registry, EHR, claims, administrative database, pragmatic registry-based, post-authorization safety, and comparative effectiveness studies
- external-control, historical-control, synthetic-control, hybrid-control, and single-arm benchmark designs
- self-controlled case series, case-crossover, interrupted time series, difference-in-differences, regression discontinuity, instrumental-variable, and target trial emulation designs
- pharmacovigilance signal-detection, active surveillance, risk-management, and safety database studies

### Diagnostic, screening, prognostic, and prediction studies

- diagnostic accuracy, reader study, paired diagnostic, triage, screening, surveillance, and test-impact designs
- diagnostic case-control and cohort diagnostic designs with reference-standard review
- biomarker analytical validation, clinical validation, clinical utility, companion diagnostic, and enrichment-marker designs
- prognostic factor, prognostic model development, internal validation, external validation, model updating, impact, calibration, decision-curve, and clinical utility designs
- risk-score, dynamic prediction, imaging-model, omics-signature, AI model, and multimodal prediction studies

### Implementation, quality, health-services, and health-economics studies

- pilot, feasibility, acceptability, usability, workflow, recruitment, retention, and adherence studies
- effectiveness-implementation hybrid type 1, type 2, and type 3 studies
- quality-improvement, audit, interrupted time series, stepped-wedge implementation, controlled before-after, and policy evaluation designs
- health-services, comparative effectiveness, care-pathway, resource-use, and patient-preference studies
- cost-effectiveness, cost-utility, budget-impact, decision-tree, Markov, microsimulation, and cost-consequence analyses
- Delphi, consensus, survey, qualitative, mixed-methods, instrument development, and patient-reported outcome validation studies

### Translational and omics-linked clinical studies

- biomarker discovery, locked signature validation, analytical validation, clinical validation, and clinical utility studies
- specimen collection, pre-analytical variable, assay bridging, platform concordance, batch bridging, and external-laboratory validation studies
- pharmacogenomics, immune monitoring, minimal residual disease, liquid biopsy, imaging biomarker, and molecular tumor board studies
- multi-cohort public validation, retrospective-prospective validation, prospective-retrospective validation, and companion assay development

## Sample Size And Power

Current route:

1. State endpoint, scale, null value, alternative value, power, type I error, sidedness, allocation ratio, dropout, follow-up, and analysis set.
2. For single-arm binary endpoints, use exact binomial, Simon two-stage, Bayesian phase II, or precision-based sample size.
3. For controlled binary, continuous, count, ordinal, survival, repeated-measure, longitudinal, competing-risk, and recurrent-event endpoints, choose formulas or simulation according to endpoint and planned model.
4. For survival endpoints, specify median survival, hazard ratio, accrual, follow-up, dropout, event count, and interim looks.
5. For diagnostic accuracy, power sensitivity, specificity, AUC, paired design, and prevalence separately when needed.
6. For prediction models, use pmsampsize, shrinkage, outcome frequency, number of candidate predictors, expected performance, and validation design.
7. For noninferiority and equivalence, justify the margin, effect scale, active-control evidence, and analysis set.
8. For cluster, stepped-wedge, crossover, N-of-1, SMART, micro-randomized, and longitudinal designs, include correlation structure, periods, cluster size, repeated measures, carryover, tailoring variables, and missingness.
9. For adaptive, Bayesian, basket, umbrella, platform, and response-adaptive designs, run simulation and report operating characteristics.
10. For implementation and health-economic studies, include adoption, fidelity, reach, cost, utility, site, cluster, and time effects when relevant.
11. For high-dimensional omics studies, do not rely on generic sample size formulas alone. Use pilot variance, effect-size range, multiple testing, batch, and validation needs.

Primary tools:

- rpact, gsDesign, gsDesign2, clinfun, OneArmPhaseTwoStudy, ph2simon, BOIN, dfcrm, bcrm
- powerSurvEpi, powerMediation, pmsampsize, MKmisc, epiR, TrialSize, samplesize4surveys
- simtrial, simr, clusterPower, CRTsize, steppedwedge, longpower, powerlmm, Superpower
- randomizeR, blockrand, randomizr, DeclareDesign, simstudy, heemod, hesim, BCEA
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
- CONSORT extensions for adaptive, crossover, early phase, factorial, multi-arm, N-of-1, outcomes, nonpharmacologic treatment, abstracts, health equity, and other special trial contexts when applicable
- TIDieR for intervention description
- StaRI for implementation studies
- SQUIRE 2.0 for quality-improvement studies
- CHEERS 2022 for health-economic evaluations
- IDEAL for surgical and interventional innovation
- COREQ or SRQR for qualitative studies when qualitative methods are central
- STROBE, RECORD, STARD, TRIPOD+AI, PROBAST+AI, CONSORT-AI, and SPIRIT-AI should be selected according to actual design and model type

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
- CONSORT extensions: https://www.consort-spirit.org/extensions
- IDEAL recommendations: https://www.ideal-collaboration.net/the-ideal-framework/recommendations/
- SMART design review: https://pmc.ncbi.nlm.nih.gov/articles/PMC5963278/
- Micro-randomized trials: https://pmc.ncbi.nlm.nih.gov/articles/PMC4732571/
- Effectiveness-implementation hybrid designs: https://pmc.ncbi.nlm.nih.gov/articles/PMC3731143/
- TIDieR: https://www.equator-network.org/reporting-guidelines/tidier/
- StaRI: https://www.equator-network.org/reporting-guidelines/stari-statement/
- SQUIRE 2.0: https://pmc.ncbi.nlm.nih.gov/articles/PMC4625997/
- CHEERS 2022: https://www.bmj.com/content/376/bmj-2021-067975
