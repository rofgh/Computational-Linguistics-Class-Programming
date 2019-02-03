import sys

f = open(sys.argv[1])
word = sys.argv[2]
d = {}

for line in f.readlines():
	words = line.split()
	for w in words:
		if w == word: 
			if w in d: d[word] += 1
			else: d[word] = 1

print d[word]