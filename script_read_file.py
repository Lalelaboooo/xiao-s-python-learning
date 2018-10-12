import os
import sys
import glob

input_file = sys.argv[1]

print("Output #143:")
filereader = open(input_file, 'r')
for row in filereader:
    print(row.strip())
filereader.close()