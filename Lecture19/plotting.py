#!/bin/python3 

# Use the ecoli.txt file and, using the code above as a starting point, make a chart which shows the AT content in a sliding 1000 base window

import matplotlib.pyplot as plt
ecoli = open("ecoli.txt").read().replace('\n', '')


# For the first 50000 bases

data1 = ecoli[0:50001]
winsize = 1000
at = []

print(f"Finding sequences using window size " + str(winsize) + "...")

for start in range(0, len(data1) - winsize) :
    seq = ecoli[start:start+winsize]
    at.append((seq.count('A') + seq.count('T')) / winsize)

print(f"Plotting figure...")
print(f"Creating first subplot...")

plt.figure(figsize=(20,10))
plt.subplot(311)
plt.plot(at, linewidth = 2, color = "red")
plt.title('First 50000 bases')
plt.ylabel('AT content')
plt.xlabel('Genome position')

print(f"First subplot created.")


# For the first 100000 bases

data2 = ecoli[0:100001]
at = []

for start in range(0, len(data2) - winsize) :
    seq = ecoli[start:start+winsize]
    at.append((seq.count('A') + seq.count('T')) / winsize)

print(f"Creating second subplot...")

plt.subplot(312)
plt.plot(at, linewidth = 2, color = "red")
plt.title('First 100000 bases')
plt.ylabel('AT content')
plt.xlabel('Genome position')

print(f"Second subplot created.")


# For the whole genome

at = []

for start in range(0, len(ecoli) - winsize) :
    seq = ecoli[start:start+winsize]
    at.append((seq.count('A') + seq.count('T')) / winsize)

print(f"Creating third subplot...")

plt.subplot(313)
plt.plot(at, linewidth = 2, color = "red")
plt.title('Whole Genome')
plt.ylabel('AT content')
plt.xlabel('Genome position')

print(f"Third subplot created.")

plt.suptitle('AT content in the E.coli genome\nWindow size of ' + str(winsize), fontsize = 12)
plt.savefig("Chart_19A.png", transparent = False)

print(f"Figure created -> Chart_19A.png")

## From Al's answers: ##

# Consider using a for loop to iterate over the 3 regions
