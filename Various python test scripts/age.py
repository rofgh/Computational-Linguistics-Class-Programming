print "Please enter your age"
x = int(raw_input())
print "Please enter your name"
y = raw_input()

z = 100-x
if z == 1:
	print "%s, you will turn 100 in %d year" % (y, z)
else:
	print "%s, you will turn 100 in %d years" % (y, z)