#!/bin/python3

# Script that outputs the complement of a DNA sequence
# s2150996
# 22/10/2024

# ------------ #

# Input
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("The sequence is: " + sequence)

# Process
proto_complement = sequence.replace("A", "x").replace("T", "A").replace("x", "T")
complement = proto_complement.replace("C", "x").replace("G", "C").replace("x", "G")

# Output
print("Its complement is: " + complement)
