import sys, getopt, os

def split(file_name, number_of_files):
	file = open(file_name)
	size_per_file = int(os.stat(file_name).st_size)/number_of_files
	generated_files = []
	
	for i in range(1,number_of_files+1):
		#creating a new file TODO: get path argument and create new folder.
		f = open(file_name+'_'+str(i),'w')
		generated_files.append(f)
	
	y = 0
	with file as infile:
		for line in infile:
			generated_files[y].write(line)
			if int(os.stat(generated_files[y].name).st_size) >= size_per_file:
				if y+1 < int(os.stat(generated_files[y].name).st_size):
					y+=1
	
	#close all files
	for gf in generated_files:
		gf.close()

def main(argv):
	#sys.argv[1] is the input file  | sys.argv[2] the number of files
	split(sys.argv[1],int(sys.argv[2]))

if __name__ == "__main__":
   main(sys.argv[1:])

