import os
import re

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
print(', '.join(dataset))
