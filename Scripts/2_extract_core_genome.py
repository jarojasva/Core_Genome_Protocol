# -*- coding: utf-8 -*- # NAME [2_extract_core_genome_v3]  Version [3.0]
# AUTHOR  Jorge Alexander Rojas Vargas
# CREATED (2024-08)
# USAGE python 2_extract_core_genome.py
# DESCRIPTION
# Extract the protein sequences of the core proteome

import os
import glob

def extract_sequences(faa_file, codes_file):
    with open(faa_file, 'r') as faa, open(codes_file, 'r') as codes:
        sequences = faa.read().split('>')
        sequences_dict = {seq.split('\n', 1)[0]: '>' + seq for seq in sequences if seq}

        with open(f"{os.path.splitext(faa_file)[0]}_order_seq.fasta", 'w') as out_fasta:
            for ID in codes:
                ID = ID.strip()
                for header, sequence in sequences_dict.items():
                    if ID in header:
                        out_fasta.write(sequence)
                        break


def concatenate_sequences():
    with open("concatenated_core_genome.faa", 'w') as out_file:
        for file in glob.glob("*_core_genome.faa"):
            with open(file, 'r') as f:
                out_file.write(f.read().replace("_core_genome", "") + '\n')


def main():
    faa_files = glob.glob("*.faa")
    for faa_file in faa_files:
        codes_file = f"{os.path.splitext(faa_file)[0]}_codes.txt"
        extract_sequences(faa_file, codes_file)

        with open(f"{os.path.splitext(faa_file)[0]}_order_seq.fasta", 'r') as order_seq, \
                open(f"{os.path.splitext(faa_file)[0]}_seq_line_breaks.fasta", 'w') as seq_line_breaks:
            for line in order_seq:
                if not line.startswith('>'):
                    seq_line_breaks.write(line.strip())

        with open(f"{os.path.splitext(faa_file)[0]}_core_genome.faa", 'w') as core_genome, \
                open(f"{os.path.splitext(faa_file)[0]}_seq_line_breaks.fasta", 'r') as seq_line_breaks:
            core_genome.write(f">{os.path.splitext(faa_file)[0]}_core_genome\n")
            core_genome.write(seq_line_breaks.read())

        os.remove(codes_file)
        os.remove(f"{os.path.splitext(faa_file)[0]}_order_seq.fasta")
        os.remove(f"{os.path.splitext(faa_file)[0]}_seq_line_breaks.fasta")

    concatenate_sequences()


if __name__ == "__main__":
    main()
