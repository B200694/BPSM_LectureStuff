#!/bin/python3

# Open exons file and create a list of exon positions
with open("exons.txt") as f :
    # replacing newline with comma allows all positions to be extracted in one go
    exons = f.read().replace("\n", ",").split(",")
    exons = exons[:-1] # remove the last item as it is blank

# Convert to a list of integers
pos = []
pos.extend(int(i) for i in exons)

# Print the exons positions
print(f"Exon start positions are {exons[0::2]}")
print(f"Exon end positions are {exons[1::2]}")

# Open genome sequence
with open("genomic_dna2.txt") as f :
    seq = f.read()

# Extract exons from sequence
seq_CDS = []
count=0

for i in range(0, len(pos), 2) :
    count+=1
    print(f"Extracting exon {count}...")
    start = pos[i]
    end = pos[i+1]
    seq_CDS.append(seq[start+1:end+2])
    print("Exon", count, ":", seq[start+1:end+2])

# Concatenate exons
print("Concatenating exons...")
output = ''.join(seq_CDS)
print("Final output:", output)

# Write to file
with open("concatenated_exons.txt", "w") as f :
    f.write(output)
print("Output written to file -> concatenated_exons.txt")
