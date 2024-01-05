# A protocol to extract the Core Proteome

## UNDER CONSTRUCTION !

Hi there! 

I share with you a protocol I've developed for extracting the core proteome from a set of genomes. This approach uses:

1- Proteinortho (https://gitlab.com/paulklemm_PHD/proteinortho)

2- Python

3- Bash

The culmination of this protocol is a concatenated amino acid FASTA file (*concatenated_core_genomes.faa*) containing the core proteome. This file can be used for downstream analyses, such as alignment and phylogenetic inference.

## Protocol

### Part 1 - Extracting the protein codes of each proteome

1- Install Proteinortho software in your computer or server (https://anaconda.org/bioconda/proteinortho)

2- Annotate your genome(s) using your preferred annotation software and save the resulting .faa file(s) in a designated directory

3- Execute Proteinortho, comparing your .faa file(s)
```sh
proteinortho Directory_with_proteomes/*.faa -identity=50 -project=output_proteinortho
```
**Note**: Change the identity percentage if you want a more relaxed (<50) or stricter (>50) analysis

4- Put in the same directory the *1_extract_codes_files.py* script and your output_proteinortho.tsv file

5- Run the *1_extract_codes_files.py* script to extract the protein codes for each proteome
```sh
python 1_extract_codes_files.py core
```
**Note**: Define your core value (the percentage of proteomes that will be part of the core proteome). It must be a value between [0-100]. The traditional "core-genome" is defined as the contained in 100% (core value 100) (https://doi.org/110.1128/AEM.02411-13) or 95% of your isolates (core value 95) (https://doi.org/10.1038/s41467-023-43802-1)
e.x. If you want to obtain the core proteome in 100% of your isolates, then run:
```sh
python 1_extract_codes_files.py 100
```

### Part 2 - Extract the core proteome

1- Put in the same directory your .faa files, the late generated proteome_name_codes.txt files and the *2_extract_core_proteome.sh* script

2- Run the *2_extract_core_proteome.sh* script to extract the core proteome of each isolate and to obtain the concatenated core proteome fasta file
```sh
./2_extract_core_proteome.sh
```
3- Enjoy your core genome files
