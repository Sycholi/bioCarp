# Metagenomics

Use this file for 16S rRNA, ITS, shotgun metagenomics, metatranscriptomics, microbiome multi-omics, microbial genome reconstruction, host-microbe analysis, microbial ecology, and microbiome literature reproduction.

## Intake

Before choosing tools, verify:

- assay type: 16S, ITS, shotgun DNA, metatranscriptome, virome, long-read metagenomics, or mixed omics
- platform: Illumina, Nanopore, PacBio, or mixed
- sample source, extraction kit, negative controls, positive controls, batch, host species, tissue, stool, swab, tumor, blood, or environmental material
- primer region for amplicon data and reference database release
- host-depletion status, read length, paired-end status, expected biomass, contamination risk, and metadata
- biological unit: subject, sample, time point, cage, litter, site, lesion, or batch
- whether `platforms.md` and `parameters.md` are needed for sequencing platform, primer trimming, truncation, host removal, taxonomy database, differential method, or MAG quality thresholds

## Amplicon Route

Current route:

1. Inspect raw read quality, primer structure, barcode structure, read pairing, and metadata.
2. Read `parameters.md` before choosing truncation length, expected error, chimera rule, host removal, contaminant filtering, taxonomy database, rarefaction, normalization, PERMANOVA formula, and differential abundance method.
3. Use `QIIME 2`, `DADA2`, or `mothur` according to the project ecosystem and required outputs.
4. Prefer ASV-level processing for modern 16S or ITS work when the data support it.
5. Remove primers, filter low-quality reads, infer ASVs, remove chimeras, and assign taxonomy against a stated database.
6. Track read counts through every step and preserve representative sequences, feature table, taxonomy, phylogeny, and metadata.
7. Rarefy only for diversity plots or methods that require it. Do not use rarefaction as the only normalization strategy for differential abundance.
8. Run alpha diversity, beta diversity, ordination, PERMANOVA or equivalent tests, taxonomic composition, and differential abundance with compositional-data-aware methods.

Required figures:

- read quality profiles and filtering-retention table
- ASV or OTU count summary, chimera summary, taxonomy assignment summary
- alpha diversity boxplots with group statistics
- beta diversity PCoA or NMDS with PERMANOVA or constrained ordination when appropriate
- taxonomic stacked bars at multiple ranks
- differential abundance volcano, effect-size plot, heatmap, cladogram, or bubble plot
- prevalence and abundance filtering diagnostics
- batch, control, and contamination review plots when controls exist

## Shotgun Metagenomics Route

Current route:

1. Run read QC, adapter trimming, host read removal, low-complexity review, duplicate review when relevant, contamination control, and MultiQC.
2. Choose a read-based taxonomic profiler such as `Kraken2` plus `Bracken`, `MetaPhlAn`, `mOTUs`, `sylph`, or a project-specific profiler.
3. Use `HUMAnN`, `eggNOG-mapper`, `SUPER-FOCUS`, `FMAP`, or equivalent tools for functional profiling when reads or contigs support it.
4. Keep taxonomic profiles, functional profiles, database versions, host-removal statistics, and unclassified read fractions.
5. Run diversity, composition, differential abundance, functional pathway comparison, and host-microbe association according to study design.
6. For long-read metagenomics, use long-read-aware QC, host removal, taxonomic classification, assembly, polishing, and annotation routes.

Required figures:

- read QC and host-removal summary
- classified versus unclassified read fractions
- taxonomic composition by rank and sample group
- alpha and beta diversity plots
- differential taxa and differential pathway plots
- pathway abundance and pathway coverage plots
- heatmaps for selected taxa, gene families, pathways, resistome, or virulome
- database coverage and sample-depth diagnostics

## Contamination, Strain, Virus, Resistome, And Virulome

Current route:

1. For low-biomass, tumor, blood, tissue, or reagent-sensitive microbiome data, inspect negative controls, positive controls, extraction batch, and common contaminant taxa before biological interpretation.
2. Use `KneadData`, Bowtie2, BWA, or platform-specific host-removal routes for host filtering.
3. Use `decontam` or design-aware prevalence and frequency checks when negative controls or DNA concentration exist.
4. Use `StrainPhlAn`, `inStrain`, StrainGE, or related methods for strain-level analysis only when read depth and marker coverage support it.
5. Use `VirSorter2`, `VIBRANT`, `CheckV`, `geNomad`, or related tools for viral contigs and virome analysis.
6. Use `AMRFinderPlus`, `CARD`, `RGI`, `ResFinder`, `VFDB`, dbCAN, antiSMASH, or DRAM modules when resistome, virulence, CAZyme, or biosynthetic potential is central.
7. Use `PICRUSt2` for marker-gene functional prediction only as a weaker inference when shotgun functional profiling is unavailable.

Required figures:

- control and contaminant taxa review plots
- host-removal and read-retention summary
- strain-sharing and strain-diversity plots when strain tools are used
- viral contig quality, taxonomy, and abundance plots
- AMR, virulence, CAZyme, or biosynthetic-gene-cluster heatmaps
- marker-gene predicted function plots labeled as inferred when using PICRUSt2

## Assembly, Binning, MAGs, And Microbial Genomes

Current route:

1. Assemble per sample or co-assemble only when the design justifies it.
2. Use metagenome assemblers such as `MEGAHIT`, `metaSPAdes`, `metaFlye`, or long-read-aware alternatives.
3. Bin contigs with complementary binning tools when possible, then refine bins.
4. Assess MAG quality with `CheckM2`, `CheckM`, `BUSCO`, or equivalent tools.
5. Dereplicate with `dRep`, assign taxonomy with `GTDB-Tk`, annotate with `Prokka`, `Bakta`, `eggNOG-mapper`, `DRAM`, `dbCAN`, `CARD`, or project-specific databases.
6. Quantify MAG abundance and connect MAGs to phenotype only after checking mapping depth, completeness, contamination, and strain ambiguity.

Required figures:

- assembly size, N50, contig length, GC, and read mapping summary
- bin completeness-contamination plot
- MAG quality heatmap and taxonomy summary
- abundance heatmap across samples
- phylogenomic tree when strain or lineage claims are made
- functional annotation summary, pathway plots, CAZyme, AMR, virulence, or biosynthetic-gene-cluster plots when relevant

## Metatranscriptomics

Current route:

1. Separate host, microbial rRNA, microbial mRNA, and technical contamination.
2. Decide whether the analysis is taxonomic activity, pathway activity, gene expression, or strain activity.
3. Use paired metagenome data for normalization when available.
4. Preserve RNA-specific QC, rRNA depletion metrics, host fraction, and mapping strategy.
5. Interpret microbial expression in light of microbial abundance.

Required figures:

- RNA read class composition and rRNA depletion summary
- taxonomic activity profiles
- pathway activity heatmaps and group comparisons
- expression-abundance concordance plots when paired metagenomics exist
- differential microbial transcript or pathway plots

## Differential Abundance And Association

Current route:

1. Filter features by prevalence and abundance before testing.
2. Treat microbiome count data as compositional and sparse.
3. Prefer `ANCOM-BC2`, `ALDEx2`, `MaAsLin2`, `corncob`, `LinDA`, or comparable methods according to design.
4. Use random effects or repeated-measures models when subjects are sampled repeatedly.
5. Compare at least two compatible differential abundance methods for high-value claims.
6. Report effect sizes, confidence intervals, adjusted P values, and direction consistency.

Required figures:

- prevalence-abundance filtering plot
- differential abundance volcano or lollipop plot
- effect-size forest plot for top taxa or pathways
- coefficient heatmap across metadata variables
- method-concordance plot when multiple methods are used

## Host-Microbe And Oncology Integration

Use when microbiome results need to connect to tumor, immune, therapy, metabolite, or clinical features.

Current route:

1. Align subject IDs, time points, specimen sites, treatment, antibiotics, diet, geography, batch, and sequencing depth.
2. Model microbiome features with host phenotypes while preserving the subject as the inference unit.
3. Connect microbial taxa and functions to bulk RNA-seq, single-cell states, spatial niches, metabolites, immune cell fractions, or response endpoints.
4. Use causal language only when longitudinal design, perturbation, or external evidence supports it.

Required figures:

- host-microbe correlation heatmap with controlled metadata
- taxa or pathway versus immune, gene, metabolite, or clinical phenotype plots
- multivariable association forest plots
- longitudinal trajectory plots when repeated sampling exists
- external cohort validation plots when available

## Source Index

Last checked: 2026-05-28.

- QIIME 2 documentation: https://library.qiime2.org/docs
- QIIME 2 Current Protocols workflow: https://curr-protoc-bioinformatics.qiime2.org/
- DADA2 Bioconductor package: https://www.bioconductor.org/packages/release/bioc/html/dada2.html
- DADA2 introduction: https://bioconductor.org/packages/release/bioc/vignettes/dada2/inst/doc/dada2-intro.html
- MetaPhlAn 4 paper: https://www.nature.com/articles/s41587-023-01688-w
- HUMAnN documentation: https://huttenhower.sph.harvard.edu/humann/
- Kraken 2 paper: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1891-0
- Bracken documentation: https://hpc.nih.gov/apps/bracken.html
- sylph paper: https://www.nature.com/articles/s41587-024-02412-y
- ANCOM-BC paper: https://www.nature.com/articles/s41467-020-17041-7
- ANCOM-BC2 paper: https://www.nature.com/articles/s41592-023-02092-7
- MaAsLin2 paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC8714082/
- microbiome differential abundance benchmarking: https://pmc.ncbi.nlm.nih.gov/articles/PMC8763921/
- NMDC MAG workflow: https://docs.microbiomedata.org/workflows/chapters/6_Metagenome_Assembled_Genome/
- KneadData: https://huttenhower.sph.harvard.edu/kneaddata/
- decontam: https://bioconductor.org/packages/release/bioc/html/decontam.html
- StrainPhlAn: https://github.com/biobakery/MetaPhlAn/wiki/StrainPhlAn-4
- inStrain: https://instrain.readthedocs.io/
- VirSorter2: https://github.com/jiarong/VirSorter2
- VIBRANT: https://github.com/AnantharamanLab/VIBRANT
- CheckV: https://bitbucket.org/berkeleylab/checkv/
- geNomad: https://portal.nersc.gov/genomad/
- PICRUSt2: https://github.com/picrust/picrust2
- AMRFinderPlus: https://github.com/ncbi/amr
- CARD RGI: https://card.mcmaster.ca/analyze/rgi
- ResFinder: https://bitbucket.org/genomicepidemiology/resfinder/
- VFDB: http://www.mgc.ac.cn/VFs/
