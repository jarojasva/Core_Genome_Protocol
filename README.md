# A protocol to extract the Core Genome

Hi! Here is a protocol I developed for extracting the core genome from a group of genomes, based on the protein names. This protocol uses:

1- Proteinortho (https://gitlab.com/paulklemm_PHD/proteinortho)

2- Python scripts

3- Bash scripts

At the end, the concatenated amino acid fasta of the core genome will be obtained to then align (e.g. MAFFT) and perform your phylogenetic analyses.

## Protocol

### Part 1 - Extracting the protein names

1- Install Proteinortho software in your computer or server (https://anaconda.org/bioconda/proteinortho)

2- Annotate your genome(s) using your preferred annotation software and save the resulting .faa file(s) in a designated directory

3- Execute Proteinortho, comparing your .faa file(s). 
```sh
proteinortho Directory_with_proteomes/*.faa -identity=50 -project=output_proteinortho
```
**Note**: Change the identity percentage if you want a more relaxed (<50) or stricter (>50) analysis

4- Run the *0_extract_codes* script to extract the protein codes from the first isolate (column 4) in your output_proteinortho.tsv file
```sh
python 0_extract_codes.py output_proteinortho.tsv
```
**Note**: Define your core genome, protein families contained in 100% (https://doi.org/110.1128/AEM.02411-13) or 95% of your genomes (https://doi.org/10.1038/s41467-023-43802-1), changing the percentage in line X. Default value 95%

5- Run the *1_extract_protein_names* script to extract the protein names of the core genome (the generated list_protein_names.txt), using the .faa file and the codes_file.txt as input
```sh
python 1_extract_protein_names.py proteome_file.faa  codes_file.txt list_protein_names.txt
```

### Part 2 - Extract the core genome

1- Put in the same directory your .faa files, the late generated list_protein_names.txt and the *2_extract_core_genome* script

2- Run the *0_extract_codes* script to extract the core genome of each isolate and to obtain the concatenated core genome fasta file
```sh
./2_extract_core_genome.sh
```
3- Enjoy your core genome files
