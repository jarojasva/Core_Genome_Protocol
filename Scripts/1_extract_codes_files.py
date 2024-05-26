# -*- coding: utf-8 -*- # NAME [1_extract_codes_files]  Version [2.0]
# AUTHOR  Jorge Alexander Rojas Vargas
# CREATED (2024-05)
# USAGE python 1_extract_codes_files.py proteinortho_file core
# DESCRIPTION
# Extract the protein codes of the core proteome from the .tsv Proteinortho output file

import argparse
import csv
import os
import math

# Script arguments
parser = argparse.ArgumentParser()
parser.add_argument("proteinortho_file", help="the tsv file from Proteinortho to read")
parser.add_argument("core", type=float, help="Percentage of proteomes that will be part of the core proteome [0-100]")
args = parser.parse_args()

if args.core is None:
    print("Error: Add the percentage of proteomes that will be part of the core proteome")
    exit(1)  # Exit the script with an error code

elif args.core < 0 or args.core > 100:
  print("Error: The value of the 'core' parameter must be between 0 and 100")
  exit(1)

with open(args.proteinortho_file, "r") as infile:
    reader = csv.reader(infile, delimiter="\t")
    header = next(reader)
    data = list(reader)

    new_table_0 = [header[0:]]
    for row in data:
        # Comparación de la segunda y primera columna
        if int(row[1]) <= int(row[0]):
            new_table_0.append(row[0:])

# Guardar la tabla new_table_0 como archivo CSV
with open("new_table_0.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerows(new_table_0)

# Open the input file
with open("new_table_0.csv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t")

    # Get the number of proteomes from the second row, first column
    header_row = next(reader)  # Skip the header row
    second_row = next(reader)
    number_proteomes = int(second_row[0])

    # Calculate the new number of proteomes (rounded down)
    new_number_proteomes = math.floor(args.core/100 * number_proteomes)
    new_number_proteomes = max(new_number_proteomes, 1)  # Ensure at least 1 proteome
    # print(new_number_proteomes)

    # Create a new table with the first row
    new_table_1 = [header_row]

    # Iterate over the input file, adding rows that have number greater or equal to new_number_proteomes
    for row in reader:
        if int(row[0]) >= new_number_proteomes:  # Condition modified to include >=
            new_table_1.append(row)

    # Add the second row of the input file to the end of the new table
    new_table_1.append(second_row)

    # Filter rows containing ","
    filtered_rows = []
    for row in new_table_1[1:]:
        if not any(character in row[0] for character in [","]):
            filtered_rows.append(row)

    new_table_1 = [new_table_1[0]] + filtered_rows
    
    # Create a new table with a single code in each position
    new_table_2 = []
    for row in new_table_1[1:]:
        new_row = []
        new_row.append(row[0])
        for code in row[1:]:
            if "," in code:
                new_row.append(code.split(",")[0])
            else:
                new_row.append(code)
        new_table_2.append(new_row)

    # Add the first row of new_table_1 to new_table_2
    new_table_2.insert(0, new_table_1[0])

    # Create lists of the codes from the new_table_2
    for i in range(len(new_table_2[0])):
        # Get the name of the proteome
        proteome_name = new_table_2[0][i]

        # Create a list of the codes
        proteome_codes = []
        for row in new_table_2[1:]:
            proteome_codes.append(row[i])

        # Save the list to a file
        with open(f"{proteome_name}.txt", "w") as outfile:
            outfile.write("\n".join(proteome_codes))

    # Remove the lists created with the names of the first 3 columns of new_table_2.tsv
    for i in range(1, 3):
        proteome_name = new_table_2[0][i]
        os.remove(f"{proteome_name}.txt")

    # Remove the term ".faa" in the rest of names of files .txt
    for filename in os.listdir():
        if filename.endswith(".txt"):
            os.rename(filename, filename.replace(".faa", "_codes"))

    # Remove "*" of files_codes .txt
    for filename in os.listdir():
        if filename.endswith("_codes.txt"):
            with open(filename, "r") as infile:
                lines = infile.readlines()

            filtered_lines = []
            for line in lines:
                if "*" not in line:  # Filtrar filas sin "*"
                    filtered_lines.append(line)

            # Reescribir el archivo con las filas filtradas
            with open(filename, "w") as outfile:
                outfile.writelines(filtered_lines)

    # Remove the file "# Species.txt"
    os.remove("# Species.txt")

    # Add a new empty line at the end of proteome_codes files
    def add_empty_line(filename):
        with open(filename, "a") as outfile:
            outfile.write("\n")

    for filename in os.listdir():
        if filename.endswith("_codes.txt"):
            add_empty_line(filename)
