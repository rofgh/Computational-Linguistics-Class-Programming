# write a python script that is run at the command line as follows:
# >python wordfreq.py FILENAME

# It should print out the frequency of every 'word' (every string separated by
# spaces) in the file. For extra fun and more practice, get the program to
# print the output in decreasing order of frequency and/or deal with
# punctuation and capitalization.

import sys
import string
   
# saving the word file as a variable
f = open(sys.argv[1])

all = f.readlines()
# the list that will populate with modified words and then turn into a dictionary
single = []
# Used for getting rid of numbers from the strings later
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
for x in all:
	for y in x:
		if y in numbers:
			x = x.replace(y, "")
		if y in string.punctuation:
			x = x.replace(y, " ")
	y = x.lower()
	v = y.split()
	for t in v:
		single.append(t)
single.sort()
dic = dict((x,single.count(x)) for x in set(single))
f.close()

# UI: 
if len(sys.argv)==2:
	e = input("Would you like to search for a specific word in this file? y=1/n=2:    ")
	if e == 1:
		print ("Please type the word for which you would like to look:")
		s = raw_input()
		if s in dic:
			print "The word '%s' appears in the text %s times." % (s, dic[s])
		else:
			for key in sorted(dic.iterkeys()):
	   			print "%s: %s" % (key, dic[key])
	   		print "Your word, '%s', wasn't found, but feel free to look for it above!" % (s)
	if e == 2:
		o = input("Would like to see the word list alphabetically (1) or by frequency (2)?:    ")
		if o == 1:
			for key in sorted(dic.iterkeys()):
				print "%s: %s" % (key, dic[key])
		if o == 2:
			for key, value in sorted(dic.iteritems(), key=lambda (k,v): (v,k)):
    				print "%s: %s" % (key, value)
if len(sys.argv)==3:
	s = sys.argv[2]
	if s in dic:
		print "The word '%s' appears in the text %s times." % (s, dic[s])
	else:
		for key in sorted(dic.iterkeys()):
			print "%s: %s" % (key, dic[key])
		print "Your word, '%s', wasn't found, but feel free to look for it above!" % (s)
