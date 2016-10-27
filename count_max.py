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
                        h = "useages:\nget the max length in all contigs or transcripts\n-i : inputfile\n-o : outputfile"
        return input_file,output_file,h

def main(input_file):
	max = 0
	with open(input_file) as f:
		for i in f:
			if re.findall('len=\d+',str(i)):
				s = (''.join(re.findall('len=\d+',str(i)))[4:])
				#print (s)
				if int(s) > max:
					max = int(s)
	#print (max)
	return max

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
