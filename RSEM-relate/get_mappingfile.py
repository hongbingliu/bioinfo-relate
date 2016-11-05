import sys, getopt
import re
def get_option():
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:l:")
	  input_file = ""
	  output_file = ""
	  input_file_2 = ""
	  h = ""
	  for op, value in opts:
		  if op == "-i":
			  input_file = value
		  elif op == "-f":
			  input_file_2 = value
		  elif op == "-o":
			  output_file = value
		  elif op == "-h":
			  #print (h)
			  h = "useages:get the mapping file used in rsem-prepare-reference\n-i : cluster.txt file\n-o : mapping.txt file used in rsem-prepare-reference\n-f : .faste file" 
	  return input_file,input_file_2,output_file,h

def get_trs(input_file_2):
	  all = []
	  with open(input_file_2) as f:
		  for i in f:
			  if re.findall('>.+len',str(i)):
				  s = (''.join(re.findall('>.+len',str(i)))[1:-4]) + "\n"
				  all .append(s)
	  return all

def main(input_file,all):
	  cl = []
	  with open (input_file) as fh:
		  for each in fh:
			  ea = (str(each)[:-1]).split("\t")
			  ea = ea[1] + "\t" + ea[0] + "\n"
			  cl.append(ea)
	  cd = ''.join(cl)
	  #print (all)
	  for i in all:
				  if str(i) in str(cd):
					  pass
				  else:
					  cl.append("Cluster-OUT" + "\t" + str(i))
	  return ''.join(cl)

def write(out):
    fout = open(output_file, 'w')
    fout.write(str(out))
    fout.close()

if __name__ == "__main__":
	  input_file,input_file_2,output_file,h = get_option()
	
	  if str(h) == "":
		  all = get_trs(input_file_2)
		  out = main(input_file,all)
		  write(out)
	  else:
		  print (h)

