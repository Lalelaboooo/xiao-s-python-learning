import sys
import os
import glob

#input_file = sys.argv[1]
#print("Output #144:")
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print("{}".format(row.strip()))




#read multiple files
print("Output #145:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.csv')):
    with open(inout_file, 'r',newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))