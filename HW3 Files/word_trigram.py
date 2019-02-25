import re
import sys
import random
from collections import defaultdict

# keeps generating words until # is randomly generated, then returns the whole sentence
def generate_sentence():
    sentence = "# #"
    # keeps track of immediately prior symbol
    current = ''
    # keeps track of immediately prior pair of symbols
    context = ("#","#")
    while current is not '#':
        if current == '': context = ('#','#')
        current = generate_word(context)
        context = (context[1],current)
        sentence += " " + current
    return sentence

#given a pair of words, randomly generates and returns the next word using the trigram model
def generate_word(pair):
    # generate a random float between 0 and 1
    # we will use this float to probabilistically select a 'bin'
    # corresponding to a word in our bigram model
    rand = random.uniform(0,1)
    # go through each possible second word
    for following in trigram[pair]:
        # subtract this word's probability from rand 
        rand -= trigram[pair][following]
        # as soon as we 'cross over' zero we have found the word for that bin
        if rand < 0.0: return following
    return following

# open file for training the trigram model
language = open(sys.argv[1]) 

# defaultdict takes a lambda function as an argument and uses it to set the default value for every key
# this makes it easy to build up the dictionaries without checking for each key's existence
bicounts = defaultdict(lambda:0)
tricounts = defaultdict(lambda:defaultdict(lambda:0))

# this loops through all the data and stores counts
for line in language:
    # we have to have a way to begin and end each line
    line = "# # " + line.strip() + " #"
    words = re.split(r'[,.?"!\s:;]+|--', line)

    # we go through each position and keep track of word and word pair counts
    for i in range(len(words)-2):
        # create a tuple of two words that defines the context for the trigram 
        pair = (words[i],words[i+1])
        # increment the count for this pair of words
        bicounts[pair] = bicounts[pair] + 1
        # increment the count for this pair of words followed by the next word in the sequence
        tricounts[pair][words[i+2]] = tricounts[pair][words[i+2]] + 1
        
language.close()

trigram = defaultdict(lambda:{})

# this loops through all word pairs and computes relative frequency estimates
for pair in tricounts:
    for word in tricounts[pair]:
        trigram[pair][word] = float(tricounts[pair][word])/float(bicounts[pair])
        #print "P(" + word2 + " | " + word1 + ")\tis\t" + str(bigram[word1][word2])

# print 20 random 'sentences' using the bigram
for i in range(20):
    print generate_sentence()

