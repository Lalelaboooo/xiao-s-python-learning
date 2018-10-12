import os
import sys
import glob
input_file = sys.argv[1]

print("Output #143: ")
filereader = open('/Users/hanxiao/My_python/file_to_read.txt','r')
for row in filereader:
	print(row.strip)
filereader.close()

#new ways to read a file
#input_file = sys.argv[1]
#print("Output #144:")
#with open (input_file,'r', newline='') as filereader:
#	for row in filereader:
#		print("{}".format(row.strip()))

#read multiple files
#print("Output #145: ")
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#	with open(input_file,'r', newline='') as filereader:
#		for row in filereader:
#			print("{}".format(row.strip()))
