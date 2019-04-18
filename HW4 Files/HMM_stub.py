# the A and B matrices as dictionaries
A = {'N':{'N':0.54, 'V':0.23, 'R':0.08, '#':0.15}, 'V':{'N':0.62, 'V':0.17, 'R':0.11, '#':0.10}, 'R':{'N':0.17, 'V':0.68, 'R':0.10, '#':0.05}, '#':{'N':0.7, 'V':0.2, 'R':0.1, '#':0.0}}
B = {'N':{'time':0.98, 'flies':0.015, 'quickly':0.005, '#':0.0}, 'V':{'time':0.33, 'flies':0.64, 'quickly':0.03, '#':0.0}, 'R':{'time':0.01, 'flies':0.01, 'quickly':0.98, '#':0.0}, '#':{'time':0.0, 'flies':0.0, 'quickly':0.0, '#':1.0}}
# Define a new emission matrix B2 for Question 4
#B2 = ???
# two data structures you may find useful for mapping between tags and their (arbitrary) indices
tagnum = {"N":0,"V":1,"R":2,"#":3}    #gives index for a given tag
numtag = ['N','V','R','#']   #gives tag for a given index
        
def print_table(table, words, ef='%.4f', colwidth=12):
    tags = A.keys()
    print ''.ljust(colwidth),
    for w in words:
        print str(w).ljust(colwidth),
    print
    for n in range(len(A.keys())):
        print str(numtag[n]).ljust(colwidth),
        for t in range(len(words)):
            out = str(table[t][n])
            if type(table[t][n]) == tuple: 
                form=ef+",%s"
                out = form % (table[t][n][0], table[t][n][1])
            elif type(table[t][n]) == float:
                out = str(ef % table[t][n])
            print out.ljust(colwidth),
        print

#def forward(ws, A, B):
    ## PART 1 YOUR FORWARD CODE GOES HERE

#def viterbi(ws, A, B):
    ## PART 2 YOUR VITERBI CODE GOES HERE

### MAIN CODE GOES HERE ###
seq = ('time','flies','quickly')
#print "calculating forward probability of", seq, ":\n", forward(seq, A, B)
#print "calculating most likely tags for", seq, ":\n", viterbi(seq, A, B)
seq = ('swat','flies','quickly')
#print "calculating most likely tags for", seq, ":\n", viterbi(seq, A, B2)