#!/usr/bin/env python
# coding: utf-8

# import the necessary packages
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
import argparse
import sys
import chardet

#### Importing the data ####

# Parsing arguments with argparse
parser = argparse.ArgumentParser(description = 'This script allows data selection for various requested analytes from Total Diet Studies at the FDA.')
parser.add_argument('--file', required=True, help='The Total Diet Study file to be analyzed.')
parser.add_argument('--analyte', required=True, help='The analyte that is to be extracted, e.g. Arsenic. CASE SENSITIVE.')
parser.add_argument('--type', required=True, help='The type of analyte that the Total Diet Study input file is measuring, e.g. Element. CASE SENSITIVE.')
parser.add_argument('--number', required=False, help='optional: The Food Number associated with a specific food.')
parser.add_argument('--cutoff', required=False, type=float, help='optional: Specifiy a new cut-off concentration, default=None.')
parser.add_argument('--filename', required=False, default='outfile', help='optional: name of the file, default=outfile.txt, output as TSV')
args = parser.parse_args()

#### Cleaning up the data ####

# determining the file encoding for reading by pandas
rawdata = open(args.file, 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']

##### Processing the Data #####

# reading in the file
file = pd.read_csv(args.file, sep='\t', encoding=charenc)

# obtaining the rows that contain the desired analyte
df1 = file[file[args.type].str.contains(args.analyte)]

#incorporating food number; currently sorting this out
#df2 = df1[df1['Food No.'].str.contains(args.number))]

# removes rows containing RAP
df_remove = df1[df1['Sample Qualifier'].str.contains('UAP', '', na=True, regex=False)]

#### LOQ compliance ####

# generating a dataframe that compares the concentration detected to a cut off
if args.cutoff == None:
	LOQ_compliant = df_remove[df_remove['Conc'] > df_remove['LOQ']] # if no cutoff is provided
else:
	LOQ_compliant = df_remove[df_remove['Conc'] > args.cutoff] # if a cutoff is provided

No_detect = df_remove[df_remove['Conc'] == 0]

# tests 

#### Generating the output file ####

# Code for printing LOQ compliant to a file 
if args.filename == None:
	output_LOQ = open('outfile.txt', 'w')
else:
	output_LOQ = open(args.filename + '_outfile.txt', 'w')

LOQ_compliant.to_csv(output_LOQ, sep='\t')

output_LOQ.close()

# Code for printing the No Detect to a file
if args.filename == None:
	output_nodetect = open('No_detect.txt', 'w')
else:
	output_nodetect = open(args.filename + '_nodetect.txt', 'w')

No_detect.to_csv(output_nodetect, sep='\t')

output_nodetect.close()