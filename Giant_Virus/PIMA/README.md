# PIMA
Phylogeny-informed MAG assessment (PIMA) is a automatic tool to assess the quality of giant virus MAGs.

This approach was designed to overcome the limitations caused by a lack of reference genomes, which impacts the accuracy of quality assessments for giant virus MAGs. This approach requires a guide tree of giant viruses that has been rerooted in accordance with the latest taxonomic classifications and evolutionary scenarios. Then, the relative evolutionary divergence (RED) values were calculated to classify taxonomic levels for each clade (e.g., order and family)72. Within a specific clade, MAG genes were annotated with orthologous groups (OGs); then, core genes in this clade were defined as those identified in more than 50% of the genomes in the clade.

Redundant genes in a MAG are defined as genes with more copies than the mode copy number (the most common number of copies) for the given genes across all MAGs in the evaluated lineage.

You can see metabat2_bin_1, metabat2_bin_6, metabat2_bin_13, metabat2_bin_1 are potential NCLDV bins.

## Dependencies
The pipeline is written in Python v3.9.16.
The pipeline requires Prodigal and HMMER3 for gene call and HMM searches.

## Citation
Fang, Yue, et al. "Genome-resolved year-round dynamics reveal a broad range of giant virus microdiversity." bioRxiv (2024). [link](https://www.biorxiv.org/content/10.1101/2024.07.08.602415v1)

## Contact
lingjie@kuicr.kyoto-u.ac.jp

