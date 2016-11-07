#!/usr/bin/env python

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
			h = "useages:showing the distribution of genes.(used *.genes_lengths.txt)\n-i : inputfile\n-o : outputfile(without this command, the result will output the screen)\n"
	return input_file,output_file,h

def main(input_file):
	d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = d9 = d10 = d11 = d12 = d13 = d14 = d15 = d16 = d17 = d18 = d19 = d20 = d21 = d22 = d23 = d24 = d25 = d26 = d27 = d28 = d29 = 0
	with open(input_file) as f:
		for i in f:
				try:
					s = float(i.split("\t")[1])
				except:
					continue
				#print (s)
				if int(s) < 300:
					d1 +=1
				elif int(s) < 400:
					d2 +=1
				elif int(s) < 500:
					d3 +=1
				elif int(s) < 600:
					d4 +=1
				elif int(s) < 700:
					d5 +=1
				elif int(s) < 800:
					d6 +=1
				elif int(s) < 900:
					d7 +=1
				elif int(s) < 1000:
					d8 +=1
				elif int(s) < 1100:
					d9 +=1
				elif int(s) < 1200:
					d10+=1
				elif int(s) <1300:
					d11+=1
				elif int(s) <1400:
					d12+=1
				elif int(s) <1500:
					d13+=1
				elif int(s) <1600:
					d14+=1
				elif int(s) <1700:
					d15+=1
				elif int(s) <1800:
					d16+=1
				elif int(s)<1900:
					d17+=1
				elif int(s)<2000:
					d18+=1
				elif int(s)<2100:
					d19+=1
				elif int(s)<2200:
					d20+=1
				elif int(s)<2300:
					d21+=1
				elif int(s)<2400:
					d22+=1
				elif int(s)<2500:
					d23+=1
				elif int(s)<2600:
					d24+=1
				elif int(s)<2700:
					d25+=1
				elif int(s)<2800:
					d26+=1
				elif int(s)<2900:
					d27+=1
				elif int(s)<3000:
					d28+=1
				else:
					d29+=1

	return d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29

def write(out):

        fout = open(output_file, 'w')
        fout.write(str(out))
        fout.close()

if __name__ == "__main__":
	input_file,output_file,h = get_option()
	if str(h) == "":
		out = main(input_file)
		if output_file == "":
			print (out)
		else:
			write(out)
	else:
		print (h)
