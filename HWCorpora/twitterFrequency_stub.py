# coding: utf-8

import sys
import re
from collections import defaultdict
import random

## EXTRA CREDIT ##
def rand(hist):
	rnum = random.uniform(0,1)
	for x in hist:
		rnum -= hist[x]
		if rnum < 0: return x
	return x

## PART 1 ##
def clean(line):
	line = line.decode('utf8')
	#use the following syntax for all your replacements so that unicode is properly treated
	#line = re.sub(u'replace_regexp','with_regexp',line)
	return line

## PART 2 ##
def normalize(hist):
	# this is a void function that normalizes the counts in hist
	# given a dictionary of word-frequency pairs, this function modifies the frequencies so that they sum to 1
	# remove the following print statment once you complete this function
	print "Normalize doesn't do anything yet"

def get_freqs(f):
	wordfreqs = defaultdict(lambda: 0)
	lenfreqs = defaultdict(lambda: 0)

	for line in f.readlines():
		#print line
		line = clean(line)
		words = re.split(u'\s+|\s+[-]+\s+', line)
		lenfreqs[len(words)]+=1
		for word in words:
			wordfreqs[word.encode('utf8')]+=1
	
	normalize(wordfreqs)
	normalize(lenfreqs)
	return (wordfreqs,lenfreqs)

## PART 3 ##
def save_histogram(hist,filename):
	outfilename = re.sub("\.txt$","_out.txt",filename)
	outfile = open(outfilename,'w')
	print "Printing Histogram for", filename, "to", outfilename
	for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True):
		output = "%-13.6f\t%s\n" % (count,word)
		outfile.write(output)

## PART 4 ##
def get_top(hist,N):
	# return a list of the N most frequent words in hist
	return []

def filter(hist,stop):
	for word in stop:
		if word in hist: hist.pop(word)
	normalize(hist)

def main():
	file1 = open(sys.argv[1])
	(wordf1, lenf1) = get_freqs(file1)
	stopwords = get_top(wordf1, 0)
	save_histogram(wordf1,sys.argv[1])
	
	for fn in sys.argv[2:]:
		file = open(fn)
		(wordfreqs, lenfreqs) = get_freqs(file)
		#filter(wordfreqs, stopwords)
		save_histogram(wordfreqs,fn)

		'''
		## EXTRA CREDIT ##
		print "Printing random tweets from",fn
		for x in range(5):
			n = rand(lenfreqs)
			print n, "random words:"
			for i in range(n):
				print ' ',rand(wordfreqs),
			print
		'''

## This is special syntax that tells python what to do (call main(), in this case) if this  script is called directly
## this gives us the flexibility so that we could also import this python code in another script and use the functions
## we defined here
if __name__ == "__main__":
    main()