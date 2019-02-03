# Factorial program:  Find the factorial for a user-given number
def fact():
	print("Please enter positive integer for which you want a factorization:")
	x = input()
	f = x
	if x < 0:
		print "				No value for negative numbers"
	elif x == 0:
		print "				factorial of 0 is 1.  It's complicated."
	elif x == 1:
		print "				1.  The answer is 1.  Obvi."

	else:
		print "				...gimme a minute..."
		print "				Okay, I got it:"
		while f > 1:
			f -= 1
			x = f * x
		print "							", x
	print "Want another factorial?"
	print "1 = yes, 2 = no"
	a = input()
	if a == 1:
	    fact()
	elif a == 2:
	    print "				Okay, goodbye, script ending..."
	    exit()
	else:
	    print("Error: Answer must be 1 or 2")
fact()

		

