# import sys to make command line arguments accessible
import sys

# store first argument as 'num'
num = sys.argv[1]

# set first two numbers to 0, 1
fib1,fib2  = 0,1

# check to make sure num is a valid position, otherwise exit
if int(num) < 1:
    print "please give me a postive integer and try again"
    exit()

# print first one or two numbers of the sequence, depending on num
print "The fib number at 1 is " + str(fib1)
if int(num)!=1: print "The fib number at 2 is", fib2

# print out the fibonacci sequence from 3 to num 
i=3
while i <= int(num):
    fib1, fib2 = fib2, fib1 + fib2
    print "The fib number at " + str(i) + " is " + str(fib2)
    i += 1