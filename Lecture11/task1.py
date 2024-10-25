#!/bin/python3
# Program to calculate AT content of DNA sequence
# s2150996
# 22/10/2024

#------------------#

#Input
sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# Process
count_A = sequence.count("A")
count_T = sequence.count("T")
AT_content = (count_A + count_T) / len(sequence)

# Output
print("The sequence is of length", len(sequence), "and has", count_A, "As and",
	count_T, "Ts, giving it an AT content of", str(round(100*AT_content)) + "%.")
