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
			h = 'useages:\nremove the sequence which contain "N"\n-i : inputfile\n-o : outputfile\n'
	return input_file,output_file,h

def main(input_file, output_file):
	fout = open(output_file, 'w')
	all = []
	count = 1
	with open (input_file) as f:
		for i in f:
			#print (i)
			if '<Hit_id>' in i:
				pass
			elif '<Hit_def>' in i:
				st = i.find('<Hit_def>') + len('<Hit_def>')
				sd = i.find('</Hit_def>',st)
				d = i[st:sd].split(" ")
				id = d[0]
				de = i.replace((str(id) + ' '),'')
				ac = (id.split('|')[3]).split('.')[0]
				fout.write('  <Hit_id>' + id + '</Hit_id>\n')
				fout.write(de)
				fout.write('  <Hit_accession>' + ac + '</Hit_accession>\n')
			elif '<Hit_accession>' in i:
				pass
			else:
				fout.write(i)
			count += 1
	fout.close()

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
