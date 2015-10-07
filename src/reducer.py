#!/usr/bin/python

import sys

wordCount = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	thisKey, node_id = data_mapped
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
	        continue

	if oldKey and oldKey != thisKey:
		print oldKey,"\t",wordCount,"\t",node_id
		oldKey = thisKey
		wordCount = 0

	oldKey = thisKey
	wordCount += 1

if oldKey != None:
	print oldKey,"\t", wordCount,"\t",node_id 

