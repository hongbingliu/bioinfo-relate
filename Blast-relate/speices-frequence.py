#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys, getopt
import re

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
			h = "useages:caculate the frequence of each speice.\n-i : inputfile\n-o : outputfile"
	return input_file,output_file,h

def main(inputfile):
	da = pd.read_table(inputfile,header = None)
	data = pd.DataFrame(pd.read_table(inputfile,header = None))
	da = da[1]
	counts = da.value_counts()
	return counts

def write(out):

        fout = open(output_file, 'w')
        fout.write(str(out))
        fout.close()

if __name__ == "__main__":
	input_file,output_file,h = get_option()
	if str(h) == "":
		out = main(input_file)
		write(out)
	else:
		print (h)
