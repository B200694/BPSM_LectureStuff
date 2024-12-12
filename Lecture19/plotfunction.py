#!/bin/python3

# Using the working code from the Exercise 1, write a script that calls a function that you have written to do the processing. The default sequence should be the ecoli one we used for the lecture. The user should be able to provide the window size, whether they want AT content or GC content plotted, and what portion (base range) of the genome they want analysed 

import matplotlib.pyplot as plt

def myplot(inputfile = "ecoli.txt", winsize = 1000, seqstart = 0, seqend = 50000, bases = "AT") :
    if winsize > seqend - seqstart :
        return(f"ERROR: Window size is larger than sequence size")
    print(f"Importing {inputfile} ...")
    with open(inputfile, 'r') as f:
        genome = f.read().replace('\n', '').upper()
    content = []
    print(f"Finding sequences using window size " + str(winsize) + " between positions " + str(seqstart) + \
            " and " + str(seqend) + " in the genome...")
    for i in range(seqstart, seqend - winsize) :
        window = genome[i:i+winsize]
        if bases == "AT" :
            content.append((window.count('A') + window.count('T')) / winsize)
        elif bases == "GC" :
            content.append((window.count('G') + window.count('C')) / winsize)
        else :
            return(f"ERROR: bases argument requires AT or GC")
    print(f"Sequences found. Initialising plot...")
    plt.figure(figsize = (20,10))
    plt.plot(content, linewidth = 2, color = "purple")
    plt.xlabel('Genome position')
    plt.ylabel(f'{bases} content')
    plt.title(f'{bases} content in {inputfile}')
    plt.savefig("myplot.png", transparent = False)
    print(f"Figure created -> myplot.png")
