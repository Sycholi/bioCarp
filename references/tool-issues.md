# Tool Issues

Use this file when `index.md` selects issue review for version-sensitive, web-service dependent, fast-moving, or object-format-sensitive tools.

This file does not replace official documentation. It defines the troubleshooting and issue-review habit that must happen before implementation and when errors appear.

## Issue Review Contract

Before using a major tool in an analysis:

1. Record tool name, version, installation source, R or Python version, operating system, and key dependencies.
2. Check official documentation and NEWS or changelog.
3. Check open and recently closed GitHub issues for the exact package and version.
4. Check Bioconductor support, package discussion boards, Stack Overflow, Biostars, scverse discourse, and package-specific forums when relevant.
5. For Chinese practical troubleshooting, search CSDN, CSDN 问答, and Chinese bioinformatics blogs by exact error text. Treat these as symptom-level references, then verify against official documentation or source code.
6. Record known unresolved issues, version conflicts, reproducible error messages, and accepted workarounds in the project notes.
7. Do not silently apply a workaround. State why it is needed and what behavior it changes.
8. Prefer version pinning with `renv`, `conda`, `mamba`, `pip-tools`, Docker, Singularity, or Nextflow profiles when the tool is fragile.

## Issue Notes To Capture

For each relevant issue, record:

- source: GitHub issue, Bioconductor support, CSDN, forum, documentation, or source code
- URL and access date
- tool version and dependency versions
- symptom or error text
- issue status: open, closed, fixed in version, wontfix, stale, unclear, or user error
- accepted workaround
- whether the workaround affects scientific output
- local test confirming that the workaround works on the project data

## Common Problem Classes

### Seurat v5 and SeuratObject

Common issues:

- Assay5 layer handling changes break old code using `slot`.
- `GetAssayData()` may fail or warn when multiple layers exist.
- Some old packages expect v3 or v4 assay structure.
- Merged objects may need explicit layer handling before downstream tools.

Typical checks:

- Use `Layers()`, `JoinLayers()`, `LayerData()`, and `layer =` syntax deliberately.
- Verify whether downstream packages support Seurat v5.
- Convert or rebuild objects only after preserving raw counts and metadata.
- Use `renv` or explicit package versions for old projects.

### CellChat

Common issues:

- Cell group names, factor levels, missing expression layers, low cell counts, and database version mismatches can cause errors.
- Spatial mode needs distance and coordinate information in the expected format.
- Merged or integrated objects may not contain the expression layer expected by CellChat.

Typical checks:

- Verify group labels and minimum cell counts.
- Use raw or normalized expression according to CellChat documentation.
- Record CellChatDB version and species.
- Check active GitHub issues when `computeCommunProb()` or visualization functions fail.

### decoupleR, DoRothEA, PROGENy, OmniPath, CollecTRI

Common issues:

- Input matrix scale and orientation are easy to mismatch.
- Gene identifiers must match network targets.
- Some networks are human-centered and require orthology translation for mouse or rat.
- Method outputs differ by statistic, signed network, confidence level, and resource.

Typical checks:

- Confirm row genes and sample columns.
- Check network coverage before activity inference.
- Record resource version and confidence filter.
- Compare at least two compatible methods or resources for high-value claims.

### immunedeconv and deconvolution tools

Common issues:

- Some methods expect non-log expression and HGNC symbols.
- xCell spillover compensation can overcompensate when irrelevant cell types are included.
- CIBERSORT or CIBERSORTx can require license, web login, Docker, or specific file formatting.
- MCP-counter and xCell scores are not always absolute cell fractions.

Typical checks:

- Verify input scale and gene symbols.
- Use `expected_cell_types` when supported and biologically justified.
- Separate score-type methods from fraction-type methods in plots and interpretation.
- Check CIBERSORTx login, file format, and run mode before promising results.

### Scanpy, AnnData, and scverse

Common issues:

- AnnData layer, raw, and X matrix semantics can differ across workflows.
- Python package version conflicts can break compiled dependencies.
- Sparse and dense matrix conversions can change memory requirements.

Typical checks:

- Record which matrix is used for each step.
- Save `.h5ad` after major processing stages.
- Pin Python, scanpy, anndata, numpy, scipy, and scvi-tools versions when needed.

### Emerging single-cell, spatial, and imaging tools

Common issues:

- New tools such as SLOPER, scDecorr, PSGRN, TotalX-linked workflows, TrendCatcher, scSurv, scSurvival, RegDiffusion, seismicGWAS, and phenoptr-related pipelines can have narrow input assumptions, unstable installation paths, or limited examples.
- Some methods are preprint-only, recent-paper-only, or repository-only and may not have mature error handling.
- Tool names can be ambiguous. Confirm the exact repository or package before installing.
- Spatial tools differ in coordinate conventions, image origin, spot or cell indexing, and supported object format.
- Survival and GWAS-linked single-cell tools can fail when patient labels, event times, LD reference, or annotation granularity do not match assumptions.

Typical checks:

- Record the source URL, commit, package version, example dataset, and successful smoke test.
- Run the official example before running project data when the tool is new to the environment.
- Compare the result with a mature method family when the conclusion depends on a new tool.
- Preserve all input conversions and intermediate tables so source-format errors can be traced.

### Upstream workflows and raw data processing

Common issues:

- Cell Ranger, Space Ranger, STARsolo, alevin-fry, kallisto-bustools, and nf-core workflows can use different gene models, barcode filters, intron handling, and output conventions.
- Nextflow cache, container engines, profiles, and reference downloads can fail or silently reuse old outputs.
- Public FASTQ metadata can have lane, sample, organism, and strandedness errors.

Typical checks:

- Record workflow version, command, profile, container, reference, annotation, and genome build.
- Preserve MultiQC, logs, sample sheet, and per-sample output counts.
- Compare expected sample count, read count, and chemistry with metadata before downstream analysis.

### Variant, HLA, and antigen peptide tools

Common issues:

- Variant callers differ by tumor-normal pairing, panel size, purity, UMI handling, and platform.
- HLA tools differ in class support, resolution, input type, and allele ambiguity.
- Neoantigen workflows depend on transcript annotation, expression, HLA calls, phasing, clonality, and copy-number status.
- NetMHCpan, MHCflurry, MixMHCpred, pVACtools, and related predictors can change model versions and output columns.

Typical checks:

- Record caller version, reference resources, panel of normals, germline resource, filter settings, and annotation database release.
- Keep HLA allele support and ambiguity in reports.
- Check pVACtools, NetMHCpan, and predictor version before comparing scores across runs.
- Treat predicted peptides as candidates unless peptide evidence or functional evidence supports them.

### Proteomics, metabolomics, and flux tools

Common issues:

- MaxQuant, FragPipe, DIA-NN, Spectronaut, and OpenMS differ in protein grouping, FDR, library handling, and missing-value behavior.
- MS raw formats and vendor converters can change peak picking and metadata.
- Metabolite annotation level is often lower than compound identity.
- XCMS, MZmine, MS-DIAL, GNPS, SIRIUS, and MetaboAnalyst results depend on peak picking, adduct rules, retention-time alignment, blanks, and pooled QC.
- Flux analysis depends on isotope correction, tracer design, steady-state assumptions, model definition, and parameter identifiability.

Typical checks:

- Record raw file conversion, search database, FDR, digestion enzyme, modifications, library, and quantification settings.
- Preserve QC plots before imputation or normalization.
- Report metabolite annotation level and supporting evidence.
- For isotope tracing, record correction tool, tracer, time points, model, fit, residuals, and confidence intervals.

### Epigenomics and chromatin tools

Common issues:

- MACS2, MACS3, SEACR, and broad-peak callers require mark- and protocol-specific settings.
- deepTools, HOMER, MEME, TOBIAS, chromVAR, Cicero, and footprint tools depend on genome build, motif database, peak set, and background selection.
- Bismark, methylKit, DSS, bsseq, minfi, sesame, ChAMP, and RnBeads can differ by normalization, probe filtering, coverage filtering, and annotation release.
- Hi-C tools depend on restriction enzyme, resolution, normalization, and contact depth.

Typical checks:

- Record genome build, blacklist, peak caller, control, replicate handling, motif database, and normalization.
- Save bigWig, peak, matrix, and browser-track evidence for key loci.
- For methylation, report probe or CpG filtering and beta or M value choice.
- For Hi-C, check valid pairs, distance decay, resolution, and normalization before loop or compartment claims.

### Metagenomics and microbiome tools

Common issues:

- Reference databases differ across releases and can change taxonomic calls.
- Kraken2 and Bracken outputs depend heavily on database construction and read length.
- QIIME 2 artifacts and plugin versions can be incompatible across releases.
- DADA2 trimming parameters can remove most reads when quality profiles or primer structure are misread.
- Differential abundance results can change across ANCOM-BC2, ALDEx2, MaAsLin2, and related methods.
- Low-biomass samples can be dominated by reagent or environmental contamination.

Typical checks:

- Record database name, version, build date, and command used to build or download it.
- Preserve read-retention tables and classified or unclassified fractions.
- Check negative controls and common contaminant taxa before biological interpretation.
- Compare compatible differential abundance methods for high-value claims.
- Record whether data were rarefied, transformed, centered log-ratio transformed, or modeled as counts.

### Structural biology, docking, and molecular dynamics

Common issues:

- Structure predictors differ in molecule support, license, model access, and confidence metrics.
- Low-confidence predicted regions can produce misleading docking pockets.
- Protonation, tautomer, metal, cofactor, and water handling can change docking poses.
- Docking scores are not comparable across tools without calibration.
- MD results can be dominated by force field, ligand parameters, equilibration, or insufficient sampling.
- GPU, CUDA, OpenMM, GROMACS, and Python dependency conflicts are common.

Typical checks:

- Record structure source, model version, confidence metrics, and all preprocessing steps.
- Redock a known ligand or use a benchmark control when possible.
- Run more than one pose or method when ranking drives the conclusion.
- Store force field, ligand parameter files, random seeds, run length, and replicate information.
- Mark short single MD runs as exploratory.

### Imaging, segmentation, and virtual spatial tools

Common issues:

- DICOM spacing, orientation, resampling, and RTSTRUCT conversion can silently change geometry.
- Tile-level splits can leak patient information in WSI or microscopy models.
- Segmentation labels from different annotators or protocols may not be comparable.
- nnU-Net, MONAI, TotalSegmentator, Cellpose, and StarDist outputs can fail on out-of-domain images.
- Stain normalization, scanner differences, compression, and registration can dominate virtual staining or virtual spatial prediction.
- Virtual marker or gene-expression predictions can look plausible without being quantitatively valid.

Typical checks:

- Verify image orientation, spacing, masks, contour overlays, and patient-level split before modeling.
- Save best, median, and worst visual cases, not only aggregate metrics.
- Evaluate segmentation with overlap, boundary, and volume metrics.
- For virtual outputs, compare against measured paired markers or spatial transcriptomics when available.
- Record model checkpoint, training data domain, stain normalization, and uncertainty strategy.

### Web Services and Model Checkpoints

Common issues:

- CIBERSORTx, CMap, DrugReflector checkpoints, CellTypist models, and other resources can change, move, or require registration.
- Model checkpoints may be large, versioned, or incompatible with the installed package.

Typical checks:

- Confirm access before promising an output.
- Record model checkpoint DOI or URL.
- Cache model files in the project working directory when allowed.
- Report access restrictions clearly.

### Clinical research, causal inference, and clinical data standards

Common issues:

- Sample-size tools can silently use different sidedness, allocation, dropout, accrual, event-rate, or interim assumptions.
- Target trial emulation fails when eligibility, treatment assignment, time zero, follow-up, and endpoint timing are misaligned.
- Matching and weighting workflows can produce extreme weights, poor positivity, or a changed target population.
- REDCap, OMOP, FHIR, CDISC, MedDRA, CTCAE, ICD, SNOMED CT, LOINC, RxNorm, and ATC mappings can change definitions across versions.

Typical checks:

- Record every sample-size and operating-characteristic assumption.
- Save target-trial protocol table before analysis.
- Inspect balance, overlap, effective sample size, missingness, and sensitivity plots.
- Record terminology version, data dictionary, source table, and mapping logic.

### Evidence synthesis and genetic epidemiology

Common issues:

- Meta-analysis results change with effect scale, continuity correction, heterogeneity estimator, outcome definition, and duplicate cohorts.
- MR results can be distorted by allele harmonization errors, weak instruments, sample overlap, horizontal pleiotropy, or wrong LD reference.
- GWAS, PRS, fine mapping, and colocalization depend on ancestry, imputation quality, relatedness, genome build, allele coding, and summary-statistic format.

Typical checks:

- Preserve screening decisions, study IDs, effect scales, and risk-of-bias judgments.
- Record allele harmonization, palindromic SNP handling, LD reference, genome build, and ancestry.
- Inspect QQ, Manhattan, regional association, colocalization, PRS calibration, and validation plots.

### Specialized RNA and liquid biopsy

Common issues:

- Small RNA, CLIP, Ribo-seq, long-read isoform, and RNA modification tools are protocol-sensitive.
- Splicing tools differ in event definitions and junction-count requirements.
- Direct RNA and RNA editing workflows can confuse modification, editing, SNP, mapping artifact, and strand bias without controls.
- cfDNA and ctDNA workflows depend on UMI depth, fragment size, panel design, tumor fraction, and limit of detection.

Typical checks:

- Record protocol, library design, read length, strandedness, UMI, annotation, and controls.
- Preserve read-length, junction, isoform, peak, periodicity, modification, editing, fragment-size, and molecular-support diagnostics.
- Treat MRD and longitudinal ctDNA claims as clinical hypotheses unless assay validation supports the threshold.

## Practical Source Index

Last checked: 2026-05-28.

- GitHub issue API documentation: https://docs.github.com/en/rest/issues/issues
- Seurat issue example for Assay5 layer handling: https://github.com/satijalab/seurat/issues/8176
- SeuratObject layer documentation: https://satijalab.github.io/seurat-object/reference/sub-.Assay5.html
- CSDN Seurat v5 multi-layer example: https://blog.csdn.net/Rita_rr/article/details/146542920
- CSDN Seurat `slot` to `layer` example: https://blog.csdn.net/MO_NICA/article/details/141203784
- immunedeconv xCell overcompensation documentation: https://omnideconv.org/immunedeconv/reference/deconvolute_xcell.html
- immunedeconv deconvolution input documentation: https://omnideconv.org/immunedeconv/reference/deconvolute.html
- CellChat v2 repository: https://github.com/jinworks/CellChat
- CIBERSORTx web service: https://cibersortx.stanford.edu/
- QIIME 2 documentation: https://library.qiime2.org/docs
- DADA2 documentation: https://bioconductor.org/packages/release/bioc/vignettes/dada2/inst/doc/dada2-intro.html
- Kraken 2 paper: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1891-0
- AutoDock Vina documentation: https://autodock-vina.readthedocs.io/
- GROMACS documentation: https://manual.gromacs.org/documentation/2024.0/index.html
- OpenMM: https://openmm.org/
- nnU-Net repository: https://github.com/MIC-DKFZ/nnUNet
- MONAI documentation: https://docs.monai.io/en/latest/
- TotalSegmentator repository: https://github.com/wasserth/TotalSegmentator
- nf-core documentation: https://nf-co.re/docs
- Cell Ranger: https://www.10xgenomics.com/support/software/cell-ranger
- BD Rhapsody documentation: https://bd-rhapsody-bioinfo-docs.genomics.bd.com/
- ScaleBio Seq Suite documentation: https://scalebio.github.io/ScaleRna-docs/
- Fluent PIPseeker documentation: https://www.fluentbio.com/
- alevin-fry: https://alevin-fry.readthedocs.io/
- GATK documentation: https://gatk.broadinstitute.org/
- pVACtools documentation: https://pvactools.readthedocs.io/
- NetMHCpan: https://services.healthtech.dtu.dk/services/NetMHCpan-4.1a/
- FragPipe: https://fragpipe.nesvilab.org/
- DIA-NN: https://github.com/vdemichev/DiaNN
- MetaboAnalystR: https://www.metaboanalyst.ca/
- XCMS: https://bioconductor.org/packages/release/bioc/html/xcms.html
- MACS3: https://macs3-project.github.io/MACS/
- Bismark: https://www.bioinformatics.babraham.ac.uk/projects/bismark/
- rpact: https://www.rpact.org/
- TrialEmulation: https://causal-lda.r-universe.dev/TrialEmulation/TrialEmulation.pdf
- MatchIt: https://kosukeimai.github.io/MatchIt/
- WeightIt: https://ngreifer.github.io/WeightIt/
- PLINK2: https://www.cog-genomics.org/plink/2.0/
- metafor: https://www.metafor-project.org/
