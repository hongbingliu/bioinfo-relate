#!/usr/bin/env python2

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
			h = "E-value distribution.\n-i : inputfile\n-o : outputfile\n"
	return input_file,output_file,h

def main(input_file, output_file):
	o = a = b = c = d = e = g = 0
	fout = open(output_file, 'w')
	with open (input_file) as f:
		for i in f:
			i = float(i[:-1])
			if i == 0:
				o +=1
			elif i < float(1e-150):
				a +=1
			elif i < float(1e-100):
				b +=1
			elif i < float(1e-50):
				c +=1
			elif i < 1e-10:
				d +=1
			else :
				g +=1
	out = str(o) + " " + str(a) + " " + str(b) + " " + str(c) + " " + str(d) +" " + str(g)
	fout.write(out)
			
	fout.close()

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
