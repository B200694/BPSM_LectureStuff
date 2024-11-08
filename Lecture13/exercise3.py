#!/bin/python3

with open("rCDS1.fasta") as inputfile:
    seq = inputfile.read().split()[1]

windowsize = 30
offset = 3

k_starts = list(range(0, len(seq), offset))

k_mers = []

for i in k_starts :
    k_mer = seq[i:i+windowsize].upper()
    k_mers.append(k_mer)

for i in range(0, len(k_mers)) :
    print(k_mers[i])
    print("\n")
