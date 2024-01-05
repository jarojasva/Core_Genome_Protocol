# -*- coding: utf-8 -*- # NAME [2_extract_core_proteome]  Version [1.0]
# AUTHOR  Jorge Alexander Rojas Vargas
# CREATED (2024-01)
# USAGE ./2_extract_core_proteome
# DESCRIPTION
# Extract the fasta file(s) of the core proteome

#!/bin/bash

# Iterate over the names of the proteomes
for i in *.faa; do

  # Extract sequences and remove protein names
  while read ID; do grep -m 1 -A 2 -Ff <(echo "$ID" | sed 's/^[ \t]*//;s/[ \t]*$//') $i; done < ${i%.faa}_codes.txt > ${i%.faa}_order_seq.fasta
  
  # If ${i%.faa}_order_seq.fasta is not generated, then run the next command, and rerun the script:
  # sed -i 's/\r$//' 2_extract_core_proteome.sh

  # Remove '>' characters and line breaks
  grep -v ">" ${i%.faa}_order_seq.fasta | tr -d '\n' > ${i%.faa}_seq_line_breaks.fasta

  # Add a name to the concatenated sequences
  echo ">${i%.faa}_core_proteome" | cat - ${i%.faa}_seq_line_breaks.fasta > ${i%.faa}_core_proteome.faa

  # Remove temporary files
  rm ${i%.faa}_codes.txt
  rm ${i%.faa}_order_seq.fasta
  rm ${i%.faa}_seq_line_breaks.fasta

done

# Add a newline at the end of each file
for file in *_core_proteome.faa; do echo >> "$file"; done

# Concatenate the files into a single file named concatenated_core_proteomes.faa
cat *_core_proteome.faa > concatenated_core_proteome.faa