#!/usr/bin/env python

import sys, getopt
import re
import time

def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
	input_file = ""
	output_file = ""
	h = ""
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			h = 'useages:\nBuild the WEGO native format"N"\n-i : inputfile\n-o : outputfile\n'
	return input_file,output_file,h

def main(input_file, output_file):
	fout = open(output_file, 'w')
	all = ''
	count = 1
	tmp = ''
	with open (input_file) as f:
		for i in f:
			t = i.split('\t')[0]
			go = i.split('\t')[1]
			if "GO" in go:
				if t != tmp:
					fout.write(all + "\n")
					tmp = t
					all = i[:-1]
				
				else:
					all = all + '\t' + go[:-1]
	fout.close()

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)

