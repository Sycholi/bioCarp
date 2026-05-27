# Tool Evaluation

Use this file whenever a requested tool, package, model, web service, database, or workflow is not already covered in the local references, or when a known tool has a new major version, new paper, new repository, or new failure pattern.

## New Tool Gate

Before using a new or unfamiliar tool:

1. Confirm accessibility:
   - exact name, official repository, paper, documentation, package page, license, release status, installation route, platform support, model checkpoint access, database access, and whether the tool is still maintained
2. Define purpose:
   - biological question, accepted input, required metadata, processing steps, output tables, output models, output figures, and expected runtime or hardware needs
3. Evaluate value:
   - publication venue, peer-review status, citations or adoption, benchmark design, competing tools, advantage over mature alternatives, visualization value, reliability, and known limitations
4. Check research fit:
   - study design, sample size, replicate structure, species, tissue, disease, platform, endpoint, validation route, and user-specific needs
5. Read primary guidance:
   - original paper, official tutorial, README, vignettes, example notebooks, issue tracker, release notes, forum discussions, and practical user reports
6. Run and validate:
   - install in an isolated or project-specific environment when possible
   - avoid changing an existing working environment unless the user explicitly approves
   - run the official example or a small project subset
   - record command, version, dependency versions, seed, hardware, runtime, warnings, and outputs
   - fix installation or code issues when feasible without breaking existing environments
7. Summarize:
   - write a Chinese note in project reports with accessibility, role, input, route, output, value, limitations, bugs, fixes, and whether the result is confirmatory or exploratory
   - update `references/method-updates.md` when the tool should affect future tasks
   - update the most specific reference file when the tool becomes part of a recurring route

## Evidence Levels

- Level 1: official documentation plus peer-reviewed paper, maintained code, examples, and runnable installation
- Level 2: peer-reviewed paper or strong documentation, code available, limited examples or moderate maintenance
- Level 3: preprint, code available, unclear maintenance or narrow examples
- Level 4: code-only or web-only tool with limited documentation
- Level 5: name only, broken link, unavailable code, proprietary access without documentation, or ambiguous identity

Use Level 1 or Level 2 tools for central conclusions when possible. Use Level 3 tools for exploration only unless independent validation is strong. Do not build a main conclusion on Level 4 or Level 5 tools.

## Comparison Rule

For every new tool, identify at least one mature alternative in the same method family.

Minimum comparison fields:

- method family
- input and output match
- maintenance status
- evidence level
- computational cost
- required figures
- expected scientific gain
- known failure modes

Use the new tool only when it improves fit, output quality, interpretability, scale, or scientific value for the current task.

## Bug And Environment Rule

When a tool fails:

1. Preserve the failed command, log, versions, input type, and traceback.
2. Search official issues, documentation, release notes, Bioconductor support, scverse discourse, GitHub discussions, Stack Overflow, Biostars, CSDN, and field-specific forums by exact error text.
3. Try fixes inside the same project-specific environment or a new isolated environment.
4. Do not upgrade or remove packages from an environment that already runs existing project analyses unless the user approves.
5. Record whether the fix changes scientific output.
6. Add recurring failures to `references/bug-log.md`.

## Output Standard

A new tool has not been accepted into an analysis until these files or sections are updated in the project:

- `工具部署记录.md`
- `工具问题记录.md` when errors, issues, or forum fixes were used
- `方法学说明.md`
- `图表清单.md`
- `图表解读.md`
- `参考文献与依据.md`
- `阶段报告.md`
