# Python script to change the headers of a Fasta-file
# Usage: python Change_Headers_Fasta.py original_fasta_file(.fa) new_header_names(.txt) output(.fa)

import sys

# Open files
file_1 = open(sys.argv[1], "r") # Open input file 1
file_2 = open(sys.argv[2], "r") # Open input file 2
merged_file = open(sys.argv[3], "a") # Open file that will contain final information

# Replace headers in Fasta-file
for line in file_1:
	if ">" in line:
		merged_file.write(">" + file_2.readline().strip() + "\n")
	else:
		merged_file.write(line)

# Close files
file_1.close()
file_2.close()
merged_file.close()
