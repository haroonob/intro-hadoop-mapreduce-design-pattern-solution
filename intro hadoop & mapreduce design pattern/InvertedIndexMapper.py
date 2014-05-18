#!/usr/bin/python

import sys
import csv
import re
#print word and quesiton id
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	content = re.split(r'[\s?:!"()<>/,#-.;]',line[4])
	for word in content:
		if(len(word) > 1):
         	 print "{0}\t{1}".format(word.strip().lower(),line[0])
