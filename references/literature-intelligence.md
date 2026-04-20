# Literature Intelligence

## Contents

1. When to use
2. Corpus construction contract
3. Query decomposition
4. What to extract from each paper
5. Writing-logic reconstruction
6. Public-data capture
7. Minimum deliverables

## When To Use

Read this file when the request asks for any of the following:

- literature-grounded study design
- what analyses are common in a disease or modality
- what data types and public cohorts are used in recent papers
- what figure logic and writing order are typical
- what method families dominate the last decade of papers

## Corpus Construction Contract

Do not answer from a vague impression of the literature.

Build a focused corpus around the actual question:

1. disease or histology
2. tissue or specimen type
3. modality
4. phenotype or endpoint
5. intervention or treatment context
6. validation context

Use the last 10 years by default. Backfill older papers only for canonical methods, landmark discovery cohorts, or indispensable biology.

Start with PubMed or PMC and then move to official accession portals and source-journal methods.

The first pass should be broad enough to map the field. The second pass should be narrow enough to support the exact design or analysis request.

## Query Decomposition

Break the question into a query grid:

- disease: hepatocellular carcinoma, colorectal cancer, glioblastoma, AML
- tissue: primary tumor, adjacent normal, metastatic lesion, PBMC, ascites
- modality: bulk RNA-seq, microarray, scRNA-seq, Visium, TCR-seq, ATAC-seq
- phenotype: response, relapse, grade, survival, metastasis, lineage state
- biology: macrophage, CAF, stemness, hypoxia, lipid remodeling, ferroptosis
- validation: TCGA, GEO, CPTAC, HPA, external single-cell cohort

Example query pattern:

`("hepatocellular carcinoma" OR HCC) AND ("single-cell" OR scRNA-seq) AND (macrophage OR myeloid) AND (response OR prognosis)`

## What To Extract From Each Paper

Extract these fields into a structured table:

- title
- PMID, PMCID, DOI
- year and journal
- disease
- sample type
- total sample count
- grouping and endpoint
- modality and platform
- preprocessing or alignment stack
- QC thresholds
- integration or batch-correction approach
- annotation strategy
- differential-analysis model
- pathway or signature strategy
- trajectory, communication, CNV, clonality, or survival modules
- validation cohort or orthogonal experiment
- accession numbers
- main-claim figure chain
- direct relevance to the user's request
- whether the extraction came from full text or abstract only

If a method-level detail is not visible in full text or supplement, label it as unknown rather than inferring it.

## Writing-Logic Reconstruction

For anchor papers, reconstruct the logic progression rather than only the result:

1. why the biological question matters
2. what cohort and assay can observe it
3. how the discovery signal is isolated
4. how the signal is translated into mechanisms
5. how the mechanism is validated
6. how the final figure order supports the claim

Typical oncology paper chains:

- bulk discovery -> external cohort validation -> mechanistic single-cell refinement
- single-cell discovery -> trajectory or communication -> public cohort validation
- tumor microenvironment state discovery -> clinical association -> wet-lab validation
- public meta-analysis -> self-test cohort extension -> mechanistic follow-up

When writing study design or Results sections, mirror the logic chain that best matches the available data rather than copying a generic paper template.

## Public-Data Capture

From each relevant paper, capture every reusable accession or portal record:

- GEO or ArrayExpress accession
- SRA or ENA project
- GDC or TCGA cohort
- CPTAC cohort
- cBioPortal study
- EGA accession when controlled access matters
- HPA or GTEx resource used for validation

Also capture:

- whether processed objects are provided
- whether sample annotations are complete
- whether response or survival metadata are available
- whether raw counts, TPM, FASTQ, or matrices are available

## Minimum Deliverables

Every literature-grounded task should leave behind:

1. a machine-readable corpus table
2. a compact markdown summary
3. a list of anchor papers read in full text
4. a list of reusable public datasets
5. a final statement translating literature into the chosen analysis route
