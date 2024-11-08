#!/bin/python3

### IMPORTING DATA ###

with open("data.csv") as f :
    data = f.readlines()

# Define our variables as arrays
species_name = []
seq = []
gene_name = []
expr_lvl = []

count=0 # Variable for counting number of genes
for i in data : # For each line, assign values to our variables
    count+=1
    gene = i.split(",")
    species_name.append(gene[0])
    seq.append(gene[1].upper()) # Make sequences uppercase
    gene_name.append(gene[2])
    expr_lvl.append(gene[3].replace("\n", "")) # Replace EOL in last CSV column

print("\n")
print("There are " + str(count) + " genes in the dataset")
print("\n")

### Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans. ###

for i in range(0,count) :
    if species_name[i] == "Drosophila melanogaster" :
        print(f"Gene {gene_name[i]} was sampled from Drosophila melanogaster")
    elif species_name[i] == "Drosophila simulans" :
        print(f"Gene {gene_name[i]} was sampled from Drosophila simulans")
    else :
        print(f"Gene {gene_name[i]} was not sampled from D. melanogaster or D. simulans")


### Print out the gene names for all genes that are between 90 and 110 bases long. ###

print("\n")
print("The following genes are between 90 and 110 bases long:")

for i in range(0,count) :
    if len(seq[i]) >= 90 and len(seq[i]) <= 110 :
        print(gene_name[i])

### Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200 ###

print("\n")
print("The following genes have an AT content of less than 0.5 and an expression level of over 200:")

for i in range(0,count) :
    A = seq[i].upper().count("A")
    T = seq[i].upper().count("T")
    AT_content = (A + T)/len(seq[i])
    if AT_content < 0.5 and int(expr_lvl[i]) > 200 :
        print(gene_name[i])

### Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster. ###

print("\n")
print("The following genes begin with 'k' or 'h', excluding those sampled from D. melanogaster:")

for i in range(0,count) :
   if species_name[i] != "Drosophila melanogaster" and (
       gene_name[i].startswith("k") or gene_name[i].startswith("h")):
    print(gene_name[i])

### For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65). ###

print("\n")

for i in range(0,count) :
    A = seq[i].upper().count("A")
    T = seq[i].upper().count("T")
    AT_content = (A + T)/len(seq[i])
    if AT_content > 0.65 :
        level = "high"
    elif AT_content < 0.45 :
        level = "low"
    else :
        level = "medium"
    print(f"Gene {gene_name[i]} has an AT content of", str(round(AT_content, 2)), f"which is {level}")

# Could be made more compact by answering all the questions within one for loop
