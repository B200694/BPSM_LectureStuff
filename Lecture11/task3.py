#!/bin/python3

# Program to take a DNA sequence, find EcoRI restriction site and work out fragment sizes
# s2150996
# 22/10/2024

# ----------- #

#Input
sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

# Process
pos = sequence.find("GAATTC")

# Output
print("Sequence length:", len(sequence))
print("The recognition site for EcoRI is at Python position", pos, "in this sequence")

# Process
cut1 = sequence[:int(pos)+1]
cut2 = sequence[int(pos)+1:]

# Output
print("EcoRI cuts the sequence into two fragments of length", len(cut1), "and", len(cut2))
