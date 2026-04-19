#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import pathlib
import re
from typing import Iterable


PACKAGE_PATTERN = re.compile(r"(?:library|require)\(([^)]+)\)")
FUNCTION_PATTERN = re.compile(r"^[A-Za-z0-9_.]+\s*(?:=|<-)\s*function\s*\(", re.MULTILINE)
EQ_ASSIGN_PATTERN = re.compile(r"^[A-Za-z0-9_.]+\s*=\s*", re.MULTILINE)
LEFT_ASSIGN_PATTERN = re.compile(r"<-")

WORKFLOW_TAGS = collections.OrderedDict(
    [
        ("single_cell", re.compile(r"\bSeurat\b|\bHarmony\b|\bCellTypist\b", re.IGNORECASE)),
        ("pathway", re.compile(r"clusterProfiler|fgsea|GSEA|enrich", re.IGNORECASE)),
        ("communication", re.compile(r"CellChat|ligand|receptor", re.IGNORECASE)),
        ("trajectory", re.compile(r"monocle|slingshot|tradeSeq|CytoTRACE", re.IGNORECASE)),
        ("clonotype", re.compile(r"scRepertoire|Startrac|TCR|BCR|clon", re.IGNORECASE)),
        ("cnv", re.compile(r"infercnv|fastCNV|CopyKAT|CNV", re.IGNORECASE)),
        ("survival", re.compile(r"survival|survminer|cox|KM_plot|matchit", re.IGNORECASE)),
        ("public_data", re.compile(r"GSE[0-9]{4,}|TCGA|GDC|GEOquery|ArrayExpress", re.IGNORECASE)),
    ]
)


def iter_r_files(root: pathlib.Path) -> Iterable[pathlib.Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() == ".r":
            yield path


def normalize_package(raw: str) -> str:
    cleaned = raw.strip().strip('"').strip("'")
    return cleaned


def summarize_repo(root: pathlib.Path) -> str:
    r_files = list(iter_r_files(root))
    package_counts: collections.Counter[str] = collections.Counter()
    workflow_counts: collections.Counter[str] = collections.Counter()
    eq_assign = 0
    left_assign = 0
    function_defs = 0
    project_counts: collections.Counter[str] = collections.Counter()

    file_sizes: list[tuple[int, pathlib.Path]] = []

    for path in r_files:
      text = path.read_text(encoding="utf-8", errors="ignore")
      rel_path = path.relative_to(root)
      project_name = rel_path.parts[0] if len(rel_path.parts) > 1 else rel_path.name
      project_counts[project_name] += 1
      file_sizes.append((len(text.splitlines()), rel_path))

      for match in PACKAGE_PATTERN.findall(text):
          package_counts[normalize_package(match)] += 1

      function_defs += len(FUNCTION_PATTERN.findall(text))
      eq_assign += len(EQ_ASSIGN_PATTERN.findall(text))
      left_assign += len(LEFT_ASSIGN_PATTERN.findall(text))

      for tag, pattern in WORKFLOW_TAGS.items():
          if pattern.search(text):
              workflow_counts[tag] += 1

    lines = []
    lines.append("# R Repo Style Scan")
    lines.append("")
    lines.append(f"Scanned root: `{root}`")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append(f"- R files: {len(r_files)}")
    lines.append(f"- Top-level project buckets: {len(project_counts)}")
    lines.append(f"- Function definitions: {function_defs}")
    lines.append(f"- Top-level `=` assignments: {eq_assign}")
    lines.append(f"- `<-` occurrences: {left_assign}")
    lines.append("")
    lines.append("## Top Packages")
    lines.append("")
    for package, count in package_counts.most_common(20):
        lines.append(f"- {package}: {count}")
    lines.append("")
    lines.append("## Workflow Tag Coverage")
    lines.append("")
    for tag, count in workflow_counts.items():
        lines.append(f"- {tag}: {count}")
    lines.append("")
    lines.append("## Largest Scripts By Line Count")
    lines.append("")
    for line_count, rel_path in sorted(file_sizes, reverse=True)[:15]:
        lines.append(f"- {rel_path}: {line_count}")
    lines.append("")
    lines.append("## Top-Level Project File Counts")
    lines.append("")
    for project, count in project_counts.most_common(20):
        lines.append(f"- {project}: {count}")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize an r_repo style snapshot.")
    parser.add_argument("--repo", default="~/r_repo", help="Path to the R repository root")
    parser.add_argument("--output", help="Optional output markdown file")
    args = parser.parse_args()

    root = pathlib.Path(args.repo).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Repository path does not exist: {root}")

    summary = summarize_repo(root)

    if args.output:
        output_path = pathlib.Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(summary + "\n", encoding="utf-8")
    else:
        print(summary)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
