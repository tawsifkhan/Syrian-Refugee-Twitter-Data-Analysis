#!/usr/bin/python

import sys
import csv
import re


reader = csv.reader(sys.stdin, delimiter = ',')

for line in reader:
	tweet,country = line
# A word is strictly an array of alphabets (no digits and etc)
	tweetWords = re.findall(r"['\w]+",tweet)
	for word in tweetWords:
		if len(re.findall(r"[a-z]",word.lower())) == len(word) and len(word)>3:
			print "{0}\t{1}".format(word.lower(),country)
	
