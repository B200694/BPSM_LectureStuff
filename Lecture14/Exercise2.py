#!/bin/python3

# Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n (you chose what the number n is!).

with open("rCDS1.fasta") as inputfile:
    seq = inputfile.read().split()[1]

k = 5
n = 3

k_mers = []

for i in range(0, len(seq)) :
    if (i+k) < len(seq)+1 : # Ensures that sequences will not be shorter than k, comment out if not needed.
        k_mer = seq[i:i+k].upper()
        k_mers.append(k_mer)

print(f"Using k = {k}, the following k-mers appear more than {n} times")

for i in set(k_mers) :
    count = k_mers.count(i)
    if count > n :
        print(f"{i} appears {count} times")

