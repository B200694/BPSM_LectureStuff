#!/bin/python3

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translate_dna(dna, frame=1) :
    dna = dna.upper()
    if frame not in [-3,-2,-1,1,2,3]:
       print("Not a valid translation frame,\nHas to be one of these: -3, -2, -1, 1, 2, 3.\nExiting....")
       return
    if frame in [-3,-2,-1]:
       print("Need to make the reverse complement to do the reverse strand translations....")
       c_dna = dna.replace("G","c").replace("A","t").replace("T","a").replace("C","g").upper()
       rc_dna = c_dna[::-1]
       dna = rc_dna
    print(f'Translating sequence using frame: {dna}')
    translation = []
    for start in range(abs(frame)-1, len(dna), 3) :
        codon = dna[start:start+3]
        if len(codon) == 3 :
            aa = gencode.get(codon, "X")
        else :
            aa = ""
        translation.append(aa)
    print(f'Frame ' + str(frame) + ':')
    print(''.join(translation))
    return(''.join(translation))

assert translate_dna("ATGTTCGGT") == "MFG"
assert translate_dna("ATCGATCGATCGTTGCTTATCGATCAG") == "IDRSLLIDQ"
assert translate_dna("actgatcgtagctagctgacgtatcgtat") == "TDRS_LTYR"
assert translate_dna("ACGATCGATCGTNACGTACGATCGTACTCG") == "TIDRXVRSYS"
