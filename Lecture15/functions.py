#!/bin/python3

def perc_of_peptide(peptideseq, query) :
    count = peptideseq.upper().count(query.upper())
    output = (count / len(peptideseq))*100
    return(output)

# Same code as above, but takes list

def perc_of_peptide(peptideseq, query_list=["A", "I", "L", "M", "F", "W", "Y", "V"]) :
    total_count = 0
    for i in query_list :
        item_count = peptideseq.upper().count(i.upper())
        total_count += item_count
    output = (total_count / len(peptideseq))*100
    return(output)

# Write a Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether the DNA sequence contains a high proportion of undetermined bases (i.e not A, T, G or C).

def undefined_bases(dnaseq, threshold=20) :
    defined_count = 0
    for i in ["A", "T", "C", "G"] :
        item_count = dnaseq.upper().count(i)
        defined_count += item_count
    undefined = 1 - (defined_count / len(dnaseq))
    if undefined > threshold :
        print("More than " + round(threshold) + "% of bases are undefined")
        return(TRUE)
    elif undefined < threshold :
        print("Less than " + round(threshold) + "% of bases are undefined")
        return(FALSE)
    else :
        print(round(threshold) + "% of bases are undefined")
        return(FALSE)

## Version 2 - simpler

def undefined_bases(dnaseq, threshold=0.2) :
    defined_count = 0
    for i in ["A", "T", "C", "G"] :
        item_count = dnaseq.upper().count(i)
        defined_count += item_count
    undefined = 1 - (defined_count / len(dnaseq))
    return undefined >= threshold

# Assertions

    assert undefined_bases("ATCGTCXYZ")) == TRUE
    assert undefined_bases("ATGCTGACCN", 0.8)) == FALSE
    assert undefined_bases("atucgtgractanctgactg", 0.2)) == TRUE

# Write a FUNCTION that, given any DNA sequence, will printvall the k-mers (of a chosen size e.g. 4-mers) 
# that occur more than some chosen number of times

def find_kmers(seq, k=2, n=2): 
    k_mers=[]
    for i in range(0, len(seq)) :
        if (i+k) < len(seq)+1 : # Ensures that sequences will not be shorter than k, comment out if not needed.
            k_mer = seq[i:i+k].upper()
            k_mers.append(k_mer)
    print(f"Using k = {k}, the following k-mers appear more than {n} times")
    output=[]
    for i in set(k_mers) :
        count = k_mers.count(i)
        if count > n :
            print(f"{i} appears {count} times")
            output.append(i+": "+str(count))
    return(output)


