# coding: utf-8

import sys
import re
from collections import defaultdict
import random
import math

## EXTRA CREDIT ##
def rand(hist):
	rnum = random.uniform(.001857,.026454)
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
	#sum of frequencies
	x = sum(hist.values())
	#divide each value by sum, in order to get values that will add to 1
	for r in hist: hist[r] = float(hist[r])/x
	

	# this is a void function that normalizes the counts in hist
	# given a dictionary of word-frequency pairs, this function modifies the frequencies so that they sum to 1
	# remove the following print statment once you complete this function
	#print "Normalize doesn't do anything yet"


def get_freqs(f):
	wordfreqs = defaultdict(lambda: 0)
	lenfreqs = defaultdict(lambda: 0)
	#for each line in all the lines of the file (which is sys.argv[x])
	for line in f.readlines():
		#clean it of all the unwanted characters
		line = clean(line)
		#Is this okay to add here to get rid of the '' strings?  Or is there a better way??
		#if line:
		#split each line into what we have determined to be words
		words = re.split(u'\s+|\s+[-]+\s+', line)
		#lenfreqs is the dictionary of how often each line(tweet) length occurs
		lenfreqs[len(words)]+=1
		#for each word in the words split from each line
		for word in words:
			#count the frequency in the wordfreqs dictionary
			wordfreqs[word.encode('utf8')]+=1
	#change the frequencies from counted to percentage
	normalize(wordfreqs)
	normalize(lenfreqs)
	#return wordfreqs to the main function, where it will have the stopwords taken from it and then
	#be saved to the outfile
	return (wordfreqs,lenfreqs)


## PART 3 ##
'''
def save_histogram(hist,filename):
	#The output file name will be the argument filename plus _out before the .txt
	outfilename = re.sub("\.txt$","_out.txt",filename)
	outfile = open(outfilename,'w')
	print "Printing Histogram for", filename, "to", outfilename
	#I put this in in order to print out the ranks of the words printed to the file
	rank = 0
	#for each word it will print the rank, the count (normalized), the word, the log of the count
	#and the log of the rank
	for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True):
		rank+=1
		output = "%d:\t%-13.6f\t%s\t\t%f\t%f\n" % (rank,count,word,math.log(count),math.log(rank))
		outfile.write(output)
'''
## PART 4 ##
def get_top(hist,N):
	#an empty list to be appended to
	toplist = []
	#From the words of file 1 (i.e. the all corpus), starting at item 0 until item #N (N items),
	#save these to a list to be returned to the main function
	for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True)[:N]:
		toplist.append(word)
	# return a list of the N most frequent words in hist
	return toplist

def filter(hist,stop):
	#for each word in the stop words list, pop that word from the given dictionary
	for word in stop:
		if word in hist: hist.pop(word)
	#re-normalize the dictionary, since we have made it's relative frequencies not add to 1
	normalize(hist)

def main():
	#first we are going to open the all corpus, which should be argument 1
	file1 = open(sys.argv[1])
	#get the frequencies of the words and the frequencies of the lines
	(wordf1, lenf1) = get_freqs(file1)
	#get the top 200 words from the all corpus
	stopwords = get_top(wordf1, 200)
	#save to the output file for the all corpus
	#save_histogram(wordf1,sys.argv[1])
	#for each argument past 1
	for fn in sys.argv[2:]:
		file = open(fn)
		(wordfreqs, lenfreqs) = get_freqs(file)
		#run the words found in this corpus through the stop words list and take out any that are present
		filter(wordfreqs, stopwords)
		#save it to the output file
		#save_histogram(wordfreqs,fn)
		rank = 0
		for word in sorted(wordfreqs.items(), key = lambda pair: pair[1], reverse = True)[:10]:
			rank+=1
			print "%d:\t%s" % (rank,word)

'''
		tweetlength = input('How many topic words would you like these tweets to be?')
		#Prints the string and then the name of the corpus it is making tweets for
		print "Printing random tweets from",fn
		#it’s going to iterate the following 5 times (i.e. it’s gonna make 5 tweets)
		
		for x in range(5):
			#n is a random amount of words from the count of how many words were in each line
			#after cleaning (i.e. the keys of lenfreqs are all the possible tweet line lengths)
			
			
			#this for loop will be iterated whatever random amount of times was found above 
			#meaning that this tweet will be n words long, and it will get those words from…
			#for i in range(n):
				#…wordfreqs--it is going to print n words from wordfreqs, which will be all
				#the words that were in the tweets after cleaning and after popping the stop words.
			for i in range(tweetlength):
				print stopwords[random.randint(25,100)],rand(wordfreqs),
			print
'''	
		
		

## This is special syntax that tells python what to do (call main(), in this case) if this  script is called directly
## this gives us the flexibility so that we could also import this python code in another script and use the functions
## we defined here
if __name__ == "__main__":
    main()


#command for all files: python tweetgenerator.py tweets_corpus_all.txt tweets_corpus1.txt tweets_corpus2.txt tweets_corpus3.txt tweets_corpus4.txt tweets_corpus5.txt tweets_corpus_classchoice.txt tweets_corpus_mystery.txt 


		




