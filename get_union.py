import sys, getopt
import re
import time
def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hL:R:l:r:")
	input_file_L = ""
	input_file_R = ""
	output_file_L = ""
	output_file_R = ""
	h = ""
	for op, value in opts:
		if op == "-L":
			input_file_L = value
		elif op == "-R":
			input_file_R = value
		elif op == "-l":
			output_file_L = value
		elif op == "-r":
			output_file_R = value
		elif op == "-h":
			h = "useages:\nget the union between left reads and right reads\n-L : inputfile(Left)\n-R : inputfile(Right)\n-l : outputfile(Left)\n-r : outputfile(Right)"
	return input_file_L,input_file_R,output_file_L,output_file_R,h

def get_union(input_file_L,input_file_R):
	count = -1
	L = []
	R = []
	with open(input_file_L) as fL:
		for i in fL:
			count +=1
			if ((int(count)) % 4) == 0:
				tmp = str(i).split(" ")[0]
				L.append(str(tmp) + "\n")
	print ("left is OK")
	count = -1
	with open(input_file_R) as fR:
		for i in fR:
			count +=1
			if ((int(count)) % 4) == 0:
				tmp = str(i).split(" ")[0]
				R.append(str(tmp) + "\n")
	print ("right is OK")
	un = list(set(L).intersection(set(R)))	
	return un

def main(input_file_L,input_file_R,output_file_L,output_file_R,reference):
	foutL = open(output_file_L, 'w')
	foutR = open(output_file_R, 'w')
	
#	ref = open(reference)
#	ref = ref.read()
	ref = dict.fromkeys(reference,True)
	#print (ref)
	count = -1
	with open(input_file_L) as fL:
			for i in fL:
				count +=1
				if ((int(count)) % 4) == 0:
						du = 1
						tmp = str(i).split(" ")[0] + "\n"
						if tmp in ref:
							foutL.write(i)
							#print (".....")
							du = 0
				elif du == 0:
					foutL.write(i)

	print ("left is OK")
	count = -1
	with open(input_file_R) as fR:
		for i in fR:
			count +=1
			if ((int(count)) % 4) == 0:
				du = 1
				tmp = str(i).split(" ")[0] + "\n"
				if str(tmp) in ref:
					foutR.write(i)
					du = 0
			elif du == 0:
					foutR.write(i)
	print ("right is OK")

if __name__ == "__main__":
	time_start = time.time()
	input_file_L,input_file_R,output_file_L,output_file_R,h = get_option()

	if str(h) == "":
		reference = get_union(input_file_L,input_file_R)
		main(input_file_L,input_file_R,output_file_L,output_file_R,reference)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
