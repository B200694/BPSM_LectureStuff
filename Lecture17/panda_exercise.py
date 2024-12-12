#!/bin/python3

import os, sys, re, numpy as np
import pandas as pd

df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])


df.index=df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1) # create a new index which is made up of the Organism name and the accession number

df['Genus'] = df.apply(lambda x : x['#Organism/Name'].split(' ')[0], axis=1) # Create new Genus column

# print(df.columns)

### How many fungal species have genomes bigger than 100Mb? What are their names? ###

# print('Fungi' in set(df['Group']))

fungi = df[df.apply(lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1)]

print('\nThere are ' + str(len(fungi)) + ' fungal species with a genome size > 100 Mb:\n')

print('Organism\tCount')
print(fungi['#Organism/Name'].value_counts().to_string())

fungi_names = sorted(set(fungi['#Organism/Name'])) # Create list if that is preferred

### How many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced? ###

kingdoms = df['Group'].value_counts()

print('\nHow many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?\n') 
print(kingdoms.to_string())

### Which Heliconius species genomes have been sequenced? ###

heliconius = df[df['Genus'] == 'Heliconius']['#Organism/Name'].value_counts()

print('\nList of Heliconius species in dataset:\n')
print(heliconius.to_string())

### Which sequencing centre has sequenced the most plant genomes? the most insect genomes? ###

# Plant
plant_centres = df[df['Group'] == 'Plants']['Center'].value_counts()

print('\nCentres that have sequenced the most plant genomes:\n')
print(plant_centres.head(5).to_string())

top_plant_centre = plant_centres.index[0]
print(f'\n\tThe centre that has sequenced the most plant genomes is {top_plant_centre}.\n')

# Insect
insect_centres = df[df['SubGroup'] == 'Insects']['Center'].value_counts()

print('\nCentres that have sequenced the most insect genomes:\n')
print(insect_centres.head(5).to_string())

top_insect_centre = insect_centres.index[0]
print(f'\n\tThe centre that has sequenced the most insect genomes is {top_insect_centre}.\n')

### Add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes? ###

df['PPG'] = df['Proteins'] / df['Genes']
filtered_df = df[df['PPG'] >= 1.1]

print('\nGenomes with a proteins per gene (PPG) over 1.1:\n')
print(filtered_df['PPG'])
