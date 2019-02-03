from collections import defaultdict
hist = {"word1": 3, "word2": 4}



for x in hist.values():
	print x/float(sum(hist.values()))


'''
for i in hist.values():
	v = i/x
	r =({hist.keys(): v})
print r
hist = r
print hist
#print hist.values()
'''

