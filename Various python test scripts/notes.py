		t = t.strip(",")
		t = t.strip("?")
		t = t.strip(".")
		t = t.strip("]")
		t = t.strip("[")
		t = t.strip("/")


		
if len(sys.argv)==3:
	s = sys.argv[2]
	if s in dic:
		print "%s: %s" % (s, dic[s])
	else:
		for key in sorted(dic.iterkeys()):
   			print "%s: %s" % (key, dic[key])
   		print "Your word, '%s', wasn't found, but feel free to look for it above!" % (s)
if len(sys.argv)==2:
	for key in sorted(dic.iterkeys()):
   		print "%s: %s" % (key, dic[key])
   	print "      If you would like to search an individual word, add it as a"
   	print "      second argument after the filename..."	
