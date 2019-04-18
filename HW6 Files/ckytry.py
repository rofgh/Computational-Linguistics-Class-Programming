'''
Script cky.py on the command line:      
                python cky.py GRAMMAR_FILE SENTENCE_FILE
                python cky.py english_cnf.gr sentences.sen
                python cky.py cky_grammar.gr mary.sen
cky.py returns:
        a .out file named after the sentence file given:
            this .out file will contain:
                For sentence in .sen file:
                    "Parsing:  sentence"
                    if parse:
                        for parse in parses:
                        "Tree 1 weight: xxx
                         Tree 1 parse in bracketed form:(()(()))()"
'''
import sys
import math
import random
from collections import defaultdict
from nltk.tree import Tree
import time
'''
'''
class Node(object):
    def __init__(self, xpos=0, ypos=0, NT=[], weight=0.0, L='', R=''):
        self.xpos =     xpos
        self.ypos =     ypos
        self.NT =       NT
        self.weight =   weight
        self.L =        L
        self.R =        R

def readGrammar(fn):
    f = open(fn, "r")
    rules = defaultdict(lambda:[])
    for line in f:
        line = line.split('#')[0].strip()  # strip out comments and whitespace
        if line == '': continue
        fields = line.split()
        weight = float(fields[0])
        lhs = fields[1]
        tup = (weight, lhs)
        try:
            rhs = (fields[2], fields[3])
        except:
            rhs = (fields[2])
        rules[rhs].extend([tup])
    f.close()
    return rules
'''
parseSentence
is given:
    sen
    grammar
returns:
    parsestrings?
'''
def parseSentence(sen, grammar):
    words = sen.split()
    L = len(words)
    weight = float(0)
    #for word in words:
        # print word
        # Only looks at whether the word is in the grammar, has a preterminal, and adds that to weight
        #for lhs in range(len(grammar[word])):
            #print grammar[word][lhs]
            #print grammar[word][lhs][0]
            #weight += grammar[word][lhs][0]
    #print weight
    return words

def ckyDiagonal(words, L, grammar):
    table =             []
    for l in range(L):
        table.append([])
    for l in range(L):
        for l in range(L):
            table[l].append([])
    backpointers =      []
    for l in range(L):
        backpointers.append([])
    for i in range(L):
        for j in range(L):
            backpointers[l].append([Node(xpos=i, ypos=j)])
    for j in range(L):
        tags = [tag for tag in grammar[words[j]]]
        # print words[j], tags
        table[j][j] =   [pre for pre in tags]

    for t in backpointers:
        print t
    return table, backpointers

def ckyFillIn(table, backpointers, words, L, grammar):
    '''
    for t in table:
        print t
    for j in range(L):
        print "J:", j
        for i in range(j):
            print "\tI:", i
            for k in range(j):
                if not k < i:
                    print "\t\tK:", k
                    y = []
                    x = []  
                    try:
                        print "(",i,",",j,")","(",i,",",k,")","(",k+1,",",j,")"
                        for term in table[i][k]:
                            y += [term[1]]
                            print y
                        for mert in table[k+1][j]:
                            x += [mert[1]]
                            print x
                    except:
                        print "exception"
                for yterm in y:
                    for xterm in x:
                        print yterm, xterm, grammar[(yterm,xterm)]
                        try:
                            table[i][j] += grammar[(yterm,xterm)]
                            print "Grammar for",i,j, grammar[(yterm, xterm)]
                        except:
                            print "exceptionx"
    '''
    for j in range(1, L):
        # print "J:",j
        for i in range(j-1, -1, -1):
            # print "\tI:",i
            ij = Node(xpos = i, ypos = j)
            #table[i][j]
            for k in range(i, j):
                # print "\t\tK:",k
                left = ['x']
                down = ['x']
                for term in table[i][k]:
                    if term:
                        # print term
                        left.append(term[1])
                        # print "left:",left
                for term in table[k+1][j]:
                    if term:
                        # print term
                        down.append(term[1])
                        # print "down:",down
                for l in left:
                    # print "l:",l
                    for d in down:
                        # print "d:",d
                        if grammar[(l,d)]:

                            for item in grammar[(l,d)]:
                                    # print "(",i,",",j,")"
                                    # print "G:",item
                                    # for t in table:
                                    #    print t
                                    ij.NT.append(item)
                                    backpointers[i][j].append(item[1])
                                    # for t in table:
                                    #    print t
                                    # print "table",i,j,table[i][j]
                left = []
                down = []




    return table, backpointers

def cky(words, grammar):
    L = len(words)
    table, backpointers = ckyFillIn(ckyDiagonal(words, L, grammar)[0], ckyDiagonal(words, L, grammar)[1], words, L, grammar)
    print words
    for i in table[0]:
        print i
    for i in backpointers:
        print i
    '''
    print words
    for t in table:
        print t
    '''
    # return ????


def bracket():
    bracketed = "( ROOT " + ("ROOT", grammar) + ")"
    
    return bracketed

def tree(bracketed):
    t = Tree.fromstring(bracketed)
    t.draw()



'''
saveOutput puts the trees into an output file
saveOutput is given:
    a parse?
    a filename?
saveOutput returns:
    nothing, it just updates the output file
'''
def saveOutput(parsestrings,senfilename):
    #The output file name will be the argument filename plus _out before the .txt
    outfilename = re.sub("\.txt$","_out.txt",senfilename)
    outfile = open(outfilename,'w')
    output = "Sentence to parse:\t" "%d:\t%-13.6f\t%s\t\t%f\t%f\n" % (rank,count,word,math.log(count),math.log(rank))
    outfile.write(output)
'''
    print "Printing Histogram for", filename, "to", outfilename
    #I put this in in order to print out the ranks of the words printed to the file
    rank = 0
    #for each word it will print the rank, the count (normalized), the word, the log of the count
    #and the log of the rank
    for word, count in sorted(hist.items(), key = lambda pair: pair[1], reverse = True):
        rank+=1
        output = "%d:\t%-13.6f\t%s\t\t%f\t%f\n" % (rank,count,word,math.log(count),math.log(rank))
        outfile.write(output)
'''
'''
MAIN CODE:  Interpret the grammar, parse the sentences, output the parse
main is given:
    nothing
main returns:
    nothing
'''
def main():
    # create a grammar from the grammar file
    gr = sys.argv[1]
    #grammar = readGrammar(gr)

    # parse the sentences
    sentfile = sys.argv[2]
    sentences = open(sentfile, "r")

    for line in sentences:
        cky(parseSentence(line, readGrammar(gr)), readGrammar(gr))

if __name__ == "__main__":
    main()



'''
Print to .out file:
tree weight
tree brackets
'''


