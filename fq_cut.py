#!/usr/bin/env python

import sys, getopt
import re
def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:l:")
	input_file = ""
	output_file = ""
	f = ""
	l = ""
	h = ""#"useages:\n-i : inputfile\n-o : outputfile\n-f : the forward base number you trim\n-l : the last base number you trim "
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-f":
			f = value
		elif op == "-l":
			l = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			#print (h)
			h = "useages:\n-i : inputfile\n-o : outputfile\n-f;-l : base from <f> to the <l> " 
	return input_file,output_file,f,l,h

def main(input_file,output_file,f,l):
	fout = open(output_file, "w")
	count = 1
	with open (input_file) as fh:
			for i in fh:
				if ((int(count)) % 2) == 0:
					i = i[(int(f) - 1):(int(l))] + "\n"
					fout.write(i)
				else:
					fout.write(i)
				count += 1

if __name__ == "__main__":
	input_file,output_file,f,l,h = get_option()
	#input_file = input(":")
	if str(h) == "":
		out = main(input_file,output_file,f,l)
	else:
		print (h)
