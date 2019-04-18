import sys
sys.path.append(../HW1 Files/)
from doit import cani

import re
from collections import defaultdict
import random
import math

x = sys.argv[1]
cani(x)

'''
def normalize(hist):
	x = sum(hist.values())

	for r in hist: hist[r] = float(hist[r])/x
'''
		

	#x = {k: float(v)/sum(hist.values()) for k, v in hist.iteritems()}
	#return x
	#print hist either prints the original hist, or if you use hist as
	#a variable in this def it just prints that.....

'''
hist = {"yes": 2, "no": 3}
print hist
normalize(hist)
print hist.values()
rank = 0
for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True):
	rank+=1
	print "%d:\t%-13.6f\t%s\t\t%f\t%f\n" % (rank,count,word,math.log(count),math.log(rank))
'''

#The below doesn't work, as x is only defined in def norm
#print x
