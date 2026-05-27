# Variants

Use this file for germline variants, somatic variants, structural variants, copy number, HLA typing, variant annotation, tumor mutation burden, mutational signatures, clonality, and variant-to-antigen handoff.

## Intake

Before implementation, verify:

- sample type: tumor, normal, matched tumor-normal, germline cohort, WGS, WES, panel, RNA-seq, cfDNA, ctDNA, single-cell DNA, long-read DNA, or long-read RNA
- genome build, capture kit, panel BED, read group, duplicate or UMI design, tumor purity, ploidy, sex, contamination, and matched normal availability
- variant class: SNV, indel, MNV, CNV, SV, fusion, HLA, MSI, TMB, mutational signature, clonality, or allele-specific expression
- downstream need: MAF, VCF, clinical annotation, antigen peptide prediction, pathway interpretation, druggability, or cohort comparison

## Germline Short Variants

Current route:

1. Run raw QC, alignment, duplicate handling, base recalibration or workflow-equivalent steps, and coverage review.
2. Use `GATK HaplotypeCaller`, `DeepVariant`, `FreeBayes`, `bcftools`, or `Strelka2` according to design, platform, and validation expectation.
3. For cohorts, use GVCF or joint-calling route when applicable.
4. Filter variants with VQSR or hard filters according to cohort size and reference resources.
5. Annotate with VEP, ANNOVAR, SnpEff, ClinVar, gnomAD, dbSNP, COSMIC, ClinGen, OMIM, or disease-specific resources.

Required figures:

- coverage, insert size, duplication, mapping, contamination, and callability plots
- variant quality distributions, Ti/Tv, depth, allele balance, genotype quality, missingness, and per-sample variant counts
- PCA or relatedness plots when cohort structure matters
- annotation-class summary, pathogenicity summary, and gene-level burden plots when relevant

## Somatic Variants And Cancer Interpretation

Current route:

1. Prefer matched tumor-normal analysis when available.
2. Use `Mutect2`, `Strelka2`, `VarScan2`, `MuSE`, `SomaticSniper`, or documented consensus routes according to sample type and platform.
3. For tumor-only analysis, record the missing normal limitation and use population, panel-of-normals, and artifact resources carefully.
4. Annotate variants, convert to MAF when useful, and summarize drivers, TMB, MSI, signatures, pathways, clonality, and druggability.
5. Use RNA expression, protein expression, copy number, and clonality to prioritize variants for antigen or drug analysis.

Required figures:

- VAF distribution, depth distribution, filtered-versus-retained summary, and artifact filters
- oncoplot, lollipop, transition-transversion, rainfall or kataegis, TMB, MSI, and driver summary plots
- mutational signature exposure and reconstruction error plots
- cancer cell fraction, clonality, and phylogeny plots when supported
- treatment target or clinical actionability summary when requested

## Copy Number And Structural Variants

Current route:

1. Select CNV or SV tools according to assay, tumor-normal pairing, panel size, purity, and platform.
2. Use `CNVkit`, `FACETS`, `PureCN`, `Sequenza`, `ASCAT`, `ichorCNA`, `Control-FREEC`, `GISTIC2`, `Manta`, `Delly`, `SvABA`, `GRIDSS`, `Sniffles2`, `cuteSV`, or long-read-specific tools when suitable.
3. Validate important rearrangements or amplifications with coverage, split reads, discordant pairs, long-read support, FISH, WGS, or orthogonal assays when available.

Required figures:

- genome-wide copy-number profile, segment plot, purity-ploidy fit, B-allele frequency, and allele-specific copy-number plots
- focal amplification or deletion plots around key loci
- SV circos, breakpoint, read-support, fusion, and gene-impact plots
- GISTIC peak plots and recurrent event heatmaps when cohort size supports them

## HLA Typing And Variant-To-Antigen Handoff

Current route:

1. Run HLA typing only from data that support it: WES, WGS, RNA-seq, targeted HLA, or validated clinical HLA calls.
2. Use `OptiType`, `arcasHLA`, `HLA-HD`, `Polysolver`, `HLAminer`, `Kourami`, or platform-specific tools according to input and class I or class II need.
3. Record HLA resolution, allele ambiguity, expression support, and sample identity.
4. For neoantigen work, pass HLA calls, annotated variants, phasing, expression, clonality, and copy-number status to `immunopeptidomics.md`.

Required figures:

- HLA allele table and ambiguity summary
- read support or expression support per HLA allele when available
- HLA loss, LOH, or expression plots when tumor immune escape is part of the question
- variant-to-antigen candidate flow diagram

## Source Index

Last checked: 2026-05-28.

- GATK HaplotypeCaller: https://gatk.broadinstitute.org/hc/en-us/articles/360036889312-HaplotypeCaller
- GATK Mutect2: https://gatk.broadinstitute.org/hc/en-us/articles/360037593851-Mutect2
- nf-core/sarek: https://nf-co.re/sarek
- DeepVariant: https://github.com/google/deepvariant
- Strelka2: https://github.com/Illumina/strelka
- Clair3: https://github.com/HKU-BAL/Clair3
- VEP: https://www.ensembl.org/info/docs/tools/vep/index.html
- maftools: https://bioconductor.org/packages/release/bioc/html/maftools.html
- SigProfiler: https://github.com/AlexandrovLab/SigProfilerExtractor
- CNVkit: https://cnvkit.readthedocs.io/
- FACETS: https://github.com/mskcc/facets
- PureCN: https://bioconductor.org/packages/release/bioc/html/PureCN.html
- GISTIC2: https://gatk.broadinstitute.org/hc/en-us/articles/360035890671
- OptiType: https://github.com/FRED-2/OptiType
- arcasHLA: https://github.com/RabadanLab/arcasHLA
- HLA-HD: https://www.genome.med.kyoto-u.ac.jp/HLA-HD/
