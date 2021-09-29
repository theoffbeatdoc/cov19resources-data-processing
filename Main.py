import os
import re

def basedataprocess():
    #input file
    fin = open("BaseDataSource.txt", "rt")
    #output file to write the result to
    fout = open("BaseData.txt", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        #fout.write(line.replace('pyton', 'python'))
        fout.write((re.sub('[a-zA-Z]', '', line)).replace(' ','').replace('\t','').replace('\n',',').replace('/', ',').replace('-','').replace('(','').replace(')',''))
    #close input and output files
    fin.close()
    fout.close()
    print("Base Data Updated Successfully !")
    return


def rawdataprocess():
    #input file
    fin = open("RawDataSource.txt", "rt")
    #output file to write the result to
    fout = open("RawData.txt", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        #fout.write(line.replace('pyton', 'python'))
        text = (re.sub('[a-zA-Z]', '', line)).replace(' ','').replace('\t','').replace('\n',',').replace(',,',',').replace('-','')
        fout.write(text)
    
    #close input and output files
    fin.close()
    fout.close()
    print("Check if your raw data is perfect or not:")
    fout = open("RawData.txt", "rt")
    print(fout.readlines())
    fout.close()
    return

def process():
    rawdata = "RawData.txt"
    basedata = "BaseData.txt"
    dataset = set()
    r = open(rawdata, "r")
    b = open(basedata, "r")
    # print(f.read())
    x = str(r.read()).split(',', -1)
    y = str(b.read())
    for i in x:
        #print(i)
        s=re.search(i.strip(), y)
        if s == None:
            #print(i)
            dataset.add(i)
    r.close()
    b.close()
    print("Here are the new entries in the raw data that do not exist in the base data:")
    print(', '.join(dataset))
    return

def ui():
    loop=1
    while (loop==1):
        print(" ")
        print (""" The OffBeat Doc - COV-19 RESOURCES DATA PROCESSOR
        1. Enter Raw Data
        2. Process Data comparing with Base Data
        3. Change Base data
        4. Exit""")
        x = int(input())
        if x==1:
            print ("Enter Raw Data")
            lines = []
            while True:
                line = input()
                if line:
                    lines.append(line)
                else:
                    break
            text = '\n'.join(lines)
            rawwritesource = open("RawDataSource.txt", "wt")
            rawwritesource.write(text)
            rawwritesource.close()
            rawdataprocess()
        if x==2:
            process()
        if x==3:
            print ("Enter New Base Data")
            lines = []
            while True:
                line = input()
                if line:
                    lines.append(line)
                else:
                    break
            text = '\n'.join(lines)
            basewritesource = open("BaseDataSource.txt", "wt")
            basewritesource.write(text)
            basewritesource.close()
            basedataprocess()
        if x==4:
            loop=2
    print("Thank you.")

    
    
ui()