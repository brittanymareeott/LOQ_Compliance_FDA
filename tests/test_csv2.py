#!/usr/bin/env python
# coding: utf-8

# import the necessary packages
import csv
import pandas as pd
from pandas import DataFrame
import argparse
import sys
import chardet

# Parsing arguments with argparse
parser = argparse.ArgumentParser(description = 'This script allows data selection for various requested analytes from Total Diet Studies at the FDA.')
parser.add_argument('--file', required=True, help='The Total Diet Study file to be analyzed.')
parser.add_argument('--analyte', required=True, help='The analyte that is to be extracted, e.g. Arsenic.')
parser.add_argument('--type', required=True, help='The type of analyte that the Total Diet Study input file is measuring, e.g. Element.')
parser.add_argument('--out', required=True, help='The directory where you want output files written.')
parser.add_argument('--number', required=False, help='optional: The Food Number associated with a specific food.')
parser.add_argument('--cutoff', required=False, help='optional: Specifiy a new cut-off concentration, default=0.')
args = parser.parse_args()

rawdata = open(args.file, 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']

with open(args.file, newline='', encoding=charenc) as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    rows = [r for r in csvreader]
# check consistency of rows
print(len(rows))
print(set((len(r) for r in rows)))
print(tuple(((i, r) for i, r in enumerate(rows) if len(r) == bougus_nbr)))
# find bougus lines and modify in memory, or change csv and re-read it.

# Code for printing to a file 
output = open('Results.txt', 'w') 
  
print(file, file = output) 
output.close()
