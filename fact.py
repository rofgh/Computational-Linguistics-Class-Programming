# Factorial program:  Find the factorial for a user-given number
import sys

# def fact() is the actual factorial function
def fact():
	# x = int(input("				Please enter positive integer for which you want a factorialization: "))
	x = int(sys.argv[1])
	print "\n"
	print "				I am going to factorialize the number %d for you" % (x)
	f = x
	if x < 0:
		print "				Factorializing negative numbers isn't really a thing..."

	elif x == 0:
		print "				...the factorial of 0 is 1.  It's complicated."

	elif x == 1:
		print "				1.  The answer is 1.  Obvi."

	else:
		print "				...gimme a second..."
		while f > 1:
			f -= 1
			x = f * x
		print "				%d" % (x)
		print "\n"
	ask()

# def ask() is just the UI function for after a factorial has been calculated, in order to quit or re-iterate the script...
def ask():
	print "				Would you like another factorial?"
	a = input("				1 = yes, 2 = no: ")
	if a == 1:
	    print "\n"
	    sys.argv[1] = int(input("				Please enter positive integer for which you want a factorialization: "))
	    fact()

	elif a == 2:
	    print "				Okay, goodbye. Script ending..."
	    exit()

	else:
	    print "				Error:"
	    ask()

# is there some other way to cover over the sys.argv[1]...?
if len(sys.argv) < 2:
	sys.argv.insert(1, input("				Please enter positive integer for which you want a factorialization: "))
	fact()

else:
	fact()

ask()

		


