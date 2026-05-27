# Learning

Use this file to record user level, user habits, recurring analysis choices, encountered errors, tool bugs, version changes, new workflows, and new literature ideas.

User level and user habits are provisional references. They are not fixed facts. Reassess them at the start of every task because another person may use the same account or the same user may change task type, experience level, or preference.

## User Level Assessment

At the start of an analysis, infer the user's likely technical level from the current request:

- beginner: unclear data type, confused terminology, impossible grouping, missing endpoint, asking for a result without knowing required input, or using a method name incorrectly
- intermediate: knows the data type and broad method but may miss assumptions, figures, metadata, validation, or package limitations
- experienced: gives data structure, endpoint, contrast, metadata, method preference, and expected outputs

If the user appears to be a beginner:

1. State the incorrect or risky part directly and politely.
2. Explain why it is incorrect in concrete terms.
3. Propose a corrected analysis route.
4. Suggest suitable tools, data types, public datasets, and validation methods.
5. Explain the role of each suggested tool in plain Chinese.
6. Avoid assuming the user knows available tools or standard workflows.

If the user's requested method does not fit the data, say so clearly and give a feasible replacement.

## Proactive Method Suggestions

When the research idea would benefit from tools or data the user did not mention, actively suggest them.

Suggest methods when they improve:

- data quality control
- annotation reliability
- statistical validity
- external validation
- public-data reuse
- disease-specific interpretation
- figure completeness
- reproducibility of the final result

For each suggested method, explain:

- what data it requires
- what question it answers
- what output it produces
- why it is suitable for the current task
- what limitation or assumption should be checked

## Local Learning Records

Maintain learning records in the skill reference directory and in project reports. Treat user-level and preference records as hints only.

Skill-level records:

- `references/user-profile.md`: provisional user preferences, naming habits, output style, common project structure, preferred tools, recurring restrictions
- `references/bug-log.md`: tool errors, versions, symptoms, cause, fix, whether the fix changes analysis output
- `references/method-updates.md`: newly observed tool versions, new workflows, new papers, new datasets, and added local guidance

Project-level records:

- `分析状态.md`: current project state
- `工具问题记录.md`: project-specific tool bugs and fixes
- `方法学说明.md`: methods actually used
- `参考文献与依据.md`: literature and documentation used
- `阶段报告.md`: stage-level conclusion and limitations

Do not record private secrets, tokens, passwords, controlled-access credentials, or unnecessary personal information.

## Bug Learning Rule

When an error or bug appears:

1. Save the exact command, package version, input object type, error text, and system context.
2. Search official documentation, GitHub issues, package forums, Bioconductor Support, Stack Overflow, Biostars, scverse discourse, and CSDN when useful.
3. Record the cause if found.
4. Record the fix, workaround, version pin, or reason the issue remains unresolved.
5. State whether the fix changes the scientific result.
6. Update `references/bug-log.md` when the issue may recur.
7. Use this record in later analyses before rerunning the same tool.

## Method Update Rule

When a new tool version, new workflow, new documentation, new public dataset, or new literature idea is encountered:

1. Verify the source from official documentation, primary paper, repository, or dataset portal.
2. Record date, source, tool or paper name, relevant method change, input requirements, output, and limitation.
3. Update the most specific local reference file when the change affects future analysis.
4. Update `references/method-updates.md` with a short Chinese note.
5. If the change conflicts with an older local rule, keep the older rule only as historical context and state which route should be used now.

## User Habit Learning Rule

Record recurring user preferences when they affect future analysis. Apply them only when they fit the current request.

- preferred language and file naming
- preferred R style
- preferred output directory structure
- favored tools or package families
- repeated analysis goals
- repeated reporting requirements
- repeated constraints such as preserving original files or asking before deleting caches

Use these preferences in later tasks only as reference. Re-check the current request before applying them.
