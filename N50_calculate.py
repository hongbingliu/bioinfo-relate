#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys, getopt
import re

def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:G:g:")
	input_file = ""
	output_file = ""
	h = ""
	g = ""
	G = 0
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-G":
			G = value
		elif op == "-g":
			g = value
		elif op == "-h":
			h = "useages:calculate the N50 length of transcripts or genes use *.genes_lengths.txt or *.trans_lengths.txt(the Python packages : pandas and numpy be used)\n-i : inputfile\n-o : outputfile\n-G <int>: 0 or 1, 0:genes N50, 1:transcripts N50(default : 0)\n\noptional:\n\t-g : cluster.txt(if you want to calculate the N50 length of transcripts in corset)"
	return input_file,output_file,G,g,h

def trs_main(input_file,g):

	all = []
	with open(g, 'r') as fh:
		for i in fh:
			i = i.split("\t")[0]
			all.append(i)
	data = pd.DataFrame(pd.read_table(input_file,index_col = 'transcript_id'))
	data = data.ix[all].sort(["length"],ascending = False)
	data = data['length']

	sum_50 = data.sum()/2

	count = 0
	sum = 0
	for i in data:
		count +=1
		sum +=float(i)
		if sum >= sum_50:
			break
	return i

def main(inputfile):

	data = pd.DataFrame(pd.read_table(inputfile))
	data = (data.sort(["length"],axis = 0,ascending = False))
	data = data.iloc[:,1]
	sum_50 = data.sum()/2

	count = 0
	sum = 0
	for i in data:
		count +=1
		sum +=float(i)
		if sum >= sum_50:
			break
	return i

def write(out):

        fout = open(output_file, 'w')
        fout.write(str(out))
        fout.close()

if __name__ == "__main__":
	input_file,output_file,G,g,h = get_option()
	if str(h) == "":
		if str(G) == "1":
			out = trs_main(input_file,g)
			if output_file == "":
				print ("N50 is " + str(out))
			else:
				write(out)
		else:
			out = main(input_file)
			if output_file == "":
				print ("N50 is " + str(out))
			else:
				write(out)
		
	else:
		print (h)
