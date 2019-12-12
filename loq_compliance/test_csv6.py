#!/usr/bin/env python
# coding: utf-8

############################# Documentation #############################
#  test_csv6.py                                                         #
#                                                                       #
# Author: Brittany M. Ott                                               #
#                                                                       #
# This script allows the user to parse down a .tsv file produced        #
# by the Total Diet Study at the FDA. It produces two files:            #
# 1) An output `.txt` file that contains all samples where the          #
# concentration of the analyte of interest is greater than the          #
# sample's LOQ (limit of quantitation); and 2) An output `.txt`         #
# file containing all samples where the analyte requested is not        #
# detected.                                                             #
#                                                                       #
# For documentation used to generate this script, please visit:         #
# * Python's argparse page:                                             #
# https://docs.python.org/dev/library/argparse.html#argparse.Namespace  #
# * Pandas's API reference page:                                        #
# https://pandas.pydata.org/pandas-docs/stable/reference/index.html     #
# * PyPi's chardet page:                                                #
# https://pypi.org/project/chardet/                                     #
#                                                                       #
# The script takes 3 required arguments:                                #
# 1) --file | The Total Diet Study file that is to be analyzed (`.txt`) #
# 2) --analyte | The analyte to be extracted (e.g. Arsenic), this is    #
# case sensitive                                                        #
# 3) --type | The type of analyte that the Total Diet study is          #
# examining (e.g. Element), this is case sensitive                      #
#                                                                       #
# This script currently also takes two arguments that are optional:     #
# 1) --cutoff | This allows the user to specify a new cutoff            #
# concentration; default=None                                           #
# 2) --filename | This allows the user to specify a file name for the   #
# output files; default=outfile.txt and nodetect.txt, output as TSV     #
#                                                                       #
# usage: python test_csv6.py [-h] --file FILE --analyte ANALYTE         # 
# --type TYPE [--number NUMBER] [--cutoff CUTOFF] [--filename FILENAME] #
#########################################################################


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
# parser.add_argument('--number', required=False, help='optional: The Food Number associated with a specific food.')
parser.add_argument('--cutoff', required=False, type=float, help='optional: Specifiy a new cut-off concentration, default=None.')
parser.add_argument('--filename', required=False, default='outfile', help='optional: name of the file, default=outfile.txt and nodetect.txt, output as TSV')
args = parser.parse_args()

#### Cleaning up the data ####

# determining the file encoding for reading by pandas
rawdata = open(args.file, 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']

### Processing the Data ###

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
# *note*: currently working on a way to compare the new cutoff with the LOQ column
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