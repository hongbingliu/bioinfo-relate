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
			h = 'useages:From nr database import gene-to-speices table\n-i : inputfile\n-o : outputfile\n'
	return input_file,output_file,h

def main(input_file,output_file):
	fout = open(output_file, 'w')
	with open (input_file) as f:
		for i in f:
			if i[0] == ">":
				name = i[1:i.find(" ")]
				n = i[(i.find("[") +1):i.find("]")]
					
				n = name + "\t" + n + "\n"
				#print (n)
				fout.write(n)
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

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file,output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
