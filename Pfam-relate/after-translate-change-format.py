#!/usr/bin/env python

import sys, getopt
import re
def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:l:")
	input_file = ""
	output_file = ""
	h = ""#"useages:\n-i : inputfile\n-o : outputfile\n-f : the forward base number you trim\n-l : the last base number you trim "
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			#print (h)
			h = "useages:Change the format after translate the gene.fasta to protein.fasta\n-i : inputfile\n-o : outputfile " 
	return input_file,output_file,h

def main(input_file,output_file):
	fout = open(output_file, "w")
	count = 1
	with open (input_file) as fh:
			for i in fh:
				if '>' in i:
					i = i.split(' ')
					i = i[0]  + i[1] + '\n'
					#print (i)
					fout.write(i)
				else:
					fout.write(i)
				count += 1

if __name__ == "__main__":
	input_file,output_file,h = get_option()
	#input_file = input(":")
	if str(h) == "":
		out = main(input_file,output_file)
	else:
		print (h)

