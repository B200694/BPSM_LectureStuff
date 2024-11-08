#!/bin/python3

## Import modules

import os, subprocess, shutil

### LOCAL SEQUENCE ###

## Split sequence into coding and non-coding parts

with open ("plain_genomic_seq.txt") as myfile:
    local_seq = myfile.read().rstrip().upper().replace("X","").replace("S","").replace("K","").replace("L","")

lCDS1 = local_seq[:63]
lCDS2 = local_seq[90:]
lNCS1 = local_seq[63:90]

print("Length of local sequence: ", len(local_seq))
print("Sum of coding and noncoding sequences: ", len(lCDS1) + len(lCDS2) + len(lNCS1))


## Write to files

lCDS1_out = open("lCDS1.fasta", "w")
lCDS1_out.write(">LocalSeq_exon01_length" + str(len(lCDS1)) + "\n")
lCDS1_out.write(lCDS1)
lCDS1_out.close()

lCDS2_out = open("rCDS2.fasta", "w")
lCDS2_out.write(">LocalSeq_exon02_length" + str(len(lCDS2)) + "\n")
lCDS2_out.write(lCDS1)
lCDS2_out.close()

lNCS1_out = open("lNCS1.fasta", "w")
lNCS1_out.write(">LocalSeq_noncoding01_length" + str(len(lNCS1)) + "\n")
lNCS1_out.write(lNCS1)
lNCS1_out.close()



### REMOTE SEQUENCE ###

## Split sequence into coding and non-coding parts

with open ("AJ223353_noheader.fasta") as myfile:
    remote_seq = myfile.read().upper().replace("\n","")

rCDS1 = remote_seq[28:409]
rNCS1 = remote_seq[:28]
rNCS2 = remote_seq[409:]

print("Length of remote sequence: ", len(remote_seq))
print("Sum of coding and noncoding sequences: ", len(rCDS1) + len(rNCS1) + len(rNCS2))


## Write to files

rCDS1_out = open("rCDS1.fasta", "w")
rCDS1_out.write(">AJ223353_exon01_length" + str(len(rCDS1)) + "\n")
rCDS1_out.write(rCDS1 + "\n")
rCDS1_out.close()

rNCS1_out = open("rNCS1.fasta", "w")
rNCS1_out.write(">AJ223353_noncoding01_length" + str(len(rNCS1)) + "\n")
rNCS1_out.write(rNCS1)
rNCS1_out.close()

rNCS2_out = open("rNCS2.fasta", "w")
rNCS2_out.write(">AJ223353_noncoding01_length" + str(len(rNCS2)) + "\n")
rNCS2_out.write(rNCS2)
rNCS2_out.close()
