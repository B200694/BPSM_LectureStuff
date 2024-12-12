#!/bin/python3

import os, re
import matplotlib.pyplot as plt

values = []
kmers = []
with open("all_stats.txt") as inputfile :
    for i in inputfile :
        fields = i.split("/")
        KB = fields[3].replace("KB", "").replace(" ", "").replace("\n", "")
        print(KB)
        print(fields[1])
        kmer = re.search("k\d+", fields[1]).group().replace("k", "")
        values.append(KB)
        kmers.append(kmer)

values[0] = 0
print(values)
print(kmers)

plt.figure()
plt.scatter(kmers, values)
plt.ylabel("Contig size (KB)")
plt.xlabel("kmer size")
plt.savefig("all_stats.png",transparent=False)


