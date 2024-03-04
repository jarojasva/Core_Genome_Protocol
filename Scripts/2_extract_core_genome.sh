# -*- coding: utf-8 -*- # NAME [2_extract_core_genome]  Version [1.0]
# AUTHOR  Jorge Alexander Rojas Vargas
# CREATED (2024-02)
# USAGE ./2_extract_core_genome
# DESCRIPTION
# Extract the fasta file(s) of the core-genome

#!/bin/bash

# Iterate over the names of the proteomes
for i in *.faa; do

  # Extract sequences and remove protein names
  while read ID; do grep -m 1 -A 2 -Ff <(echo "$ID" | sed 's/^[ \t]*//;s/[ \t]*$//') $i; done < ${i%.faa}_codes.txt > ${i%.faa}_order_seq.fasta
  
  # If ${i%.faa}_order_seq.fasta is not generated, then run the next command, and rerun the script:
  # sed -i 's/\r$//' 2_extract_core_genome.sh

  # Remove '>' characters and line breaks
  grep -v ">" ${i%.faa}_order_seq.fasta | tr -d '\n' > ${i%.faa}_seq_line_breaks.fasta

  # Add a name to the concatenated sequences
  echo ">${i%.faa}_core_genome" | cat - ${i%.faa}_seq_line_breaks.fasta > ${i%.faa}_core_genome.faa

  # Remove temporary files
  rm ${i%.faa}_codes.txt
  rm ${i%.faa}_order_seq.fasta
  rm ${i%.faa}_seq_line_breaks.fasta

done

# Add a newline at the end of each file
for file in *_core_genome.faa; do echo >> "$file"; done

# Concatenate the files into a single file named concatenated_core_genomes.faa
cat *_core_genome.faa > concatenated_core_genome.faa