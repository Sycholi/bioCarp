# Execution

Use this file for project control, sub-agent use, goal tracking, tool deployment, figure inspection, result interpretation, and phase documentation.

## Project Start Rule

At the beginning of every analysis:

1. Inspect the project directory, input files, previous outputs, existing scripts, and environment.
2. Reconstruct the original biological or clinical question from first principles.
3. Identify the actual data type, sample unit, grouping, endpoint, and missing metadata.
4. Plan each step with a clear purpose before implementation.
5. If the purpose, endpoint, grouping, or needed output cannot be determined from files and context, ask before continuing.

## Goal And Sub-Agent Control

Use goal capability when it is available and the user explicitly asks to create, track, resume, or complete a goal. If an active goal already exists, check its state before major work and update it only when the goal is genuinely complete or blocked.

Use sub-agents when the task is broad, multi-modal, time-consuming, or benefits from independent checks. Suitable sub-agent tasks include:

- literature and public-data scanning
- tool issue and installation review
- package documentation extraction
- figure manifest review
- independent result interpretation
- method comparison across tool families

Record every sub-agent assignment and result in the project notes. Do not delegate final scientific judgment; integrate and verify the result before reporting.

## Tool Deployment

For any real analysis, assume required tools should be installed or deployed when they are missing and installation is feasible.

Required practice:

1. Check whether the tool, package, reference database, model checkpoint, or command-line dependency already exists.
2. Install missing requirements in the project environment or a clearly named environment.
3. Prefer `renv`, `conda`, `mamba`, `pip`, `BiocManager`, Docker, Singularity, or Nextflow profiles according to the method.
4. Use GPU or multi-threading when the tool supports it and the machine can provide it.
5. Preserve Tailscale and Clash connectivity. Do not stop, restart, disable, or reconfigure those services during tool deployment.
6. Record installed tools, versions, installation commands, database or checkpoint versions, environment path, GPU or thread settings, and install time in `工具部署记录.md`.
7. If installation fails, record the exact command, error, attempted fix, and remaining blocker.

## Workspace Rule

Save task outputs and downloaded files in the working directory. Use clear subdirectories such as `数据`, `脚本`, `中间文件`, `结果表格`, `结果图片`, `报告`, `环境`, and `缓存` when the project size justifies them.

Preserve original files and key outputs. After the final result is secured, ask before removing nonessential caches or temporary files.

## Figure Inspection

Every generated figure must be checked before the analysis is considered usable.

For each figure, verify:

- file exists and is nonempty
- dimensions, length, width, and aspect ratio fit the plot type
- resolution is sufficient for review and manuscript use
- text, labels, legends, facets, and color bars are not clipped or overlapping
- axis limits, scales, group labels, sample labels, and ordering are correct
- colors are standard, readable, color-blind aware when possible, and consistent across related figures
- plot size is neither excessively small nor excessively large for the information density
- output is not blank, corrupted, duplicated, or visually inconsistent with the underlying table
- data ranges, group counts, sample numbers, and statistical annotations are plausible
- package warnings or failed layers did not remove important visual elements

If any figure fails inspection, revise code or plotting parameters and regenerate the figure. Repeat inspection until the figure is usable or a real data blocker is documented.

## Result Interpretation

For every figure, write a short Chinese interpretation that includes:

- what input data and method produced the figure
- what the figure shows
- what result is reliable
- what result is exploratory
- what abnormal pattern, batch effect, missing group, outlier, or failed assumption was checked
- what follow-up or validation is needed

Keep figure interpretation in `图表解读.md` or a module-specific Markdown file. Link each interpretation entry to the figure filename.

## Phase Documentation

Every analysis must produce Markdown documentation in the result directory. Explanation files and output figures must use UTF-8 Chinese filenames by default. Use ASCII filenames only when a real encoding problem appears, and record the Chinese-to-ASCII mapping in `文件名映射表.md`.

All explanation file content must be written in Chinese. Use concise scientific wording. Do not put instructions about how the file should be generated inside the file. Write the actual result, interpretation, methods, references, limitations, and next step.

Required files:

- `分析状态.md`: current question, data sources, completed steps, pending steps, blockers, important parameters, and next action
- `方法学说明.md`: software versions, package documentation, statistical methods, parameters, databases, model checkpoints, and command summaries
- `图表清单.md`: required figures, generated files, source justification, QC status, interpretation status, and blocked figures
- `图表解读.md`: per-figure result explanation and abnormality review
- `工具部署记录.md`: installed or configured tools, versions, commands, and environment paths
- `参考文献与依据.md`: papers, documentation, datasets, issue pages, and access dates used to justify the analysis
- `阶段报告.md`: phase-level result summary, interpretation, methods, limitations, and references
- `文件名映射表.md`: required only when encoding issues force ASCII filenames

When an analysis has multiple stages, update `分析状态.md` after each stage so the project can be resumed after context loss.

## Phase Completion Gate

A stage is complete only when all items below are satisfied:

1. scripts or notebooks run without unresolved errors
2. required tables and figures exist
3. every figure has passed inspection
4. every figure has interpretation
5. tool deployment and tool issues are recorded when applicable
6. methods and references are recorded
7. `阶段报告.md` includes result analysis, interpretation, methods, references, and remaining limitations

If any item fails, continue revising or record a real blocker with evidence.

## Evidence Rule

Use only real datasets, real tools, official documentation, current issue pages, and published literature. Citation summaries must match the source content. If only an abstract is available, mark the detail as abstract-only. If a claim needs full-text support, read the full text or record the limitation.
