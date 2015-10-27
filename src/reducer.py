#!/usr/bin/python

import sys
import csv
wordCount = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	thisKey = data_mapped
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
	        continue

	if oldKey and oldKey != thisKey:
		word,country = oldKey
		csvfile = open("../wordcount1.csv","a")
		writer = csv.writer(csvfile,dialect = "excel")
		writer.writerow([word,country,wordCount])
		oldKey = thisKey
		wordCount = 0

	oldKey = thisKey
	wordCount += 1

if oldKey != None:
		word,country = oldKey
		csvfile = open("../wordcount1.csv","a")
		writer = csv.writer(csvfile,dialect = "excel")
		writer.writerow([word,country,wordCount])
		
