#!/bin/python3

import re

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
print(f"Accessions to be analysed:", accessions)


print(f"\nAccessions that contain the number 5: \n")
for i in accessions :
    if re.search(r'5', i) :
        print(i)

print(f"\nAccessions that contain the letter d or e: \n")
for i in accessions :
    if re.search(r'[de]', i) :
        print(i)

print(f"\nAccessions that contain d followed by e: \n")
for i in accessions :
    if re.search(r'de', i) :
        print(i)

print(f"\nAccessions that contain d, followed by any letter, followed by e: \n")
for i in accessions :
    if re.search(r'd.e', i) :
        print(i)

print(f"\nAccessions that contain de or ed: \n")
for i in accessions :
    if re.search(r'(de|ed)', i) :
        print(i)

print(f"\nAccessions that start with x or y: \n")
for i in accessions :
    if re.search(r'^[xy]', i) :
        print(i)

print(f"\nAccessions that start with x or y and end with e: \n")
for i in accessions :
    if re.search(r'^[xy].*e$', i) :
        print(i)

print(f"\nAccessions that contain any 3 numbers: \n")
for i in accessions :
    if len(re.findall(r'\d', i)) == 3 :
        print(i)

print(f"\nAccessions that contain 3 different numbers: \n")
for i in accessions :
    if len(set(re.findall(r'\d', i))) == 3 :
        print(i)

print(f"\nAccessions that contain 3 or more numbers in a row: \n")
for i in accessions :
    if re.search(r'\d{3,}', i):
        print(i)

print(f"\nAccessions that end with d followed by either a, r or p: \n")
for i in accessions :
    if re.search(r'd[arp]{1}$', i):
        print(i)

