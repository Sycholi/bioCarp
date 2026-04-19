# Teaching Optimization Boundary

Use this file only when the requester explicitly states that a nonpublic custom dataset is for internal teaching, rehearsal, or method demonstration.

## Required Practice

- Preserve the untuned baseline analysis.
- Record every changed grouping rule, threshold, filter, and model choice.
- Label all tuned outputs as didactic, sensitivity, or teaching-oriented results.
- Keep raw data values unchanged.
- Keep public-dataset group labels unchanged.

## Allowed Levers For Didactic Sensitivity Analysis

- metadata-defined regrouping
- biologically justified subgroup restriction
- QC threshold sweeps
- normalization and differential-method comparison
- feature-filtering rules
- pathway-database choice
- ranking-metric choice

## Not Allowed

- fabricating values
- deleting inconvenient samples without a rule
- relabeling public-data groups to force a result
- erasing the untuned baseline
- presenting post hoc tuning as fixed confirmatory truth

## Reporting Rule

When tuned results are requested for teaching:

1. save the baseline result
2. save the tuned result
3. explain what changed
4. keep confirmatory and didactic language separate
