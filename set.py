'''Prompt:At-Home Coding Problem
 
Implement a command console for changing settings on a particular object. The command console should allow you to enter a string and will return the response (very similar to a terminal session). The commands are as follows:
 
SET propertyname=newvalue will change the target object's member named "propertyname" to have a value equal to "newvalue". If the input value is incompatible (e.g. an int being set to a string), print out an appropriate error message.
 
GET propertyname will print out the current value of the target object's member named "propertyname".
 
GET * will print out a list of all target object members and their current values.
 
The system should be extensible for future commands and should accept an arbitrary object, such that another developer could insert another object into the system and rely on the command console to get and set the properties correctly.

'''

import sys

class property:
	prop = "Default"
	name = "Default"


def set(x):
	try:
		x, y = x.split("=")
		# x is name, y is new value/property
		print "You are giving object {} the {} property".format(x, y)
		#set x's property to y
		proppedx = property("%s" % (x), "%s" % (y))
		print "Name: {:<20}Property: {} ".format(proppedx.name, proppedx.prop)
	except ValueError:
		print "did you use the format 'propertyname=newvalue'??"

	
def get(x):
	if x == "*":
		print "List of all Property objects:"
		for x in property.name:
			print property.name
	else: 
		x = property()
		x.name = "Roy"
		print "Name: {:<20}Property: {} ".format(x.name, x.prop)

def main():
	getset = sys.argv[1]
	x = sys.argv[2]

	if getset == "set":
		set(x)

	if getset == "get":
		get(x)




if __name__ == "__main__":
    main()