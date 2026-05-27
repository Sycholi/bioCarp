# Metabolomics

Use this file for metabolomics, lipidomics, targeted metabolite panels, untargeted LC-MS or GC-MS, NMR metabolomics, isotope tracing, metabolic flux analysis, constraint-based metabolic modeling, and single-cell or spatial metabolism inference.

## Intake

Before implementation, verify:

- experiment type: untargeted LC-MS, GC-MS, NMR, targeted metabolite panel, lipidomics, isotope tracing, fluxomics, extracellular flux, Seahorse, single-cell metabolism inference, or genome-scale metabolic modeling
- raw format, ion mode, chromatography, batch, pooled QC, blank, internal standard, dilution series, isotope tracer, time points, labeling steady state, and metadata
- annotation evidence level, database, adduct rules, retention time support, MS/MS support, and compound class
- statistical unit, repeated measures, batch design, normalization strategy, and pathway question
- whether `platforms.md` and `parameters.md` are needed for instrument, acquisition mode, peak picking, alignment, blank filtering, QC correction, annotation, isotope correction, or flux model settings

## Untargeted And Targeted Metabolomics

Current route:

1. Preserve raw spectra, vendor files, converted mzML or mzXML, sample table, batch, blanks, pooled QC, and internal standards.
2. Read `platforms.md` for LC-MS, GC-MS, CE-MS, MALDI-MSI, NMR, ion mode, chromatography, and instrument-specific interpretation.
3. Read `parameters.md` for peak picking, retention-time alignment, gap filling, blank filtering, pooled-QC correction, normalization, adduct grouping, isotope grouping, and annotation confidence.
4. Run peak detection, deconvolution, retention-time correction, alignment, gap filling, adduct grouping, isotope grouping, blank filtering, and QC filtering.
5. Use `XCMS`, `MZmine`, `MS-DIAL`, `asari`, `OpenMS`, `MetaboAnalystR`, or vendor tools according to input and lab practice.
6. Annotate metabolites using MS/MS libraries, exact mass, isotope pattern, retention time, SIRIUS, CSI:FingerID, MS-FINDER, GNPS, HMDB, KEGG, LIPID MAPS, or MassBank.
7. Report annotation confidence. Do not treat formula-level or class-level annotations as confirmed metabolites.

Required figures:

- TIC or base peak chromatogram summary
- peak count, missingness, QC RSD, blank ratio, internal-standard stability, and batch plots
- retention-time correction and mass-error plots
- PCA, sample correlation, outlier review, and QC clustering
- volcano, heatmap, boxplot, and pathway enrichment plots
- annotation level, compound class, MS/MS match, and adduct summary plots

## Lipidomics

Current route:

1. Preserve lipid class, adduct, MS/MS evidence, retention time, and isomer ambiguity.
2. Use lipid-aware tools such as MS-DIAL, MZmine, LipidSearch, LipidHunter, LipidMatch, LipidAnnotator, or LIPID MAPS routes when suitable.
3. Analyze lipid class abundance, chain length, unsaturation, saturation, and pathway-level patterns.
4. Avoid overinterpreting unresolved isomers or adduct duplicates.

Required figures:

- lipid class composition and abundance
- chain length and unsaturation plots
- differential lipid volcano, heatmap, and class-level summary
- pathway or reaction-family plot when supported
- MS/MS evidence panels for key lipids when central

## Isotope Tracing And Metabolic Flux

Current route:

1. Confirm tracer, labeling design, time points, medium composition, cell count, extraction protocol, derivatization, and whether isotopic or metabolic steady state holds.
2. Correct natural isotope abundance with IsoCor, AccuCor, El-MAVEN, Polly, or suitable scripts.
3. Report mass isotopomer distributions, fractional enrichment, pool size, and tracer incorporation before flux modeling.
4. For 13C metabolic flux analysis, use INCA, OpenFLUX2, 13CFLUX2, Metran, FiatFlux, or lab-validated software when the model and measurements support flux estimation.
5. Report confidence intervals, goodness-of-fit, residuals, and parameter identifiability.

Required figures:

- tracer experiment design and sampling timeline
- mass isotopomer distribution plots
- fractional enrichment and pool-size plots
- pathway-level labeling maps
- model fit, residual, confidence interval, and flux map plots
- comparison of measured and simulated isotopologue fractions

## Constraint-Based Metabolic Modeling

Current route:

1. Use curated genome-scale metabolic models when possible, such as Human1, Recon3D, Recon2, BiGG models, or species-specific models.
2. Use COBRA Toolbox, COBRApy, cameo, RAVEN, CarveMe, MEMOTE, or MICOM according to organism and question.
3. Run model quality checks before biological interpretation.
4. Use FBA, pFBA, FVA, gene deletion, reaction deletion, MOMA, ROOM, exchange flux, production envelope, or thermodynamic constraints as required.
5. Integrate transcriptomics, proteomics, metabolomics, or microbiome data only after recording mapping assumptions and objective function.

Required figures:

- model coverage and gap summary
- growth or objective value comparison
- FBA or pFBA flux map
- flux variability range plots
- gene or reaction knockout effect plots
- exchange flux, production envelope, and sensitivity plots
- omics-to-reaction mapping and pathway activity plots

## Single-Cell, Spatial, And Host-Microbe Metabolism

Current route:

1. Distinguish direct measured metabolites from transcriptome-inferred metabolism.
2. Use scFEA, Compass, scMetabolism, AUCell or GSVA metabolic gene sets, CellPhoneDB or ligand-resource metabolism links, or spatial metabolism tools only after checking inputs.
3. For microbiome metabolism, connect metagenomic functions, HUMAnN pathways, metabolites, host expression, and clinical metadata.
4. Treat transcriptome-derived flux as inferred pathway activity unless supported by metabolite or isotope data.

Required figures:

- metabolic pathway score maps by cell type, cluster, sample, and spatial region
- inferred flux or reaction activity heatmaps
- metabolite-gene or metabolite-microbe association plots
- pathway maps connecting measured metabolites and inferred enzyme activity
- validation plots with measured metabolomics or isotope data when available

## Source Index

Last checked: 2026-05-28.

- MetaboAnalystR: https://www.metaboanalyst.ca/
- MetaboAnalystR 4.0 paper: https://www.nature.com/articles/s41467-024-48009-6
- XCMS: https://bioconductor.org/packages/release/bioc/html/xcms.html
- MZmine documentation: https://mzmine.github.io/mzmine_documentation/
- MS-DIAL: http://prime.psc.riken.jp/compms/msdial/main.html
- GNPS: https://gnps.ucsd.edu/
- SIRIUS: https://bio.informatik.uni-jena.de/software/sirius/
- HMDB: https://hmdb.ca/
- LIPID MAPS: https://www.lipidmaps.org/
- IsoCor: https://github.com/MetaSys-LISBP/IsoCor
- OpenFLUX2 paper: https://link.springer.com/article/10.1186/s12934-014-0152-x
- COBRA Toolbox: https://opencobra.github.io/cobratoolbox/
- COBRApy: https://cobrapy.readthedocs.io/
- cameo: https://cameo.readthedocs.io/
- scFEA paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC8494226/
- scFEA web server: https://scflux.org/
