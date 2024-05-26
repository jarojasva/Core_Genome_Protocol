# A protocol to extract the Core-Genome (only single copy orthologs)

Hi there! 

I share with you a protocol I've developed for extracting the core-genome (only single copy orthologs) from a set of genomes. This approach uses:

1- Your preferred annotation software

2- Proteinortho (https://gitlab.com/paulklemm_PHD/proteinortho)

3- Python

4- Bash

The culmination of this protocol is a concatenated amino acid FASTA file (*concatenated_core_genome.faa*) containing the core-genome (only single copy orthologs). This file can be used for downstream analyses, such as alignment and phylogenetic inference.

## Protocol

### Part 1 - Extracting the protein codes of each proteome

1- Install Proteinortho software in your computer or server (https://anaconda.org/bioconda/proteinortho)

2- Annotate your genome(s) using your preferred annotation software and save the resulting .faa file(s) in a designated directory

3- Execute Proteinortho, comparing your .faa file(s)
```sh
proteinortho Directory_with_proteomes/*.faa -identity=50 -project=output_proteinortho
```
> [!NOTE]
> Change the identity percentage if you want a more relaxed (<50) or stricter (>50) orthology prediction

4- Put in the same directory the *1_extract_codes_files.py* script and your output_proteinortho.tsv file

5- Run the *1_extract_codes_files.py* script to extract the protein codes for each proteome
```sh
python 1_extract_codes_files.py <proteinortho_file> <core>
```
> [!NOTE]
>Define your core value (the percentage of genomes that will be part of the core genome). It must be a value between [0-100]. The traditional "core-genome" is defined as the contained in 100% (core value 100) (https://doi.org/110.1128/AEM.02411-13) or 95% of your isolates (core value 95) (https://doi.org/10.1038/s41467-023-43802-1)
f.i. If you want to obtain the proteins contained in 95% of your isolates, then run:
>```sh
>python 1_extract_codes_files.py <proteinortho_file> 95
>``` 

### Part 2 - Extract the core-genome

1- Put in the same directory your .faa files, the late generated genome_name_codes.txt files and the *2_extract_core_genome.sh* script

2- Run the *2_extract_core_genome.sh* script to extract the core-genome of each isolate and to obtain the concatenated core-genome fasta file
```sh
./2_extract_core_genome.sh
```
3- Enjoy your core genome files

## Example trial

1- Download the *files* directory. It contains an output_proteinortho.tsv and ten proteome files (.faa)

2- Extract the codes of the proteins contained in 100% of proteomes:
```sh
python 1_extract_codes_files.py output_proteinortho.tsv 100
```
3- Extract the core genome files:
```sh
./2_extract_core_genome.sh
```

