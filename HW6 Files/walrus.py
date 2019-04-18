import sys
import math
import random
from collections import defaultdict
from nltk.tree import Tree
import time

class Node(object):
    names = []
    def __init__(self, name='', x=0, y=0, tags=[], weights=[], L=[], D=[]):
        self.name =     name
        self.x =        x
        self.y =        y
        self.tags =     tags 
        self.weights =  weights
        self.L =        L
        self.D =        D
        Node.names.append((self))

    def addLP(self, x, y):
        pass

def parseSentence(sen):
    words = sen.split()
    return words

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

def initializeTable(L, grammar, words):
    T = []
    for j in range(L):
        T.append([])
        for i in range(L):
            T[j].append([])
    return T

def pullTup(grammar, words, i, j):
    tags =          []
    weights =       []
    rule =          [r for r in grammar[words[j]]]
    for w, t in rule:
                    tags.append(t)
                    weights.append(w)
    return weights, tags

def pullDTup(grammar, tup, i, j):
    tags =          []
    weights =       []
    rule =          [r for r in grammar[tup]]
    for w, t in rule:
                    tags.append(t)
                    weights.append(w)
    return weights, tags

    
def diagonal(T, L, grammar, words):
    for j in range(L):
        for i in range(L):
            if i == j:
                name = str(i)+str(j)
                #print name
                T[i][j] =       Node(x=j,y=i,name=name,tags=pullTup(grammar, words, i, j)[1],weights=pullTup(grammar, words, i, j)[0])
            '''
            if x == y:
                name =          words[x]
                rule =          [r for r in grammar[name]]
                tags =          []
                weights =       []
                for w, t in rule:
                    tags.append(t)
                    weights.append(w)
                T.append(Node(x=x, y=y, name=name, tags=tags, weights=weights))
            '''
    return T

def diag(T,L,grammar,words,i,j):
    pass

def fillIn(T, L, grammar, words):
    for j in range(L):
        for i in range(j-1, -1, -1):
            if i != j:
                weights =   []
                tags =      []
                lpointers = []
                dpointers = []
                D = []
                L = []
                for k in range(i, j):
                    WT =    []
                    P =     []
                    #print i,j,k
                    # LOOK LEFT!
                    for d in Node.names:
                        if d.x == k and d.y == i:
                            if d.tags != []:
                                ltags = d.tags
                                lpointers.append(d)
                            #print "ltags:",d.x,d.y,ltags
                    # LOOK DOWN!
                    for d in Node.names:
                        if d.x == j and d.y == k+1:
                            if d.tags != []:
                                dtags = d.tags
                                dpointers.append(d)
                            #print "dtags:",d.x,d.y,dtags
                    Tups = []
                    for ltag in ltags:
                        for dtag in dtags:
                            Tups.append((str(ltag),str(dtag)))
                    for Tup in Tups:
                        #print "Tup:",Tup
                        if Tup in grammar:
                            WT = [r for r in grammar[Tup]]
                            i = Tups.index(Tup)
                            D.append(dpointers[i])
                            L.append(lpointers[i])

                    for w,t in WT:
                        weights.append(w)
                        tags.append(t)
                #if weights != []:
                    #print "W,T,LP:",weights,tags,lpointers,dpointers
                name = str(i)+str(j)
                T[i][j] = Node(x=j,y=i,name=name,tags=tags,weights=weights,L=L,D=D)

            
    return T

def bracketIt(T, L, grammar, words):

    n = T[0][L-1]
    print n,len(n.L)
    print n.L,n.D
    bracket = ''
    for root in range(len(n.tags)):
        bracket = '(' + n.tags[root] + "(" + bracket(T, n.L) + bracket(T, n.D) + ")" +  ")" 
        print bracket

def bracket(T, n):
    if n.L and n.D:
        bracketed += "(" + bracket(T,n.L) + bracket(T, n.D) +")"
    return bracketed

    '''
    T[L-1][L-1]
    bracketed = "( ROOT " + genNonTerminal("ROOT", grammar) + ")"
    print bracketed
    t = Tree.fromstring(bracketed)
    t.draw()
    return bracketedsentence
    '''

def main():
    objectlist = []
    gr =                    sys.argv[1]
    sentfile =              sys.argv[2]
    sentences =             open(sentfile, "r")
    for sen in sentences:
        words =             parseSentence(sen)
        print words
        grammar =           readGrammar(gr)
        L =                 len(words)
        T =                 initializeTable(L, grammar, words)
        T =                 diagonal(T, L, grammar, words)
        T =                 fillIn(T, L, grammar, words)
        #for i in T:
        #    print i
        #for n in Node.names:
        #    if n.L != []:
        #        print n.x,n.y,n.tags,n.L,n.D
        bracketIt(T, L, grammar, words)


        #i.name,i.x,i.y,"T:",[t for t in i.tags],"W:",[i for i in i.weights]

if __name__ == "__main__":
    main()