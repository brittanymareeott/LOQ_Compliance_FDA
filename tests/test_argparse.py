#!/usr/bin/env python
# coding: utf-8

# import the necessary packages
import csv
from pandas import DataFrame
import argparse
import sys

# Parsing arguments with argparse
parser = argparse.ArgumentParser(description = 'This script allows data selection for various requested analytes from Total Diet Studies at the FDA.')
parser.add_argument('--file', required=True, help='The Total Diet Study file to be analyzed.')
parser.add_argument('--analyte', required=True, help='The analyte that is to be extracted, e.g. Arsenic.')
parser.add_argument('--type', required=True, help='The type of analyte that the Total Diet Study input file is measuring, e.g. Element.')
parser.add_argument('--out', required=True, help='The directory where you want output files written.')
parser.add_argument('--number', required=False, help='optional: The Food Number associated with a specific food.')
parser.add_argument('--cutoff', required=False, help='optional: Specifiy a new cut-off concentration, default=0.')
args = parser.parse_args()

print(args)
