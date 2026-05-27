# Immunopeptidomics

Use this file for antigen peptides, immunopeptidomics, HLA typing, MHC binding prediction, neoantigen prediction, tumor antigen prioritization, TCR-pMHC analysis, and peptide-level validation.

## Intake

Before implementation, verify:

- antigen type: mutated neoantigen, tumor-associated antigen, viral antigen, cancer-testis antigen, alternative ORF peptide, splicing peptide, fusion peptide, or noncanonical peptide
- input data: VCF, MAF, WES, WGS, RNA-seq, proteomics, immunopeptidomics LC-MS/MS, HLA calls, TCR data, normal tissue expression, clonality, copy number, and clinical endpoint
- HLA class I and class II need, peptide length, phasing, transcript annotation, expression threshold, and whether MS evidence exists
- output purpose: candidate ranking, vaccine design research, immune escape analysis, immunopeptidomics QC, TCR recognition hypothesis, or literature-supported antigen list

## HLA Typing And Candidate Generation

Current route:

1. Obtain sample-specific HLA alleles from clinical HLA typing or infer them from WES, WGS, or RNA-seq using tools suited to the input.
2. Use annotated variants from `variants.md`, preserve transcript consequence, amino-acid change, variant allele fraction, depth, clonality, and copy-number context.
3. Include RNA expression and, when available, protein or peptide evidence before prioritization.
4. Use `pVACtools` for standard tumor neoantigen workflows when annotated VCF and HLA calls are available.
5. Use multiple peptide-MHC predictors for high-value candidates, then compare algorithm agreement and disagreement.

Primary tools:

- HLA typing: OptiType, arcasHLA, HLA-HD, Polysolver, HLAminer, Kourami
- neoantigen workflow: pVACseq, pVACbind, pVACfuse, pVACsplice, pVACvector, pVACview
- MHC class I prediction: NetMHCpan, MHCflurry, MixMHCpred, BigMHC, PRIME, HLAthena, MHCnuggets
- MHC class II prediction: NetMHCIIpan, MixMHC2pred, MARIA, MHCnuggets when supported
- immune resources: IEDB, TANTIGEN, TSNAdb, Cancer Antigenic Peptide Database, ipMSDB, HLA Ligand Atlas, SysteMHC Atlas

Required figures:

- HLA allele summary and read or expression support
- variant-to-peptide candidate flow, retained and filtered counts, and filter reasons
- binding affinity, percentile rank, presentation score, and stability score distributions
- algorithm-overlap UpSet plot or heatmap
- peptide length distribution and allele-specific candidate counts
- expression, clonality, copy-number, and normal-tissue-expression evidence matrix
- final antigen candidate priority plot with evidence columns

## Immunopeptidomics LC-MS/MS

Current route:

1. Preserve raw spectra, search database, enzyme setting, variable modifications, FDR thresholds, HLA alleles, and sample metadata.
2. Use immunopeptidomics-specific search settings. Do not force tryptic assumptions when eluted ligand data are nontryptic.
3. Search with MaxQuant, FragPipe, PEAKS, Comet, MS-GF+, MetaMorpheus, or platform-specific tools according to raw format and lab practice.
4. Assess MHC specificity with MhcVizPipe, GibbsCluster, MoDec, NetMHCpan, MHCflurry, MixMHCpred, or equivalent tools.
5. Link observed peptides to source proteins, RNA expression, tumor specificity, HLA allele, binding prediction, and disease context.

Required figures:

- raw MS QC, peptide-spectrum match, FDR, and intensity distributions
- peptide length distribution by sample and HLA class
- allele-specific binding prediction and motif logos
- GibbsCluster or motif clustering plots when used
- source protein and pathway enrichment plots
- overlap between predicted and observed peptides
- annotated spectra for high-value peptides when evidence is central

## TCR And pMHC Follow-Up

Current route:

1. Use TCR analysis only when TCR-seq, paired alpha-beta chains, clonotype data, tetramer data, public TCR databases, or experimentally supported TCR-pMHC evidence exist.
2. Compare candidate peptides with known epitope databases before proposing novelty.
3. Use tools such as GLIPH2, TCRdist, pMTnet, ERGO, NetTCR, TCRMatch, VDJdb, IEDB, McPAS-TCR, or immuneCODE only after verifying input compatibility.
4. Treat predicted TCR recognition as a prioritization result unless functional assays support it.

Required figures:

- clonotype abundance and peptide evidence table
- TCR similarity network, motif, or cluster plot when supported
- peptide-HLA-TCR candidate matrix
- database match or novelty summary
- validation status and assay-priority plot

## Source Index

Last checked: 2026-05-28.

- pVACtools documentation: https://pvactools.readthedocs.io/
- pVACtools paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC7056579/
- pVACview: https://github.com/griffithlab/pVACview
- NetMHCpan: https://services.healthtech.dtu.dk/services/NetMHCpan-4.1a/
- MHCflurry: https://openvax.github.io/mhcflurry/
- MixMHCpred: https://github.com/GfellerLab/MixMHCpred
- BigMHC: https://github.com/KarchinLab/bigmhc
- IEDB: https://www.iedb.org/
- MhcVizPipe paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC8717601/
- HLA Ligand Atlas: https://hla-ligand-atlas.org/
- VDJdb: https://vdjdb.cdr3.net/
- McPAS-TCR: http://friedmanlab.weizmann.ac.il/McPAS-TCR/
