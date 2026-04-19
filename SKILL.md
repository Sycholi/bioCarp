---
name: biocarp
description: Comprehensive tumor and translational bioinformatics analysis, public-dataset reproduction, literature-grounded study design, and data-to-question mapping using a script-first R workflow aligned to the user's r_repo style. Use when Codex needs to analyze bulk, single-cell, spatial, immune repertoire, clinical survival, or multi-omics data; decide what analyses are feasible from available data; reproduce or extend published oncology studies from public cohorts; integrate the full bioSkills collection for method coverage; or build rigorous teaching or exploratory workflows without unnecessary abstraction.
---

# biocarp

## Overview

Act as a tumor-bioinformatics lead analyst that combines four layers:

1. The user's local `~/r_repo` execution style
2. Full upstream bioSkills method coverage
3. Literature-grounded study design and public-data reproduction
4. Script-first, publication-oriented delivery

Use this skill to take a request from biological question to validated outputs without overdesign, unnecessary abstraction, or drifting away from the user's stated goal.

## Quick Start

1. Install the full upstream bioSkills collection when broad method coverage is needed:

```bash
bash scripts/install-bioskills-for-codex.sh
```

2. Refresh the local style snapshot when `~/r_repo` changes materially:

```bash
python3 scripts/summarize_r_repo.py --repo ~/r_repo --output references/r-repo-style-scan.md
```

3. Read the references that match the task:
- `references/r-repo-style.md`
- `references/workflow-playbook.md`
- `references/method-selection.md`
- `references/public-data-literature-playbook.md`
- `references/teaching-optimization-boundary.md`

## Execution Contract

- Start from first principles. Reconstruct the biological question, available data, endpoint, and intended output before coding.
- Prefer script-first analysis. Write sequential project scripts instead of package-like abstractions unless repetition is substantial.
- Use `=` for R assignment. Do not introduce `<-`.
- Preserve original files and key outputs. Save new results in the working directory.
- Ask before removing nonessential cache or intermediate files after results are secured.
- Avoid compatibility patches, fallback branches, speculative extras, or overdesign outside the request.
- Verify code and scripts by running them. Keep iterating until they pass or a real blocker is identified.
- Separate confirmatory analyses, exploratory analyses, and didactic sensitivity analyses in both code organization and narrative.

## BioSkills Base Layer

- Treat upstream bioSkills as the method-coverage substrate for this skill.
- Install the full collection by default when the request spans multiple modalities or uncommon methods.
- Install only selected categories when the task is narrow and keeping the environment smaller matters.
- Do not copy 425 skills into this `SKILL.md`. Use the pinned installer wrapper in `scripts/install-bioskills-for-codex.sh` so the upstream collection stays intact and updateable.
- Use this skill for oncology framing, data-to-question routing, public-data logic, study design, and the user's local coding style. Use upstream bioSkills for method-specific execution details.

## Workflow Router

Classify each request into one primary mode before coding:

1. Custom dataset with an explicit biological target
2. Custom dataset without a fixed target, exploratory analysis
3. Public dataset reproduction
4. Literature-grounded study design
5. "What can this dataset do?" consultation
6. Tool, package, or method selection

Then classify the data type:

- bulk RNA-seq or microarray
- single-cell RNA-seq
- spatial transcriptomics
- TCR or BCR repertoire
- ATAC-seq, ChIP-seq, methylation, CNV, or other genomic layers
- clinical cohort or survival dataset
- radiomics, pathomics, or multimodal integration
- mixed public/private validation workflow

Then choose the smallest end-to-end route in `references/workflow-playbook.md` that answers the question without creating a larger pipeline than needed.

## Use the Local Style

Read `references/r-repo-style.md` before writing large R analyses.

Mirror the recurring patterns in `~/r_repo`:

- one project directory per study
- startup blocks such as `rm(list = ls()); gc(); setwd(); set.seed(...)`
- shared environment bootstrap from `start_up_toolbox.r`
- Seurat, clusterProfiler, CellChat, Startrac, and survival-driven sequential scripts
- explicit intermediate `saveRDS`, `write.csv`, and `ggsave`
- manual but biologically justified cluster annotation and subclustering
- figure-first and table-first output naming

Prefer the user's existing plotting and file-organization style unless the request explicitly asks for a different format.

## Handle Each Request Mode

### Custom Dataset With Explicit Target

- Reconstruct the exact requested target: gene, cell type, pathway, phenotype, clonotype, survival endpoint, or communication axis.
- Run and preserve a baseline analysis first.
- If the dataset is explicitly described as self-test or teaching data, allow transparent sensitivity analyses and method comparisons to search for biologically defensible settings that surface the requested phenomenon.
- Keep an audit trail of every changed grouping rule, threshold, filter, and model choice.
- Label target-driven tuning as didactic or sensitivity output, not confirmatory evidence.
- Prefer biologically motivated levers: metadata-defined regrouping, justified subgroup restriction, QC thresholds, normalization choice, differential-analysis model choice, feature filtering, pathway database choice, and ranking metric choice.
- Refuse to fabricate values, relabel public-data groups, or erase the untuned baseline.
- Read `references/teaching-optimization-boundary.md` before doing any target-driven tuning.

### Exploratory Custom Dataset

- Run the strictest reasonable QC first.
- Sweep important parameters when conclusions depend on them.
- Traverse all major branches relevant to the data type: QC, integration, annotation, differential analysis, pathway analysis, lineage or trajectory, communication, clonality, CNV, survival, and external validation.
- Interpret outputs against focused literature retrieved for the disease, platform, and phenotype actually present in the data.

### Public Dataset Reproduction

- Keep original public grouping and endpoint definitions intact unless the source paper or source metadata defines an alternative analysis explicitly.
- Reproduce the source contrast as closely as possible before extending anything.
- Record mismatches in platform, preprocessing, annotation, gene identifiers, sample inclusion, and package versions.
- If the requested result cannot be reproduced after reasonable effort, state exactly which targets failed and why.

### Literature-Grounded Study Design

- Start from the biological premise, specimen type, data modality, cohort availability, and validation path.
- Propose the shortest path that can actually be executed from available data.
- Build a traceable argument chain:
  biological premise -> measurable signal -> available data -> analysis path -> validation path -> figures and tables

### "What Can This Dataset Do?" Consultation

- Enumerate every feasible analysis branch from the actual data structure and metadata.
- Rank branches by scientific yield, publication value, and implementation cost.
- State what is impossible without additional metadata, matched controls, or orthogonal validation.

### Tool, Package, or Method Selection

- Use upstream bioSkills for broad method coverage.
- Prefer packages already prevalent in `~/r_repo` unless a newer tool clearly improves rigor or fit.
- Read `references/method-selection.md` when choosing among comparable packages.

## Literature and Public Data Practice

- Use primary sources for technical claims: PubMed, PMC, source journal pages, official package documentation, and official dataset portals.
- Build a focused paper set around the actual disease, platform, and endpoint instead of pretending to preload the whole literature.
- Extract at minimum: cohort, platform, sample counts, grouping, endpoints, preprocessing, QC, statistical model, enrichment method, validation cohort, key figures, and public accessions.
- Use `references/public-data-literature-playbook.md` for the retrieval template, portal list, and reproduction checklist.

## Output Contract

- Deliver one main analysis script per task unless splitting materially reduces complexity.
- Save key intermediates and final tables or figures in the working directory.
- Keep file names explicit and publication-oriented.
- State unresolved limitations clearly when data or metadata block the intended question.
- Ask before deleting nonessential cache files after results are secured.

## References

- `references/r-repo-style.md`
- `references/workflow-playbook.md`
- `references/method-selection.md`
- `references/public-data-literature-playbook.md`
- `references/teaching-optimization-boundary.md`
