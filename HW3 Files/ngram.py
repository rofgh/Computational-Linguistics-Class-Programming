import sys
import random
import re
from collections import defaultdict
from timeit import default_timer as timer

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

def train():
	'''
	1. Takes each line in the training text, properly splits it apart;
	2. Counts frequency each phoneme is followed by some other and produces a bigram dictionary;
	3. Counts frequency each phoneme pair is followed by some other and produces a trigram dictionary
	4. Doesn't return anything but creates two global dictionaries 'bigram' and 'trigram'
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
		dictionary[entry.pop(0)] = entry
	t.close()

	# these two dictionaries could be returned or made global, it seemed easier to just make them global
	global bigram
	bigram = defaultdict(lambda:{})
	global trigram
	trigram = defaultdict(lambda:defaultdict(lambda:{}))
	
	# these three dictionaries will be used to created the relative frequency bigram and trigram dictionaries
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


def bi_g_phoneme(p1):
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

def tri_g_phoneme(p1,p2):
	'''
	This is the same as above, but just looks at the trigram situations instead of bigram
	'''
	rand = random.uniform(0,1)
	for p3 in trigram[p1][p2]:
		rand-=trigram[p1][p2][p3]
		if rand<0.0:return p3
	return p3

def g_word():
	rand = random.uniform(0,1) 
	if N == 2:
		word = "#"
		current = ''
		while current != '#':
			if current == '': current = "#"
			current = bi_g_phoneme(current)
			word+=" " + current
	if N == 3:
		word = "# #"
		current = ''
		p1 = "#"
		p2 = "#"
		while current != '#':
			if current == '':
				p1 = '#'
				p2 = '#'
			current = tri_g_phoneme(p1,p2)
			word+=" " + current
			p1 = p2
			p2 = current
	return word

def main():
	tic()
	# save the decision of bigram or trigram as N
	global N
	N = int(sys.argv[2])
	# Determine whether to run a bi-gram or a tri-gram or return an error
	biortri(N)
	#get information on the training data, produces two global dictionaries: bigram and trigram
	train()
	#print a number of generated words equal to the following range
	for x in range(5):
		print g_word()
	toc()

if __name__ == "__main__":
    main()



# at the command line: python ngram.py train.py 2/3





'''
for fphoneme in counts.keys():
		print "{:>2} {} {:>2} {}".format(fphoneme, "appears",counts[fphoneme],"times")
		for sphoneme in bicounts[fphoneme]:
			print "{} {} {:>2} {}".format("         followed by",sphoneme,bicounts[fphoneme][sphoneme],"times")
			if N == 3:
				for tphoneme in tricounts[fphoneme][sphoneme]:
					print "{} {} {:>2} {}".format("                  followed by",tphoneme,tricounts[fphoneme][sphoneme][tphoneme],"times")
'''