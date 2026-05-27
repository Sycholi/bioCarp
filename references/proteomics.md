# Proteomics

Use this file for DDA, DIA, TMT, label-free proteomics, phosphoproteomics, PTM analysis, proteogenomics, immunopeptidomics handoff, targeted proteomics, and protein-level biomarker workflows.

## Intake

Before implementation, verify:

- experiment type: DDA, DIA, TMT, iTRAQ, LFQ, PRM, SRM, phosphoproteomics, acetylome, ubiquitinome, secretome, plasma proteomics, metaproteomics, or immunopeptidomics
- raw format, instrument, acquisition method, fractionation, labeling design, batch, reference channel, search database, digestion enzyme, modification list, and FDR level
- statistical unit, biological replicates, missingness pattern, batch design, normalization method, and peptide-to-protein summarization route
- downstream need: differential abundance, pathway analysis, kinase activity, PTM site analysis, protein complex, drug target, or multi-omics integration
- whether `platforms.md` and `parameters.md` are needed for instrument, acquisition mode, raw conversion, search, FDR, normalization, imputation, or protein grouping choices

## Raw Processing And Quantification

Current route:

1. Preserve raw spectra, metadata, sample annotation, search database, FASTA version, contaminant database, decoy strategy, and all search parameters.
2. Read `platforms.md` for Orbitrap, Q-TOF, timsTOF, triple quadrupole, MALDI, DDA, DIA, diaPASEF, TMT, LFQ, PRM, and SRM platform effects when raw data or acquisition design matters.
3. Read `parameters.md` for search engine, spectral library, enzyme, missed cleavages, modifications, FDR, match-between-runs, normalization, missing values, protein grouping, and PTM localization choices.
4. Choose software by acquisition type and local availability.
5. Run QC before differential analysis: identification counts, peptide counts, protein counts, PSM FDR, mass error, retention time, missingness, intensity distribution, batch, and carryover.
6. Normalize and summarize at the peptide, protein, or PTM-site level according to the question.
7. Keep peptide-level evidence visible for high-value proteins or PTM sites.

Primary tools:

- DDA and LFQ: MaxQuant, FragPipe, MSFragger, IonQuant, OpenMS, Proteome Discoverer, MetaMorpheus, PEAKS
- DIA: DIA-NN, Spectronaut, Skyline, OpenSWATH, EncyclopeDIA, MaxDIA, AlphaDIA
- TMT or iTRAQ: MaxQuant, FragPipe, Proteome Discoverer, MSstatsTMT, OpenMS
- workflow route: `nf-core/quantms`, quantms, quantmsdiann
- targeted proteomics: Skyline, MSstats, Panorama

Required figures:

- raw MS QC, TIC or base peak summaries when available
- PSM, peptide, protein, and missingness counts per sample
- mass error, retention time, charge-state, peptide length, and FDR plots
- intensity distributions before and after normalization
- PCA, sample correlation, batch review, and replicate concordance
- peptide-to-protein evidence plots for key proteins

## Differential Proteomics

Current route:

1. Use replicate-aware models. Avoid treating peptides or proteins as independent biological samples.
2. Use MSstats, MSstatsTMT, limma, DEP, protti, Perseus, or platform-specific statistics according to quantification type.
3. Inspect missingness and imputation choices. Record whether missingness appears random, abundance-dependent, or group-specific.
4. Report effect size, adjusted P value, peptide support, and protein group ambiguity.
5. Run enrichment, pathway, network, and regulator inference after differential testing.

Required figures:

- normalization and missingness diagnostics
- PCA, correlation heatmap, and sample-level QC
- volcano, MA plot, heatmap, and top-protein plots
- pathway or GO enrichment dot plot, GSEA plot, protein network, and selected protein panels
- validation or orthogonal evidence plots when available

## PTM, Phosphoproteomics, And Kinase Activity

Current route:

1. Preserve site localization probability, modified peptide sequence, protein position, isoform, and phosphosite database mapping.
2. Separate protein abundance change from PTM-site change when both are measured.
3. Use PTM-aware tools and kinase-substrate resources for interpretation.
4. Use kinase activity and pathway inference as prioritization, then check key sites in literature or validation assays.

Primary tools and resources:

- MSstatsPTM, PTM-SEA, KSEA, PhosR, KinasePA, PTMphinder, Perseus, limma, decoupleR
- PhosphoSitePlus, OmniPath, SIGNOR, KEA, NetworKIN, Kinase Library

Required figures:

- PTM-site localization and intensity QC
- site-level volcano, heatmap, and protein-position plots
- kinase activity heatmap, enrichment plot, and substrate evidence table
- protein abundance versus PTM-site change scatter plot
- pathway and network plots for regulated PTM modules

## Proteogenomics And Multi-Omics Handoff

Current route:

1. Use sample-matched genomics, transcriptomics, and proteomics when available.
2. Check gene ID, protein ID, isoform, peptide uniqueness, and protein group ambiguity before cross-omics interpretation.
3. For variant peptides, alternative ORFs, fusion peptides, or immunopeptidomics, connect to `variants.md` and `immunopeptidomics.md`.
4. For protein-level regulators, connect to `bulk-inference.md` and `multiomics.md`.

Required figures:

- RNA-protein concordance plot
- copy-number, RNA, protein, and PTM feature concordance heatmap
- variant peptide or fusion peptide evidence plots when relevant
- multi-omics factor or network plots when integration is used

## Source Index

Last checked: 2026-05-28.

- nf-core/quantms: https://nf-co.re/quantms
- quantms documentation: https://docs.quantms.org/
- FragPipe: https://fragpipe.nesvilab.org/
- DIA-NN: https://github.com/vdemichev/DiaNN
- MaxQuant: https://www.maxquant.org/
- OpenMS: https://openms.de/
- Skyline: https://skyline.ms/
- MSstats: https://msstats.org/
- MSstatsTMT: https://bioconductor.org/packages/release/bioc/html/MSstatsTMT.html
- MSstatsPTM: https://bioconductor.org/packages/release/bioc/html/MSstatsPTM.html
- DEP: https://bioconductor.org/packages/release/bioc/html/DEP.html
- PhosR: https://bioconductor.org/packages/release/bioc/html/PhosR.html
- PhosphoSitePlus: https://www.phosphosite.org/
