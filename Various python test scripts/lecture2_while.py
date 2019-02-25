import sys

f = open(sys.argv[1])
word = sys.argv[2]
counter = 0

lines = f.readlines()
while lines:
	line = lines.pop(0)
	words = line.split()
	while words:
		w = words.pop()
		if w == word: counter += 1

print counter