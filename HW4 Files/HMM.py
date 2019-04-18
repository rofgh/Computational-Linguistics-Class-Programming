'''
The following should be run on the CL:  python hmm.py
'''



from collections import defaultdict
import math

# the transit and emit matrices as dictionaries
transit =   {'N':{'N':0.54, 'V':0.23, 'R':0.08, '#':0.15}, 'V':{'N':0.62, 'V':0.17, 'R':0.11, '#':0.10}, 'R':{'N':0.17, 'V':0.68, 'R':0.10, '#':0.05}, '#':{'N':0.7, 'V':0.2, 'R':0.1, '#':0.0}}
emit =      {'N':{'time':0.98, 'flies':0.015, 'quickly':0.005, '#':0.0}, 'V':{'time':0.33, 'flies':0.64, 'quickly':0.03, '#':0.0}, 'R':{'time':0.01, 'flies':0.01, 'quickly':0.98, '#':0.0}, '#':{'time':0.0, 'flies':0.0, 'quickly':0.0, '#':1.0}}
# Define a new emission matrix B2 for Question 4
B2 =       {'N':{'time':0.84, 'flies':0.155, 'quickly':0.005, '#':0.0}, 'V':{'time':0.13, 'flies':0.24, 'quickly':0.03, '#':0.0, 'swat':0.4}, 'R':{'time':0.01, 'flies':0.01, 'quickly':0.98, '#':0.0}, '#':{'time':0.0, 'flies':0.0, 'quickly':0.0, '#':1.0}}
# two data structures you may find useful for mapping between tags and their (arbitrary) indices
tagnum = {"N":0,"V":1,"R":2,"#":3}    #gives index for a given tag
numtag = ['N','V','R','#']   #gives tag for a given index

'''
print_table will produce a table of all the probabilities of each node--
depending on whether it is called from forward or viterbi, the probabilities will correspond to that method
from the if backpointers[0] line onwards, if print_table is being called from viterbi, it will also produce
the best tag sequence for the sentence.  (There is no best for forward, since forward is all the sequences, duh)
I am sure there is a better way to do the backpointers (a tuple, like asked for in the instructions, presumably)
but this works and I don't feel it's worth changing...
'''
def print_table(table, words, backpointers, ef='%.4f', colwidth=12):
    tags = transit.keys()
    print ''.ljust(colwidth),
    for w in words:
        print str(w).ljust(colwidth),
    print
    for n in range(len(transit.keys())):
        print str(numtag[n]).ljust(colwidth),
        for t in range(len(words)):
            out = str(table[n][t])
            if type(table[n][t]) == tuple: 
                form=ef+",%s"
                out = form % (table[n][t][0], table[n][t][1])
            elif type(table[n][t]) == float:
                out = str(ef % table[n][t])
            print out.ljust(colwidth),
        print
    if backpointers[0] != 'forward':
        print "Viterbi Probability of",
        x = [0]*len(words)
        for n in range(len(words)-1, -1, -1):
            try:
                x[n] = backpointers[y][n+1]
                y = tagnum[x[n]]
            except:
                x[n] = "#"
                y = tagnum[x[n]]
        for n in range(len(x)):
            print x[n],
        print "is",
    else:
        print "Forward Probability is",
    
'''
forward produces a table (list of lists) of all probabilities for reaching each node.
forward is given:
    ws:         the sentence to be looked at
    transit:    the transition probabilities for the parts of speech
    emit:       the emission probabilites for each word, cataloged by its POS 
                (there are two different emission tables, B2 being the one that contains 'swat')
forward returns:
    table:      the table of probabilities, table[x][y] --
                        x is the POS tag (or the # that corresponds to this in tagnum)  (0-3)
                        y is the step (or the word) being looked at, using range(T-1) (0-4)
                        table[x][y] will give the float(probability) for all sequences that arrive at that square
    sentence:   this is ws with a hash added to the beginning and end, and each word is an item in a list
    backpointers: this is meaningless in forward, but print_table needs it, so forward provides a dummy backpointers
'''
def forward(ws, transit, emit):
    sentence = ['#']
    for x in range(len(ws)):
        sentence.append(ws[x])
    sentence.append('#')
    T = len(sentence)
    #   for playing with 'qtf' sentences:
    #   sentence = ['#', 'quickly', 'time', 'flies', '#']    
    #   print sentence
    table =             [[0.0] * T for t in range(len(numtag))]
    backpointers =      ['forward']
    table[len(numtag)-1][0] = 1.0
    for x in range(len(numtag)-1):
        table[x][0] = 0.0
    for step in range(T-1):
        for x in range(len(numtag)):
            for y in range(len(numtag)):
                try:
                    table[x][step+1] += 2**(math.log((table[y][step]),2)+
                                            math.log((transit[numtag[y]][numtag[x]]),2)+
                                            math.log((emit[numtag[x]][sentence[step+1]]),2))
                except:
                    continue
    print_table(table, sentence, backpointers)
    return table[len(numtag)-1][T-1]

'''
viterbi produces a table (list of lists) of the probabilities for each best sequence.
viterbi is given:
    ws:         the sentence to be looked at
    transit:    the transition probabilities for the parts of speech
    emit:       the emission probabilites for each word, cataloged by its POS 
                (there are two different emission tables, B2 being the one that contains 'swat')
viterbi returns:
    table:      the table of best sequence probabilities, table[x][y] --
                        x is the POS tag (or the # that corresponds to this in tagnum)  (0-3)
                        y is the step (or the word) being looked at, using range(T-1) (0-4)
                        table[x][y] will give the float(probability) for the best sequence to arrive at that square
    sentence:   this is ws with a hash added to the beginning and end, and each word is an item in a list
    backpointers: this takes the tag (y) for a previous square for whatever proportion was the maximum for
                    getting to the current square, and saves one tag per square in a table. (Unless there is a zero
                    probability, then it will store nothing)
'''

def viterbi(ws, transit, emit):
    sentence = ['#']
    for x in range(len(ws)):
        sentence.append(ws[x])
    sentence.append('#')
    T = len(sentence)
    #   for playing with 'qtf' sentences:
    #   sentence = ['#', 'quickly', 'time', 'flies', '#']     
    #   print sentence
    table =             [[0.0] * T for t in range(len(numtag))]
    backpointers =      [[None] * T for t in range(len(numtag))]
    table[len(numtag)-1][0] = 1.0
    for x in range(len(numtag)-1):
        table[x][0] = 0.0
    for step in range(T-1):
        for x in range(len(numtag)):
            for y in range(len(numtag)):
                macks = 0.0
                try:
                    macks = 2**(math.log((table[y][step]),2)+
                                math.log((transit[numtag[y]][numtag[x]]),2)+
                                math.log((emit[numtag[x]][sentence[step+1]]),2))
                except:
                    continue
                if macks > table[x][step+1]:
                    table[x][step+1] = macks
                    backpointers[x][step+1] = numtag[y]
    #for f in backpointers:
    #    print f
    print_table(table, sentence, backpointers)
    return table[len(numtag)-1][T-1]


### MAIN CODE GOES HERE ###
# sets the sentence used in the next two meaningful print statements the be 'tfq'
seq = ('time','flies','quickly')
print
print "Calculating forward probability of", seq, ":\n", forward(seq, transit, emit), '\n'
print "Calculating most likely tags for", seq, ":\n", viterbi(seq, transit, emit), '\n'
# Changes sentence to 'sfq'
seq = ('swat','flies','quickly')
print "Calculating most likely tags for", seq, ":\n", viterbi(seq, transit, B2), '\n'