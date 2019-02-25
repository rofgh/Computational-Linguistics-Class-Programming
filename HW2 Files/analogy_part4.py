#sys allows us to use arguments after the .py script on the command line
import sys
#collections is a group of "high-performance" container datatypes;
#defaultdict is a dictionary that has a default value defined for non-existent key, such that no error will be raised
from collections import defaultdict
#regular expressions
import re
#"psuedo-" random number generation
import random
#The def min_edit from our min_edit file
from min_edit_part4 import min_edit
#math is a group of mathematical functions (log, pi, sin/cos, etc.); natlog e = 1
from math import e

# def pearson: from -1 to 1, the linear relation between two numbers
### calculates pearson correlation btwn two lists of numbers
def pearson(v1,v2):
	if len(v1)!=len(v2): return None
	s1 = sum(v1)
	s2 = sum(v2)
	m1 = s1/len(v1)
	m2 = s2/len(v2)
	xy = 0.0
	xx = 0.0
	yy = 0.0
	for i in range(len(v1)):
		xy += (v1[i]-m1)*(v2[i]-m2)
		xx += (v1[i]-m1)*(v1[i]-m1)
		yy += (v2[i]-m2)*(v2[i]-m2)
	return xy/((xx**.5)*(yy**.5))

def get_training(f):
###	returns the training data as three dictionaries:
### the verb's orthographic singular form is the key of each one
### pres[verb] gives the phonetic transcription of the verb's present form
### past[verb] gives the phonetic transcription of the verb's past form
### label[verb] gives the morphological rule category
### morphclass[morph] gives a dictionary of past tense classes each with {orth: ppres}
	pres = defaultdict(lambda:'')
	past = defaultdict(lambda:'')
	label = defaultdict(lambda:'')
	morphclass = defaultdict(lambda:{})
	for v in f.readlines():
		#Splits the string into a list, according to the , separator
		orth, ppres, opast, ppast, cat = v.split(',')
		pres[orth] = ppres
		past[orth] = ppast
		morph = cat.strip()
		label[orth] = morph
		morphclass[morph][orth] = ppres
	f.close()
	return (pres, past, label, morphclass)

### takes a phonetic transcription of a wug verb, a dictionary
### of actual verb forms to compare it to, and a number n.
### returns all neighbors within n as a dictionary of neighbor, distance pairs
### if n is negative (by default), all neighbors are returned
def get_neighbors(wugphon='', dict={}, n=-1):
	neighbors = defaultdict(lambda:0.0)
	for v in dict:
		d = min_edit(wugphon,dict[v])
		if d <= n or n < 0: 
			neighbors[v] = d
	return neighbors

### takes dictionary of neighbor, distance pairs and returns overall similarity
def similarity(neighbors):
	s = .6
	sim = 0.0
	for n,d in neighbors.items():
		sim += e**(-d/s)
	return (sim)

### takes two lists of responses and returns the proportion that match
def accuracy(v1,v2):
	tot = len(v1)
	matches = 0.0
	for x,y in zip(v1,v2): 
		if x==y: matches += 1
	return matches/tot

def main():
	# The real english words to train on
	trainf = open(sys.argv[1])
	# The wugs
	testf = open(sys.argv[2])
	# g_t will return four dicts, {orth, ppres} {orth, ppast} {orth, cat} &
	# morphclass, which is a dictionary of dictionaries, in order to be able to feed it back into get_n
	pres, past, label, morphclass = get_training(trainf)

	# some output files to be uncommented for some different analyses
	#soutfile = open("sim_out.txt",'w')
	'''
	routfile = open("responses_out.txt", "w")
	moutfile = open("morph_out.txt", "w")
	output = "Wug:\t\tResponse:\t\tPrediction:\n"
	moutfile.write(output)
	'''
	# some lists to append to while running through the wugs
	unmatchCount = 1
	responses = []	# will contain human forced choice responses
	ratings = []	# will contain human wellformedness ratings
	sims = []		# will contain predicted ratings based on similarity
	preds = []		# will contain predicted forced choice responses based on analogy
	for wug in testf.readlines():
		f = wug.split(',')
		# skip header linef
		if "Orth" in wug: continue
		# extract & store wug data from test file
		orth, phon, rating, regpast, regscore, irregpast, irregscore, irregclass = f[0], f[1], float(f[2]), f[3], float(f[4]), f[5], float(f[6]), f[7].strip()
		# add rating for this wug to the list
		ratings.append(float(rating))
		# determine participants' preferred past category
		response = ""
		if regscore < irregscore: 
				response = irregclass		# participants preferred irregular
				# score = "irregular preferred: "
		else:	# participants preferred the regular
			# determine & store the regular transformation
			#score = "regular preferred: "
			if regpast[-2:] == 'Id':
						response = "NULL->Id"
			elif regpast[-1:] == 'd':
						response = "NULL->d"
			elif regpast[-1:] == 't':
						response = "NULL->t"
		# store participants' preferred past category
		responses.append(response)
		#routput = "%s\t%s\t%s\t%s\t%s\t%s\n" % (orth, phon, regpast, irregpast, score, response)
		#routfile.write(routput)

		### PART 2
		presneighbors = get_neighbors(phon,pres)
		# print presneighbors
		sim = similarity(presneighbors)
		sims.append(sim)
		# print orth,"\t", sim, "\t", rating
		#output = "%s,%s:\n%s\n\n" % (orth, phon, str(presneighbors))
		#soutfile.write(output)


		### PART 3
		lowestSim = 0
		classMatch = ""
		for r in morphclass:
			morphneighbors = get_neighbors(phon, morphclass[r])
			morphsim = similarity(morphneighbors)
			if lowestSim < morphsim:
				lowestSim = morphsim
				classMatch = r
		# print phon, classMatch
		preds.append(classMatch)
		
		### Print to terminal: comparing preferred past past tenses to predicted past tenses
		if classMatch != response:
			print "{0:<3}Wug:{1:<15}Preferred:{2:<15}Predicted:{3:<15}Similarity:{4:<5}".format(unmatchCount, orth, response, classMatch, sim)
			unmatchCount +=1

		### For printing to an outfile: comparing preferred past past tenses to predicted past tenses
		'''
		if classMatch != response:
			response = "correct prediction!"
			classMatch = ""
		output = "%s:\t\t%s\t\t\t%s\n" % (orth, response, classMatch)
		moutfile.write(output)
		'''

	testf.close()
	# soutfile.close()
	# routfile.close()
	# moutfile.close()
	print "Correlation Ratings X Similarities:", pearson(ratings,sims)
	print "Accuracy of Analogical Predictions:", accuracy(responses,preds)

if __name__ == "__main__":
    main()


# to run code:  python analogy.py train.csv test.csv







