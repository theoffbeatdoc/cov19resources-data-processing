import re

#input file
fin = open("RawDataSource.txt", "rt")
#output file to write the result to
fout = open("RawData.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	#fout.write(line.replace('pyton', 'python'))
	fout.write((re.sub('[a-zA-Z]', '', line)).replace(' ','').replace('\t','').replace('\n',',').replace(',,',','))
#close input and output files
fin.close()
fout.close()
