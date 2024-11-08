#!/bin/python3

# Find the adapter, create a string containing it

inputfile = open("input.txt").read().split("\n")
inputlist = inputfile[:-1]

adapter = inputlist[0][:14]

# For each item of the inputfile list, replace the adapter with nothing 

count=0
cleaned = []
for i in inputlist :
    count+=1
    clean_seq = i.replace(adapter, "")
    cleaned.append(clean_seq)
    print(f"Adapter removed from sequence {count}")

# Write cleaned sequences to a new file

with open("cleaned_seqs.txt", "w") as cleaned_w :
    for i in cleaned :
        cleaned_w.write(i + "\n")

# Print each adapter-free line

count=0
for i in cleaned :
    count+=1
    print(f"Sequence {count} is {i}")
