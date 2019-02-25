import sys

fname = sys.argv[1]
word = sys.argv[2]

f = open(fname)
#f is now a file object

lines = f.readlines()

while lines:
	line = lines.pop(0)
	words = line.split()
	print words
	

