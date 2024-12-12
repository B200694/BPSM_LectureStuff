#!/bin/python3

# How many complete COX1 protein records are there for mammals?

from Bio import SeqIO, Entrez
Entrez.email = "s2150996@ed.ac.uk"
records = Entrez.read(Entrez.esearch(db="protein", term="COX1[gene] AND Mammalia[Organism]", retmax = 20))
no_seqs = int(records['Count'])

totallength = 0
for i in records['IdList'] :
    genbank = Entrez.efetch(db = "protein", id = i, rettype = "gb")
    record = SeqIO.read(genbank, "genbank")
    totallength += int(len(record.seq))

avg_length = totallength / 20

print(f"The search returned " + str(no_seqs) + " sequences with an average length of " + str(avg_length))

def mysearch(genename = "COX1", taxa = "Mammalia", retmax = 20) :
    from Bio import SeqIO, Entrez
    Entrez.email = "s2150996@ed.ac.uk"
    searchterm = f"{genename}[gene] AND {taxa}[Organism]"
    records = Entrez.read(Entrez.esearch(db = "protein", term = searchterm, retmax = retmax))
    no_seqs = int(records['Count'])
    aa_total = 0
    for i in records['IdList'] :
        genbank = Entrez.efetch(db = "protein", id = i, rettype = "gb")
        record = SeqIO.read(genbank, "genbank")
        aa_total += int(len(record.seq))
    avg_length = aa_total / retmax
    print(f"The search returned " + str(no_seqs) + " sequences")
    print(f"The first " + str(retmax) + " have an average length of " + str(avg_length))
    return(avg_length)

## Much more to do here: ##

# -- For each record, print accessions, descriptions, lengths, first e.g 20 amino acids
# -- Write these outputs to a file
# -- Allow user to choose which sequences they want
# -- Spot ambiguity codes of sequences
# -- Look at links explaining how to do things in parallel
