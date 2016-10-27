import linecache
import sys, getopt
import os
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
			h = "useages:\ncalculate the Q20 proportion\n-i : inputfile\n-o : outputfile(without this command, the result will output the screen)"
	return input_file,output_file,h

def get_content(input_file):
	count_20 = 0
	count = 1
	count_sum = 0
	with open (input_file) as f:
		for i in f:
			if (int(count) % 4) == 0:
				for each in i[:-1]:
					num = ord(each) - 33
					if num > 20 :
						count_20 +=1
				count_sum += (len(i)-1)
				#print (len(str(i)))
			count += 1
			#print (count_sum)
	return count_20,count_sum

def write():

	fout = open(output_file, 'w')
	out = "Q20:" + str (count) + "\n" + "sum:" + str (count_sum) + "\n" + "Q20%:" + str (count/count_sum)

	fout.write(out)
	fout.close()

def output():

	print("Q20:" + str(count) + "\n" + "sum:" + str(count_sum) + "\n" + "Q20%:" + str(count / count_sum))

if __name__ == "__main__":
	time_start = time.time()

	input_file, output_file, h = get_option()
	if str(h) == "":
		count, count_sum = get_content(input_file)
		if output_file == "":
			output()
		else:
			write()
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
