#!/usr/bin/python

import re

#4
with open("sequence.txt", "r") as f: 
    seq1=f.read()

#5
seq1=re.sub(" ", "", seq1)
seq1=re.sub("\d", "", seq1)
print (seq1)

#remove first line

seq55=re.sub("^>[^\n]+\n","", seq1)
seq2=re.sub("\n", "", seq55)


#6
rna=re.sub("T", "U", seq2)
print(rna)

#7 search for EcoRI sites
l=len(seq2)
c=0
pos=""

for i in range(0, l-6-1):
    if seq2[i:i+6]=="GAATTC":
        c+=1
        pos=pos + str(i+1) + " "


print ("EcoRI restriction site was found " + str(c) + " times, at positions: " + pos)


#8
import string

seq2lo=seq2.translate(seq2.maketrans("ATGC", "atgc"))
ecseq=re.sub("gaattc", "GAATTC", seq2lo)
print(ecseq)