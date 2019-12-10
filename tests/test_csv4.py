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
parser.add_argument('--number', required=False, help='optional: The Food Number associated with a specific food.')
parser.add_argument('--cutoff', required=False, help='optional: Specifiy a new cut-off concentration, default=0.')
args = parser.parse_args()

# determining the file encoding for reading by pandas
rawdata = open(args.file, 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']

# reading in the file
file = pd.read_csv(args.file, sep='\t', encoding=charenc)

# obtaining the rows that contain the desired analyte
df1 = file[file[args.type].str.contains(args.analyte)]

# removes rows containing RAP
df_remove = df1[df1['Sample Qualifier'].str.contains('UAP', '', na=True)]



# Code for printing to a file 
output = open('Results.txt', 'w') 

df_remove.to_csv(output, sep='\t')

output.close()