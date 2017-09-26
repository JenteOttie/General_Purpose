# Python script to merge contents of two files line by line
# Usage: python Merge_Two_Files.py in_file1 in_file2 output_file

import sys

# Open files
file_1 = open(sys.argv[1], "r") # Open input file 1
file_2 = open(sys.argv[2], "r") # Open input file 2
merged_file = open(sys.argv[3], "a") # Open file that will contain final information

# Merge the two files line by line
for line in file_1:
        merged_file.write(line.rstrip() + "\t" + file_2.readline().strip() + "\n")

# Close files
file_1.close()
file_2.close()
merged_file.close()
