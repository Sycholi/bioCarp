# Structural Bioinformatics

Use this file for protein structure prediction, protein complex prediction, molecular docking, molecular dynamics, free-energy estimation, structure-based virtual screening, ligand preparation, ADMET screening, chemoinformatics, and structure-informed drug prioritization.

## Intake

Before implementation, verify:

- target type: protein, protein complex, antibody-antigen, protein-DNA, protein-RNA, protein-ligand, peptide, membrane protein, enzyme, mutant, or pathway member
- available sequence, species, isoform, domain, mutation, post-translational modification, ligand, cofactor, metal, pH, protonation state, and binding-site evidence
- experimental structures from PDB, predicted structures, templates, homologs, active conformations, and known ligands
- task endpoint: structural hypothesis, docking pose, ranking, virtual screening, MD stability, binding free energy, or mechanistic figure
- compute limits, GPU availability, database size, and license constraints

## Protein Structure Prediction

Current route:

1. Search PDB and AlphaFold DB before predicting a new structure.
2. Check isoform, domain boundaries, signal peptide, transmembrane regions, disorder, PTMs, ligands, cofactors, metal ions, and oligomeric state.
3. Use `AlphaFold`, `ColabFold`, `AlphaFold-Multimer`, `AlphaFold 3`, `Chai-1`, `Boltz`, `ESMFold`, `RoseTTAFold`, or comparable tools according to molecule type and access.
4. For protein-ligand, protein-DNA, protein-RNA, or complex predictions, record model limitations and benchmark status.
5. Validate predicted structures with confidence metrics, literature, known domains, active-site geometry, conserved residues, and external structures when available.
6. Treat low-confidence regions, disordered regions, and ligand poses from structure predictors as hypotheses unless supported by orthogonal evidence.

Required figures:

- domain architecture and sequence feature diagram
- predicted structure colored by pLDDT or equivalent confidence
- PAE or inter-chain confidence heatmap when supported
- template or homolog superposition
- active site, mutation, PTM, interface, or ligand-pocket view
- confidence and coverage summary table

## Molecular Docking

Current route:

1. Prepare receptor structure, remove artifacts, choose chains, add hydrogens, assign protonation, handle cofactors, waters, metals, and missing residues deliberately.
2. Prepare ligands with stereochemistry, tautomers, protonation states, conformers, and charge states.
3. Define docking site from known ligand, pocket prediction, mutation site, literature, AlphaFold/complex prediction, or unbiased blind docking when justified.
4. Use `AutoDock Vina`, `GNINA`, `Smina`, `rDock`, `DiffDock`, or commercial tools according to question and validation options.
5. Validate the docking setup by redocking known ligands or using benchmark structures when available.
6. Rank by score, pose plausibility, interaction consistency, known pharmacophore, and reproducibility across methods. Do not rank only by one docking score.

Required figures:

- receptor preparation and pocket definition figure
- 3D docking pose for top ligands
- 2D ligand-interaction diagrams
- docking score distribution and top-ligand table
- pose cluster or RMSD plot when multiple poses are generated
- redocking RMSD or known-ligand validation plot when controls exist
- cross-tool concordance plot for high-value claims

Primary preparation and inspection tools:

- PDBFixer, OpenBabel, Meeko, PDB2PQR, PropKa, Reduce, fpocket, DoGSiteScorer, PLIP, ProLIF, LigPlot+, PyMOL, ChimeraX

## Protein, Peptide, Antibody, And Complex Docking

Current route:

1. Define whether the task is protein-protein, peptide-protein, antibody-antigen, protein-DNA, protein-RNA, or protein-ligand docking.
2. Use experimental complex structures or known interface residues when available.
3. Use AlphaFold-Multimer, AlphaFold 3, Chai-1, Boltz, HADDOCK, ClusPro, HDOCK, RosettaDock, PatchDock, or LightDock according to molecule type and access.
4. Validate interface plausibility with known residues, mutational evidence, conservation, electrostatics, buried surface area, and external literature.
5. For peptide antigens or pMHC complexes, connect to `immunopeptidomics.md`.

Required figures:

- complex pose and interface overview
- interface residue and contact map
- buried surface area or interface-score distribution when available
- cluster or pose agreement plot
- mutation, peptide, antibody CDR, or domain-specific interface panels

## Molecular Dynamics

Current route:

1. Use MD only when dynamic stability, conformational change, solvent exposure, membrane context, or binding-site stability matters.
2. Prepare protein, ligand, force field, water model, ions, box, restraints, minimization, NVT, NPT, and production settings.
3. Use `GROMACS`, `OpenMM`, `AMBER`, `NAMD`, or equivalent tools according to environment and force-field needs.
4. Run replicates when conclusions depend on stability. Short single trajectories are exploratory.
5. Monitor simulation stability before interpreting biology.
6. For ligand binding, add MM/PBSA, MM/GBSA, alchemical free energy, umbrella sampling, or enhanced sampling only when the setup is defensible.

Required figures:

- system setup figure and simulation protocol table
- energy, temperature, pressure, density, and equilibration diagnostics
- protein and ligand RMSD
- RMSF per residue
- radius of gyration, SASA, hydrogen bonds, salt bridges, contacts, and distance time series
- PCA, clustering, free-energy landscape, or conformational state plots when used
- final representative structures and binding-site interaction persistence plots

Primary analysis tools:

- MDAnalysis, MDTraj, CPPTRAJ, gmx_MMPBSA, ProLIF, PLIP, PyMOL, ChimeraX

## Virtual Screening And ADMET

Current route:

1. Define compound source, library version, filtering rules, duplicates, salts, PAINS, reactive groups, and allowed chemical space.
2. Run ligand preparation before screening.
3. Use structure-based screening when a reliable target structure and binding site exist.
4. Use ligand-based screening, QSAR, similarity, pharmacophore, or graph models when known active ligands dominate evidence.
5. Add ADMET, toxicity, drug-likeness, synthetic accessibility, novelty, and patent or availability checks when prioritizing candidates.
6. For transcriptome-derived drug prediction, connect results to `single-cell-advanced.md` and `bulk-inference.md` before claiming drug mechanism.

Required figures:

- screening workflow diagram
- library filtering summary
- docking or model-score distribution
- top-compound interaction panels
- ADMET and drug-likeness radar or heatmap
- chemical similarity or scaffold diversity plot
- target-pathway or expression-rescue plot when transcriptomic drug prediction is used

## Source Index

Last checked: 2026-05-28.

- AlphaFold 2 paper: https://www.nature.com/articles/s41586-021-03819-2
- AlphaFold 3 paper: https://www.nature.com/articles/s41586-024-07487-w
- Chai-1 repository: https://github.com/chaidiscovery/chai-lab
- Chai-1 technical report: https://chaiassets.com/chai-1/paper/technical_report_v1.pdf
- Boltz-1: https://boltz.bio/boltz1
- AutoDock Vina documentation: https://autodock-vina.readthedocs.io/
- PDBFixer: https://github.com/openmm/pdbfixer
- OpenBabel: https://openbabel.org/docs/
- Meeko: https://github.com/forlilab/Meeko
- PDB2PQR: https://pdb2pqr.readthedocs.io/
- fpocket: https://github.com/Discngine/fpocket
- PLIP: https://github.com/pharmai/plip
- ProLIF: https://prolif.readthedocs.io/
- LigPlot+: https://www.ebi.ac.uk/thornton-srv/software/LigPlus/
- PyMOL: https://pymol.org/
- ChimeraX: https://www.cgl.ucsf.edu/chimerax/
- GNINA paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC8191141/
- GNINA repository: https://github.com/gnina/gnina
- DiffDock repository: https://github.com/gcorso/DiffDock
- HADDOCK: https://www.bonvinlab.org/software/haddock2.4/
- ClusPro: https://cluspro.org/
- RosettaDock: https://docs.rosettacommons.org/docs/latest/application_documentation/docking/docking-protocol
- GROMACS documentation: https://manual.gromacs.org/documentation/2024.0/index.html
- OpenMM: https://openmm.org/
- AMBER: https://ambermd.org/
- MDAnalysis: https://www.mdanalysis.org/
- MDTraj: https://mdtraj.org/
- gmx_MMPBSA: https://valdes-tresanco-ms.github.io/gmx_MMPBSA/
- RDKit documentation: https://www.rdkit.org/docs/
- Therapeutics Data Commons: https://tdcommons.ai/
- SwissADME: http://www.swissadme.ch/
