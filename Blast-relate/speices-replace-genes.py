#!/usr/bin/env python

import sys, getopt
import re
import time
import os

def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:f:o:")
	input_file = ""
	output_file = ""
	ref = ""
	h = ""
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-f":
			ref = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			h = 'useages:\replace the gene name in match_out result to speices name\n-i : inputfile\n-f : ref\n-o : outputfile\n'
	return input_file,output_file,ref,h

def main(input_file, ff,output_file):
	fout = open(output_file, 'w')
	fh = open(input_file, 'r')
	fh = fh.read()
	#print (fh)
	count = 1
	with open (ff) as f:
		for i in f:
				name = i.split("\t")[0]
				sp = i.split("\t")[1][:-1]
				print (name + sp)
				fh = fh.replace(name,sp)
				print (count)
				count+=1
				
	fout.write(fh)
	fout.close()
'''
			m = "grep " + "'" + str(i[:-1]) + "'" + " " + ff
			print (m)
			out = os.popen(m)
			out = out.read()
			out = out[(out.find("[") +1):out.find("]")]
			out = i[:-1] + "\t" + out + "\n"
			fout.write(out)
'''

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,f,h = get_option()
	if str(h) == "":
		main(input_file, f,output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
