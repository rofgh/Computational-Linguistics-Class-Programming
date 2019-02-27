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
# tic and toc: time the operation from beginning to end and return a time at the end.
def tic():
    global start
    start = timer()

def toc():
    end = timer()
    elapsed = (end - start)
    print('Time passed: %.5f sec' % (elapsed))

# Take N and decide between a bi-gram, tri-gram or return an error
def biortri(N):
	if N == 2 or N == 3:
		return
	else:
		print "Sorry, this program can't handle anything except bigrams or tri-grams at the moment!"
		exit()

def train(N, smoothing=False):
	'''
	1. Takes each line in the training text, properly splits it apart;
	2. If smoothing == True, the default dictionaries for bicount or tricount are lambda:1
	3. Counts frequency each phoneme is followed by some other and produces a bigram dictionary;
	4. Counts frequency each phoneme pair is followed by some other and produces a trigram dictionary;
	5. Returns two dictionaries 'bigram' and 'trigram'
				Lots of dictionaries and embedded dictionaries...
	'''
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

	# these two dictionaries could be returned or made global, it seemed easier to just make them global
	bigram = defaultdict(lambda:{})
	trigram = defaultdict(lambda:defaultdict(lambda:{}))
	
	# these three dictionaries will be used to created the relative frequency bigram and trigram dictionaries
	# If add-1 smoothing is true, the default dictionaries will start with a 1 lambda value
	if smoothing == True:
		counts = defaultdict(lambda:1)
		bicounts = defaultdict(lambda:defaultdict(lambda:1))
		tricounts = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:1)))
	else:
		counts = defaultdict(lambda:0)
		bicounts = defaultdict(lambda:defaultdict(lambda:0))
		tricounts = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:0)))

	# here we start iterating over each word
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
	# here we create the relative frequency dictionaries and save them to bigram and trigram, respectively
	for p1 in counts:
		for p2 in bicounts[p1]:
			bigram[p1][p2] = float(bicounts[p1][p2])/float(counts[p1])
			for p3 in tricounts[p1][p2]:
				#print p1,p2,p3,"accounts for",tricounts[p1][p2][p3],"out of", bicounts[p1][p2], "occurences of",p1,p2
				trigram[p1][p2][p3] = float(tricounts[p1][p2][p3])/float(bicounts[p1][p2])
	return bigram, trigram


def bi_g_phoneme(p1, bigram):
	'''
	Essentially, this method of randomly choosing our phonemes can be represented with the following:
	We have four types of items: / | \ -  and ten items all together.  Each individual item has the same
	probability of being selected: 1/10 or .1, but each group has a different cumulative probabilty:
	/ = .4 | = .3 \ = .2 and - = .1               ////|||\\-
	So, then we can generate a random number between 0 and 1 (let's say .7865 for now)
	Since we are working with dictionaries where the order of items doesn't matter, we can just start
	taking any item's relative frequency (though it will always be item[0], we just won't have any idea
	which item that actually is) and subtracting it from our random number, let's go in the order they
	are above: .7865-.4=.3865  .3865-.3=.0865 .0865-.2=less than zero, so \ wins.  And since higher
	frequency items will take up more of a range, they will be more likely to zero out the random number,
	and thus more likely to occur in our generated words.
	'''

	rand = random.uniform(0,1)
	for p2 in bigram[p1]:
		rand-=bigram[p1][p2]
		if rand<0.0: return p2
	return p2

def tri_g_phoneme(p1, p2, trigram):
	'''
	This is the same as above, but just looks at the trigram situations instead of bigram
	'''
	rand = random.uniform(0,1)
	for p3 in trigram[p1][p2]:
		rand-=trigram[p1][p2][p3]
		if rand<0.0:return p3
	return p3

def g_word(N, bigram, trigram):
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

def mysdict(N):
	mysdictionary = defaultdict(lambda:'')
	mys = open(sys.argv[3])
	for x in mys.readlines():
		entry = x.split()
		# insert our word-beginning #
		entry.insert(0,"#")
		# Add another "#" for trigrams
		if N == 3:
			entry.insert(0,"#")
		# append our word-ending #
		entry.append("#")
		# takes the first string, the orthographic word, as the key and the rest as the values.
		mysdictionary[x] = entry
	return mysdictionary

def wordprob():


def perplexity(N, bigram, trigram, mys):
	# logsum is the 
	logsum = 0.0
	# corpusSize is my N (I already used an N variable, and don't want to get rid of it!)
	# corpusSize is the product of the probability of each phoneme of the corpus, including the end #s
	# of each word
	corpusSize = 0
	'''
	If N == 2, use bigram to determine the perplexity of the test file, which is represented by the mys dictionary
	If N == 3, use trigram to determine the perplexity of the test file, which is represented by the mys dictionary
	(both of these should automatically have add-1 smoothing applied with the 4th argument gate)
	'''
	if N == 2:
		bigram
	if N == 3:
		trigram

	P = 2**(logsum*((-1)/corpusSize))




def main():
	tic()
	# save the decision of bigram or trigram as N
	N = int(sys.argv[2])
	# Determine whether to run a bi-gram or a tri-gram or return an error
	biortri(N)
	'''
	If there is a 4th argument, the script should:
	Build smooth ngram
	For words in 4th arg:
		Print Word, Tab, Probability of word
	Print perplexity
	CAN I CHANGE THE BIGRAMS TO START WITH 1???
	'''
	try:
		if sys.argv[3]:
			bigram, trigram = train(N, smoothing=True)
			mys = mysdict(N)

			for x in mys:
				prob = wordprob(x)
				print prob
			P = perplexity(bigram, trigram, mys)
			for x in mys:
				print mys[x], 
			print P
	# If there is no 4th argument, the script should:
	# Print 25 random words based on an unsmoothed Ngram
	except:
		#get information on the training data, produces two returned dictionaries: bigram and trigram
		bigram, trigram = train(N)
		print "Here are 25 random words using unsmoothed Ngrams."
		for x in range(25):
			print g_word(N, bigram, trigram)
	# Finish timer
	toc()

if __name__ == "__main__":
    main()








'''
for fphoneme in counts.keys():
		print "{:>2} {} {:>2} {}".format(fphoneme, "appears",counts[fphoneme],"times")
		for sphoneme in bicounts[fphoneme]:
			print "{} {} {:>2} {}".format("         followed by",sphoneme,bicounts[fphoneme][sphoneme],"times")
			if N == 3:
				for tphoneme in tricounts[fphoneme][sphoneme]:
					print "{} {} {:>2} {}".format("                  followed by",tphoneme,tricounts[fphoneme][sphoneme][tphoneme],"times")
'''