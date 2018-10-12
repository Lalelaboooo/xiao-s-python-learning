import glob
import os
import sys

inputPath = sys.argv[1]

for input_file in glob.glob(os.path.join(inputPath,'*.csv')):
	with open (input_file, 'r') as filereader:
		for row in filereader:
			print("{}".format(row.strip()))
