import re

def clean(line):
	line = line.decode('utf8')
	#Getting rid of twitterhandles
	line = re.sub(u'@\w+','@@@',line)
	#Getting rid of urls
	line = re.sub(u'http\S+','www',line)
	#Getting rid of hashtags
	line = re.sub(u'#\S+','###',line)
	#deleting hyphens and apostrophe (' and the other slanty apostrophe which I am not allowed to write in here without getting a SyntaxError... are different!!) in word-middles
	line = re.sub(u"-|('|’)",'',line)
	#Getting rid of start of line and end of line whitespace
	line = re.sub(u'(^\s+|\s+$)','',line)
	#Getting rid of numbers, too. Because they don't seem significant at the moment
	line = re.sub(u'\d+','',line)
	#Getting rid of puncuation
	line = re.sub(u'\W+',' ',line)
	# MAYBE THIS IS BETTER?line = re.sub(u'(\s|^)\W+|\W+(\s|$)',' ',line)
	#And all single letter words...
	line = re.sub(ur'\b\w\b',' ',line)
	#lowercasing all
	line = line.lower()

	return line

lines = ['',
		"!Hellow!",
		"Rronalds@gmail.com send me @rofgh an email!",
		"@rofgh my dinner. 24 hours Hope-fully it's done.",
		"httpwww.gmail.com Is this not Wor-king now?",
		'didn\’t If it isn\’t Food Porn I didn\'t want3 don\'t it didn\'t,'
		'@rofgh',
		"#foodporn",
		'w',]

for x in lines:
	print clean(x)




#command for all files: python twitterFrequency.py tweets_corpus_all.txt tweets_corpus1.txt tweets_corpus2.txt tweets_corpus3.txt tweets_corpus4.txt tweets_corpus5.txt tweets_corpus_mystery.txt 
