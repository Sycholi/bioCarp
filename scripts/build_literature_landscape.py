#!/usr/bin/env python3

import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

MODALITY_PATTERNS = {
    "single-cell RNA-seq": [r"\bsingle[- ]cell\b", r"\bscRNA[- ]seq\b", r"\bsnRNA[- ]seq\b"],
    "spatial transcriptomics": [r"\bspatial transcript", r"\bvisium\b", r"\bstereo[- ]seq\b"],
    "bulk RNA-seq": [r"\brna[- ]seq\b", r"\btranscriptom"],
    "microarray": [r"\bmicroarray\b", r"\baffymetrix\b"],
    "ATAC-seq": [r"\bATAC[- ]seq\b", r"\bchromatin accessibility\b"],
    "TCR/BCR repertoire": [r"\bTCR\b", r"\bBCR\b", r"\bclonotype\b", r"\brepertoire\b"],
    "proteomics": [r"\bproteom", r"\bCPTAC\b"],
    "metagenomics": [r"\bmetagenom", r"\bmicrobiom", r"\b16s\b", r"\bshotgun\b", r"\bMAGs?\b"],
    "structural bioinformatics": [r"\bprotein structure\b", r"\balphafold\b", r"\bdocking\b", r"\bmolecular dynamics\b", r"\bvirtual screening\b"],
    "imaging": [r"\bradiomics\b", r"\bpathomics\b", r"\bwhole[- ]slide\b", r"\bWSI\b", r"\bimmunofluorescence\b", r"\bsegmentation\b", r"\bnnU[- ]?Net\b"],
}

METHOD_PATTERNS = {
    "Seurat": [r"\bseurat\b"],
    "Harmony": [r"\bharmony\b"],
    "DESeq2": [r"\bdeseq2\b"],
    "edgeR": [r"\bedger\b"],
    "limma": [r"\blimma\b", r"\bvoom\b"],
    "Monocle": [r"\bmonocle\b"],
    "slingshot": [r"\bslingshot\b"],
    "tradeSeq": [r"\btradeseq\b"],
    "CellChat": [r"\bcellchat\b"],
    "CellPhoneDB": [r"\bcellphonedb\b"],
    "NicheNet": [r"\bnichenet\b"],
    "inferCNV": [r"\binfercnv\b"],
    "CopyKAT": [r"\bcopykat\b"],
    "scRepertoire": [r"\bscrepertoire\b"],
    "Startrac": [r"\bstartrac\b"],
    "CIBERSORTx": [r"\bcibersortx\b", r"\bcibersort\b"],
    "MOFA2": [r"\bmofa2\b"],
    "QIIME2": [r"\bqiime ?2\b"],
    "DADA2": [r"\bdada2\b"],
    "Kraken2": [r"\bkraken ?2\b"],
    "MetaPhlAn": [r"\bmetaphlan\b"],
    "HUMAnN": [r"\bhumann\b"],
    "ANCOM-BC": [r"\bancom[- ]bc\b", r"\bancombc\b"],
    "MaAsLin2": [r"\bmaaslin ?2\b"],
    "AlphaFold": [r"\balphafold\b"],
    "AutoDock Vina": [r"\bvina\b", r"\bautodock\b"],
    "GNINA": [r"\bgnina\b"],
    "GROMACS": [r"\bgromacs\b"],
    "OpenMM": [r"\bopenmm\b"],
    "nnU-Net": [r"\bnnu[- ]?net\b", r"\bnnU[- ]?Net\b"],
    "MONAI": [r"\bmonai\b"],
    "Cellpose": [r"\bcellpose\b"],
    "StarDist": [r"\bstardist\b"],
}

ACCESSION_PATTERNS = {
    "GEO": r"\bGSE\d+\b",
    "SRA": r"\bSRP\d+\b",
    "BioProject": r"\bPRJ[DENA]{2}\d+\b",
    "ArrayExpress": r"\bE-MTAB-\d+\b",
    "EGA": r"\bEGAS\d+\b",
    "TCGA": r"\bTCGA\b",
    "CPTAC": r"\bCPTAC\b",
    "PDB": r"\bPDB\s*[A-Z0-9]{4}\b|\bPDB ID\b",
    "TCIA": r"\bTCIA\b",
}


def fetch_text(url, pause=0.34):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "biocarp-literature-landscape/1.0",
            "Accept": "application/json, text/xml, application/xml",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read().decode("utf-8")
    time.sleep(pause)
    return payload


def esearch(query, years, retmax, sort="relevance", email=None, api_key=None):
    current_year = dt.date.today().year
    start_year = current_year - years + 1
    dated_query = f'({query}) AND ("{start_year}/01/01"[Date - Publication] : "3000"[Date - Publication])'
    params = {
        "db": "pubmed",
        "retmode": "json",
        "sort": sort,
        "retmax": retmax,
        "term": dated_query,
        "usehistory": "n",
    }
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key
    url = f"{BASE}/esearch.fcgi?{urllib.parse.urlencode(params)}"
    payload = json.loads(fetch_text(url))
    result = payload["esearchresult"]
    return {
        "query": dated_query,
        "count": int(result.get("count", "0")),
        "ids": result.get("idlist", []),
        "start_year": start_year,
        "end_year": current_year,
        "sort": sort,
        "url": url,
    }


def chunked(items, size):
    for index in range(0, len(items), size):
        yield items[index:index + size]


def esummary(ids, email=None, api_key=None):
    rows = {}
    for batch in chunked(ids, 100):
        params = {
            "db": "pubmed",
            "retmode": "json",
            "id": ",".join(batch),
        }
        if email:
            params["email"] = email
        if api_key:
            params["api_key"] = api_key
        url = f"{BASE}/esummary.fcgi?{urllib.parse.urlencode(params)}"
        payload = json.loads(fetch_text(url))
        result = payload["result"]
        for pmid in batch:
            if pmid in result:
                rows[pmid] = result[pmid]
    return rows


def inner_text(node):
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def parse_year(article):
    for path in [
        ".//PubDate/Year",
        ".//ArticleDate/Year",
        ".//PubMedPubDate[@PubStatus='pubmed']/Year",
    ]:
        hit = article.find(path)
        if hit is not None and hit.text:
            return hit.text.strip()
    medline_date = article.findtext(".//PubDate/MedlineDate", default="").strip()
    match = re.search(r"(19|20)\d{2}", medline_date)
    return match.group(0) if match else ""


def efetch(ids, email=None, api_key=None):
    rows = {}
    for batch in chunked(ids, 50):
        params = {
            "db": "pubmed",
            "retmode": "xml",
            "id": ",".join(batch),
        }
        if email:
            params["email"] = email
        if api_key:
            params["api_key"] = api_key
        url = f"{BASE}/efetch.fcgi?{urllib.parse.urlencode(params)}"
        root = ET.fromstring(fetch_text(url))
        for article in root.findall(".//PubmedArticle"):
            pmid = article.findtext(".//MedlineCitation/PMID", default="").strip()
            article_title = inner_text(article.find(".//ArticleTitle"))
            abstract_blocks = [inner_text(node) for node in article.findall(".//Abstract/AbstractText")]
            abstract_text = "\n".join([block for block in abstract_blocks if block])
            journal = inner_text(article.find(".//Journal/Title"))
            journal_iso = inner_text(article.find(".//Journal/ISOAbbreviation"))
            year = parse_year(article)
            publication_types = sorted(
                {inner_text(node) for node in article.findall(".//PublicationType") if inner_text(node)}
            )
            article_ids = {}
            for article_id in article.findall("./PubmedData/ArticleIdList/ArticleId"):
                id_type = article_id.attrib.get("IdType", "").lower()
                if id_type and article_id.text:
                    article_ids[id_type] = article_id.text.strip()
            pmcid = article_ids.get("pmc", "")
            if pmcid and not pmcid.upper().startswith("PMC"):
                pmcid = f"PMC{pmcid}"
            authors = []
            for author in article.findall(".//Author"):
                last_name = author.findtext("LastName", default="").strip()
                initials = author.findtext("Initials", default="").strip()
                collective = author.findtext("CollectiveName", default="").strip()
                if collective:
                    authors.append(collective)
                elif last_name:
                    authors.append(f"{last_name} {initials}".strip())
            rows[pmid] = {
                "pmid": pmid,
                "title": article_title,
                "abstract": abstract_text,
                "journal": journal or journal_iso,
                "journal_iso": journal_iso,
                "year": year,
                "doi": article_ids.get("doi", ""),
                "pmcid": pmcid,
                "authors": "; ".join(authors[:8]),
                "publication_types": "; ".join(publication_types),
            }
    return rows


def detect_labels(text, pattern_map):
    lowered = text.lower()
    labels = []
    for label, patterns in pattern_map.items():
        if any(re.search(pattern, lowered, flags=re.IGNORECASE) for pattern in patterns):
            labels.append(label)
    return labels


def normalize_modalities(labels, text):
    label_set = set(labels)
    lowered = text.lower()
    if "single-cell RNA-seq" in label_set and "bulk RNA-seq" in label_set:
        if not re.search(r"\bbulk rna\b|\bbulk transcript", lowered):
            label_set.remove("bulk RNA-seq")
    ordered = [label for label in MODALITY_PATTERNS if label in label_set]
    return ordered


def extract_accessions(text):
    hits = defaultdict(set)
    for label, pattern in ACCESSION_PATTERNS.items():
        for match in re.findall(pattern, text, flags=re.IGNORECASE):
            hits[label].add(match)
    return {label: sorted(values) for label, values in hits.items()}


def summarize_counts(rows, field):
    counter = Counter()
    for row in rows:
        value = row.get(field, "")
        if value:
            counter[value] += 1
    return counter


def write_tsv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, query_info, rows, modality_counts, method_counts, accession_counts, year_counts):
    lines = []
    lines.append("# Literature Landscape")
    lines.append("")
    lines.append(f"- Query: `{query_info['query']}`")
    lines.append(f"- Year window: {query_info['start_year']} to {query_info['end_year']}")
    lines.append(f"- Sort mode: {query_info['sort']}")
    lines.append(f"- PubMed hits reported by ESearch: {query_info['count']}")
    lines.append(f"- Records retrieved into corpus: {len(rows)}")
    lines.append(f"- Search URL: `{query_info['url']}`")
    lines.append("")

    if year_counts:
        lines.append("## Year Distribution")
        lines.append("")
        lines.append("| Year | Papers |")
        lines.append("| --- | ---: |")
        for year, count in sorted(year_counts.items(), key=lambda item: item[0], reverse=True):
            lines.append(f"| {year} | {count} |")
        lines.append("")

    if modality_counts:
        lines.append("## Modality Signals")
        lines.append("")
        lines.append("| Modality | Papers |")
        lines.append("| --- | ---: |")
        for label, count in modality_counts.most_common():
            lines.append(f"| {label} | {count} |")
        lines.append("")

    if method_counts:
        lines.append("## Method Signals")
        lines.append("")
        lines.append("| Method | Papers |")
        lines.append("| --- | ---: |")
        for label, count in method_counts.most_common():
            lines.append(f"| {label} | {count} |")
        lines.append("")

    if accession_counts:
        lines.append("## Public Data Signals")
        lines.append("")
        lines.append("| Resource | Mentions |")
        lines.append("| --- | ---: |")
        for label, count in accession_counts.most_common():
            lines.append(f"| {label} | {count} |")
        lines.append("")

    lines.append("## Top Papers")
    lines.append("")
    lines.append("| Year | PMID | PMCID | Journal | Title |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in rows[:20]:
        title = row["title"].replace("|", "/")
        lines.append(
            f"| {row['year']} | {row['pmid']} | {row['pmcid']} | {row['journal'].replace('|', '/')} | {title} |"
        )
    lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- This summary is metadata-first. Read full text for anchor papers before making detailed preprocessing or statistical claims.")
    lines.append("- `full_text_priority` equals `pmcid_available` when a PMCID is present and should be read first.")
    lines.append("")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build a focused PubMed literature landscape for a bioinformatics question.")
    parser.add_argument("--query", required=True, help="PubMed query body without the year filter.")
    parser.add_argument("--years", type=int, default=10, help="Lookback window in years.")
    parser.add_argument("--retmax", type=int, default=60, help="Maximum number of PubMed records to retrieve.")
    parser.add_argument("--sort", choices=["relevance", "pub_date"], default="relevance", help="PubMed sort mode.")
    parser.add_argument("--email", default="", help="Optional email passed to NCBI E-utilities.")
    parser.add_argument("--api-key", default="", help="Optional NCBI API key.")
    parser.add_argument("--output", required=True, help="Output directory.")
    args = parser.parse_args()

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    query_info = esearch(
        args.query,
        args.years,
        args.retmax,
        args.sort,
        args.email or None,
        args.api_key or None,
    )
    if not query_info["ids"]:
        (output_dir / "literature_summary.md").write_text(
            "# Literature Landscape\n\nNo PubMed records matched the query.\n",
            encoding="utf-8",
        )
        with (output_dir / "literature_search.json").open("w", encoding="utf-8") as handle:
            json.dump(query_info, handle, indent=2, ensure_ascii=False)
        print(f"No PubMed records matched. Output: {output_dir}")
        return 0

    summary_rows = esummary(query_info["ids"], args.email or None, args.api_key or None)
    fetch_rows = efetch(query_info["ids"], args.email or None, args.api_key or None)

    rows = []
    for pmid in query_info["ids"]:
        merged = {"pmid": pmid}
        merged.update(fetch_rows.get(pmid, {}))
        merged["pubdate"] = summary_rows.get(pmid, {}).get("pubdate", "")
        merged["sortpubdate"] = summary_rows.get(pmid, {}).get("sortpubdate", "")
        merged["epubdate"] = summary_rows.get(pmid, {}).get("epubdate", "")
        merged["source"] = summary_rows.get(pmid, {}).get("source", "")
        merged["title"] = merged.get("title") or summary_rows.get(pmid, {}).get("title", "")
        merged["journal"] = merged.get("journal") or summary_rows.get(pmid, {}).get("fulljournalname", "")
        merged["year"] = merged.get("year") or summary_rows.get(pmid, {}).get("pubdate", "")[:4]

        combined_text = "\n".join([merged.get("title", ""), merged.get("abstract", "")])
        modalities = normalize_modalities(detect_labels(combined_text, MODALITY_PATTERNS), combined_text)
        methods = detect_labels(combined_text, METHOD_PATTERNS)
        accessions = extract_accessions(combined_text)

        merged["modalities"] = "; ".join(modalities)
        merged["methods_detected"] = "; ".join(methods)
        merged["accessions_detected"] = "; ".join(
            [f"{label}:{','.join(values)}" for label, values in sorted(accessions.items())]
        )
        merged["full_text_priority"] = "pmcid_available" if merged.get("pmcid") else "abstract_only"
        rows.append(merged)

    fieldnames = [
        "pmid",
        "pmcid",
        "doi",
        "year",
        "pubdate",
        "sortpubdate",
        "epubdate",
        "journal",
        "journal_iso",
        "source",
        "title",
        "authors",
        "publication_types",
        "modalities",
        "methods_detected",
        "accessions_detected",
        "full_text_priority",
        "abstract",
    ]
    write_tsv(output_dir / "literature_corpus.tsv", rows, fieldnames)

    modality_counts = Counter()
    method_counts = Counter()
    accession_counts = Counter()
    year_counts = summarize_counts(rows, "year")

    for row in rows:
        for label in [item.strip() for item in row.get("modalities", "").split(";") if item.strip()]:
            modality_counts[label] += 1
        for label in [item.strip() for item in row.get("methods_detected", "").split(";") if item.strip()]:
            method_counts[label] += 1
        accession_field = row.get("accessions_detected", "")
        if accession_field:
            for group in accession_field.split(";"):
                label = group.split(":", 1)[0].strip()
                if label:
                    accession_counts[label] += 1

    write_markdown(
        output_dir / "literature_summary.md",
        query_info,
        rows,
        modality_counts,
        method_counts,
        accession_counts,
        year_counts,
    )

    with (output_dir / "literature_search.json").open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "query_info": query_info,
                "modality_counts": modality_counts,
                "method_counts": method_counts,
                "accession_counts": accession_counts,
            },
            handle,
            indent=2,
            ensure_ascii=False,
            default=lambda value: dict(value) if isinstance(value, Counter) else value,
        )

    print(f"Wrote literature landscape to {output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
