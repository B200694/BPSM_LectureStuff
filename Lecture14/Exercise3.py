
### Write a programme/script that calculates and prints, for each pair of sequences, the percentage of identical positions. ###

seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

for i in range(0,len(seqs)) :
    seq1 = seqs[i]
    for j in range(i+1, len(seqs)) :
        seq2 = seqs[j]
        identical_positions = 0
        for pos in range(0, len(seq1)) :
            if seq1[pos] == seq2[pos] :
                identical_positions += 1
        percentage = (identical_positions / len(seq1))*100
        print(f"Percentage of identical positions between {seq1} and {seq2}:", int(percentage))

