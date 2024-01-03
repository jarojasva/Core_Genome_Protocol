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

3- Execute Proteinortho, comparing your .faa file(s) 
```sh
proteinortho Directory_with_proteomes/*.faa -identity=50 -conn=0.3 -project=output_proteinortho
```
4- Define your core genome, protein families contained in 100% (https://doi.org/110.1128/AEM.02411-13) or 95% of your genomes (https://doi.org/10.1038/s41467-023-43802-1).

5- Run the *0_extract_codes* script to extract the codes de las proteínas del primer isolate (columna 4) in your output_proteinortho.tsv file
```sh
python 0_extract_codes.py
```
6- Coloca en el mismo directorio el archivo generado codes_file.txt y el .faa file del primer isolate (columna 4) in your output_proteinortho.tsv file

7- Run the *1_extract_protein_names* script to extract the protein names of the core genome (list_protein_names.txt)
```sh
python 1_extract_protein_names.py
```

### Part 2 - Extract the core genome

1- Put in the same directory your .faa files, the late generated list_protein_names.txt and the *2_extract_core_genome* script

2- Run the *0_extract_codes* script to extract the core genome of each isolate and the concatenated core genome fasta
```sh
./2_extract_core_genome.sh
```
3- Enjoy your core genomes files
