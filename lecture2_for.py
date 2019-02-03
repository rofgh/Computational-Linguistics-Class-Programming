import sys

f = open(sys.argv[1])
word = sys.argv[2]
counter = 0

for line in f.readlines():
	words = line.split()
	for w in words:
		if w == word: counter += 1

print counter