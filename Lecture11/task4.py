#!/bin/python3

# Program to analyse intron and exon regions of sequence
# s2150996
# 22/10/2024

# ------------- #

# Input
sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = sequence[:63]
exon2 = sequence[90:]

# Process
coding_sequence = exon1 + exon2

print("The sequence exons combine to read:", coding_sequence)

perc_coding = (len(coding_sequence) / len(sequence)) * 100

print("Coding regions take up " + str(round(perc_coding)) + "% " + "of the sequence")

intron = sequence[64:90]

# Output
print("With coding regions in uppercase and non-coding regions in lowercase, the sequence reads: " + exon1 + intron.lower() + exon2)
