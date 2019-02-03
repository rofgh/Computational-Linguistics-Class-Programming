import re

def clean(line):
	line = line.decode('utf8')
	#Getting rid of twitterhandles#
	line = re.sub(u'.*@.+','@@@',line)
	#Getting rid of urls#
	line = re.sub(u'http.+','www',line)
	#Getting rid of hashtags#
	line = re.sub(u'#.+','###',line)
	#And all single letter words...
	line = re.sub(u'\s\w\s',' ',line)
	#Getting rid of puncuation#  
	line = re.sub(u'\W+\b',' ',line)
	#Getting rid of whitespace#  
	line = re.sub(u'(^\s+|\s+$)','',line)
	#Getting rid of numbers, too. Because they don't seem significant at the moment
	line = re.sub(u'\d+','',line)
	#lowercasing all#
	line = line.lower()
	return line


line = ''
line1 = "Hellow!"
line2 = "Rronalds@gmail.com"
line3 = "my dinner. Hopefully it's done."
line4 = "Is this not Working now?"
line5 = 'Porn I don\'t want it'

print clean(line)
print clean(line1)
print clean(line2)
print clean(line3)
print clean(line4)
print clean(line5)

