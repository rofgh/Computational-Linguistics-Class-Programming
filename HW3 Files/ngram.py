import sys
import random
import math
import re
from collections import defaultdict
from timeit import default_timer as timer
'''
This script at the command line: python ngram.py train.txt 2/3 x.txt
	train.txt is the training doc:  train.txt is the full text, mini_train.txt is a small version
	2/3 is the choice between bigram or trigram, the argument should either be 2 or 3
	x.txt is the mystery test file (either y.txt or x.txt)
'''

def train(N, smoothing=False):
	'''
	1. Takes each line in the training text, properly splits it apart;
	2. Counts frequency each phoneme is followed by some other and produces a bigram dictionary;
	3. Counts frequency each phoneme pair is followed by some other and produces a trigram dictionary;
	4. Returns two dictionaries 'bigram' and 'trigram'
	5. If smoothing == True add-1 smoothing will take place by adding 1 to every entry that has a value of 0
				Lots of dictionaries and embedded dictionaries...
	train is given:
			N:			there is one spot that we need to know if we are doing bi- or tri-grams
			smoothing:	if there is a 4th argument, smoothing is True, else is False
	train returns:
			bigram & trigram: it returns both of these no matter the N value or the smoothing gate
								bigram & trigram are our most important relative frequency dictionaries
	'''
	# 1.
	# t is the training doc of word/phonemes pairings
	t = open(sys.argv[1])
	# Probably a better name for this, but seemed simple enough to call it 'dictionary'
	dictionary = defaultdict(lambda:'')
	# Make a dictionary, keys are training words, values are the list of phonemes
	for x in t.readlines():
		entry = x.split()
		# insert our word-beginning #
		entry.insert(1,"#")
		# Add another "#" for trigrams
		if N == 3:
			entry.insert(1,"#")
		# append our word-ending #
		entry.append("#")
		# takes the first string, the orthographic word, as the key and the rest as the values.
		dictionary[entry.pop(0)] = entry
	t.close()
	# 2. & 3.
	# these two dictionaries could be returned or made global, it seemed easier to just make them global
	bigram = defaultdict(lambda:{})
	trigram = defaultdict(lambda:defaultdict(lambda:{}))
	
	# these three dictionaries will be used to created the relative frequency bigram and trigram dictionaries
	counts = defaultdict(lambda:0)
	bicounts = defaultdict(lambda:defaultdict(lambda:0))
	tricounts = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:0)))

	# here we start iterating over each word and creating counts for each phoneme pair and triplet
	for word in dictionary:
		# and each phoneme in the word (minus the word-ending # that we can ignore here)
		for phoneme in range(len(dictionary[word])-1):
			# frequency of all lone phonemes
			counts[dictionary[word][phoneme]]+=1
			# frequency of all [p1][p2]
			bicounts[dictionary[word][phoneme]][dictionary[word][phoneme+1]]+=1
		# go another level deep if trigram = True
		if N == 3:
			# frequency of all [p1][p2][p3]: we need a new for-loop to avoid asking it to iterate through more items than it has
			for phoneme in range(len(dictionary[word])-2):
				tricounts[dictionary[word][phoneme]][dictionary[word][phoneme+1]][dictionary[word][phoneme+2]]+=1
	for p1 in counts:
		# 5.	This will just add 1 to each of the 40 bottom level phoneme entries in bicounts and tricounts
		#			i.e. it adds 1 to 1600 keys in bicounts and 1 to 64000 keys in tricounts:  this will initialize
		#			keys not seen in the training data with a value of 1, and add 1 to whatever value
		#			already-existing keys have.
		if smoothing == True:
			for p2 in counts:
				bicounts[p1][p2]+=1
				for p3 in counts:
					tricounts[p1][p2][p3]+=1
		# Finishing the bigram and trigram dictionaries, finally
		for p2 in bicounts[p1]:
			bigram[p1][p2] = 2**(math.log(bicounts[p1][p2],2)-math.log(counts[p1],2))
			for p3 in tricounts[p1][p2]:
				#print p1,p2,p3,"accounts for",tricounts[p1][p2][p3],"out of", bicounts[p1][p2], "occurences of",p1,p2
				trigram[p1][p2][p3] = 2**(math.log(tricounts[p1][p2][p3],2)-math.log(bicounts[p1][p2],2))
				#print tricounts[p1][p2][p3],bicounts[p1][p2],p1,p2,p3
	# 4.
	return bigram, trigram

def bi_g_phoneme(p1, bigram):
	'''
	Essentially, this method of randomly choosing our phonemes can be represented with the following:
	We have four types of items: / | \ -  and ten items all together.  Each individual item has the same
	probability of being selected: 1/10 or .1, but each group has a different cumulative probabilty:
	/ = .4 | = .3 \ = .2 and - = .1               ////|||\\-
	So, then we can generate a random number between 0 and 1 (let's say .7865 for now)
	Since we are working with dictionaries where the order of items doesn't matter, we can just start
	taking any item's relative frequency and subtracting it from our random number, let's go in the order they
	are above: .7865-.4=.3865  .3865-.3=.0865 .0865-.2=less than zero, so \ wins.  And since higher
	frequency items will take up more of a range, they will be more likely to zero out the random number,
	and thus more likely to occur in our generated words.

	bi_g_phoneme is given:
			p1:			the preceding phoneme in word being generated
			bigram:		in order to determine the prob. of a phoneme pair
	bi_g_phoneme returns:
			p2:			the next phoneme in the word that is being generated
	'''

	rand = random.uniform(0,1)
	for p2 in bigram[p1]:
		rand-=bigram[p1][p2]
		if rand<0.0: return p2
	return p2

def tri_g_phoneme(p1, p2, trigram):
	'''
	This is the same as above, but just looks at the trigram situations instead of bigram
	tri_g_phoneme is given two preceding phonemes, in order to provide more context
	'''
	rand = random.uniform(0,1)
	for p3 in trigram[p1][p2]:
		rand-=trigram[p1][p2][p3]
		if rand<0.0:return p3
	return p3

def g_word(N, bigram, trigram):
	'''
	g_word produces a list of probabilistically generated phonemes (i.e. a word)
	g_word is given:
			N:	 		to decide between bigram or trigram
			bigram:	 	in order to give bi_g_phoneme the dictionary
			trigram: 	in order to give tri_g_phoneme the dictionary
	g_word returns:
			word: 		the list of phonemes (i.e. a word)
	'''
	# for bigrams
	if N == 2:
		# words for bigrams will start with a #
		word = "#"
		# can't set current into we are in the while loop
		current = ''
		# until current is an end-hash, run this loop
		while current != '#':
			if current == '': current = "#"
			# set current to a phoneme generated in bi_g_phoneme
			current = bi_g_phoneme(current, bigram)
			# add current to word
			word+=" " + current
	# for trigrams
	if N == 3:
		#The words for trigrams will start with # #
		word = "# #"
		current = ''
		# p1 is phoneme 1, p2 is phoneme 2.  At the start they are both #
		p1 = "#"
		p2 = "#"
		# until current is an end-hash, run through this loop
		while current != '#':
			if current == '':
				p1 = '#'
				p2 = '#'
			# set current to a phoneme generated in tri_g_phoneme
			current = tri_g_phoneme(p1,p2, trigram)
			# add current to word
			word+=" " + current
			# move each phoneme forward one
			p1 = p2
			p2 = current
	return word

def wordprob(N, bigram, trigram, entry):
	'''
	wordprob calculates the probability of each word (i.e. line in the test data)
	wordprob is given:
			N:	 		to decide between bigram or trigram
			bigram:	 	in order to find the probability of each phoneme pair
			trigram: 	in order to find the probability of each phoneme triplet
			entry:		the list of phonemes of the test word
	wordprob returns:
			prob: 		the word probability
			logprob:	the sum of the log of each pair/triplet's probability
	'''
	logprob= 0.0
	if N == 2:
		for i in range(1,len(entry)): logprob += math.log(bigram[entry[i-1]][entry[i]],2)
	if N == 3:
		for i in range(2,len(entry)): logprob += math.log(	trigram[entry[i-2]][entry[i-1]][entry[i]],2)

	prob = 2**logprob
	return prob, logprob

def main():
	# save the decision of bigram or trigram as N
	N = int(sys.argv[2])
	'''
	If there is a 4th argument, the script should:
	Build smooth ngram
	For words in 4th arg:
		Print Word, Tab, Probability of word
	Print perplexity
	'''
	try:
		if sys.argv[3]:
			#get information on the training data, produces two returned dictionaries: bigram and trigram
			bigram, trigram = train(N, smoothing=True)
			# logprobsum is the cumulative count of the log of the probability of each phoneme pair/triplet
			logprobsum = 0.0
			# corpus_size is my N (I already used an N variable, and don't want to get rid of it!)
			# corpus_size is the number of phonemes of the corpus, including the end #s of each word
			corpus_size = 0.0
			test = open(sys.argv[3])
			# run through all the "words" in the test doc, formatting them to be analyzed
			for x in test.readlines():
				x = re.sub("\n","",x)
				entry = x.split()
				# insert our word-beginning #
				entry.insert(0,"#")
				# Add another "#" for trigrams
				if N == 3:
					entry.insert(0,"#")
				# append our word-ending #
				entry.append("#")
				# get a probability for each word, and add the cumulative probabilities to logprobsum
				prob, logprob = wordprob(N, bigram, trigram, entry)
				logprobsum+=logprob
				corpus_size+=(len(entry)-(N-1))
				print x,"\t",prob
				#print "Word: {:<30}Prob: {:<20}OR    {:.10f}".format(x, prob, prob)
			# P is the perplexity/likelihood of the corpus, given the training data
			P = 2**(logprobsum*((-1)/corpus_size))
			print "{:<29} Perplexity: {:<20}".format("",P)

	# If there is no 4th argument, the script should:
	# Print 25 random words based on an unsmoothed Ngram
	except:
		bigram, trigram = train(N)
		if N == 2:
			prefix = "bi-"
		if N == 3:
			prefix = "tri-"
		r = 25
		print "Here are {} random words using unsmoothed {}grams:".format(r,prefix)
		for x in range(r):
			 print g_word(N, bigram, trigram)
if __name__ == "__main__":
    main()