# coding: utf-8

import sys
import re
from collections import defaultdict
import random
import math

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
	#Getting rid of twitterhandles
	line = re.sub(u'@\w+','@@@',line)
	#Getting rid of urls
	line = re.sub(u'http\S+','www',line)
	#Getting rid of hashtags
	line = re.sub(u'#\S+','###',line)
	#deleting hyphens and apostrophe (' and \’ are different!!) in word-middles
	line = re.sub(u"-|('|’)",'',line)
	#Getting rid of start of line and end of line whitespace
	line = re.sub(u'(^\s+|\s+$)','',line)
	#Getting rid of numbers, too. Because they don't seem significant at the moment
	line = re.sub(u'\d+','',line)
	#Getting rid of puncuation
	line = re.sub(u'\W+',' ',line)
	# MAYBE THIS IS BETTER?line = re.sub(u'(\s|^)\W+|\W+(\s|$)',' ',line)
	#And all single letter words...
	line = re.sub(ur'\b\w\b',' ',line)
	#lowercasing all
	line = line.lower()

	return line

## PART 2 ##
def normalize(hist):
	### 3 LINES OF CODE?

	x = sum(hist.values())

	for r in hist: hist[r] = float(hist[r])/x
	

	# this is a void function that normalizes the counts in hist
	# given a dictionary of word-frequency pairs, this function modifies the frequencies so that they sum to 1
	# remove the following print statment once you complete this function
	#print "Normalize doesn't do anything yet"


def get_freqs(f):
	wordfreqs = defaultdict(lambda: 0)
	lenfreqs = defaultdict(lambda: 0)
	for line in f.readlines():
		line = clean(line)
		#Is this okay to add here to get rid of the '' strings?  Or is there a better way??
		#if line:
		words = re.split(u'\s+|\s+[-]+\s+', line)
		lenfreqs[len(words)]+=1
		for word in words:
			wordfreqs[word.encode('utf8')]+=1

	normalize(wordfreqs)
	normalize(lenfreqs)
	#print wordfreqs
	#print "Above is wordfreqs"
	#print lenfreqs
	#print "Above is lenfreqs"
	return (wordfreqs,lenfreqs)


## PART 3 ##
'''
def save_histogram(hist,filename):
	outfilename = re.sub("\.txt$","_out.txt",filename)
	outfile = open(outfilename,'w')
	print "Printing Histogram for", filename, "to", outfilename
	rank = 0
	for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True):
		rank+=1
		output = "%d:\t%-13.6f\t%s\t\t%f\t%f\n" % (rank,count,word,math.log(count),math.log(rank))
		outfile.write(output)
'''

## PART 4 ##
def get_top(hist,N):
	toplist = []
	for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True)[:N]:
		toplist.append(word)
	# return a list of the N most frequent words in hist


	return toplist

def filter(hist,stop):
	for word in stop:
		if word in hist: hist.pop(word)
	hist = normalize(hist)

def main():
	file1 = open(sys.argv[1])
	(wordf1, lenf1) = get_freqs(file1)
	stopwords = get_top(wordf1, 0)
	#save_histogram(wordf1,sys.argv[1])

	
	for fn in sys.argv[2:]:
		file = open(fn)
		(wordfreqs, lenfreqs) = get_freqs(file)
		filter(wordfreqs, stopwords)
		#save_histogram(wordfreqs,fn)

		'''
		## EXTRA CREDIT ##
		print "Printing random tweets from",fn
		for x in range(5):
			n = rand(lenfreqs)
			print n, "random words:"
			for i in range(n):
				print ' ',rand(wordfreqs)
			#,' ',rand(stopwords)
			print
		'''
		print wordfreqs

		
		

## This is special syntax that tells python what to do (call main(), in this case) if this  script is called directly
## this gives us the flexibility so that we could also import this python code in another script and use the functions
## we defined here
if __name__ == "__main__":
    main()


#command for all files: python rando.py tweets_corpus_all.txt tweets_corpus1.txt tweets_corpus2.txt tweets_corpus3.txt tweets_corpus4.txt tweets_corpus5.txt tweets_corpus_mystery.txt 




