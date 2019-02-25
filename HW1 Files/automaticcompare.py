
topten = []
knowncount1 = 0
knowncount2 = 0
myswordfreqs = {"food" : 0.023743221456837934,
	"eat" : 0.023450095266012775,
	"eating" : 0.013630367873369926,
	"dinner" : 0.013190678587132187,
	"taste" : 0.00894034882016737}


knownwordfreqs1 = {"food": 0.026453549242685934,
	"eat": 0.02212605569902755,
	"eating": 0.014811195644585632,
	"breakfast": 0.008599148460946985,
	"dinner": 0.008445592238430074}

knownwordfreqs2 = {	"wall": 0.02309179248733258,
	"build": 0.012420981139962263,
	"crime": 0.010174494540515883,
	"government": 0.010043884854501558,
	"fall": 0.009834909356878637}

for word, count in sorted(myswordfreqs.items(), key = lambda pair: pair[1], reverse = True)[:10]:
	topten.append(word)

for word in topten:
		if word in knownwordfreqs1: knowncount1+= knownwordfreqs1[word]
		if word in knownwordfreqs2: knowncount2+= knownwordfreqs2[word]

print knowncount1
print knowncount2
print "the highest # corresponds to the corpus with the same keywords."


