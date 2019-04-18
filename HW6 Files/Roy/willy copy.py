import sys
import math
import random
from collections import defaultdict
from nltk.tree import Tree
import time
import re

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
    #for k,v in rules.items():
    #    print k,v
    return rules

def parseSentence(sen):
    words = sen.split()
    return words

def initializeTable(L, grammar, words):
    T = []
    for j in range(L):
        T.append([])
        for i in range(L):
            T[j].append([])
    return T

def diagonal(T, L, grammar, words):
    for j in range(L):
        for i in range(L):
            if i == j:
                for g in grammar[words[j]]:
                    node = (g[0],g[1],words[j])
                    T[i][j].append(node)
    return T

def fillIn(T, L, grammar, words):
    for j in range(L):
        for i in range(j-1, -1, -1):
            WT = []
            for k in range(i, j):
                for litem in T[i][k]:
                    for ditem in T[k+1][j]:
                        r =  (litem[1],ditem[1])   
                        if r in grammar:
                            for g in grammar[r]:
                                node = (g[0],g[1],litem,k,ditem,k+1)
                                T[i][j].append(node)
    return T

def bracket(tree, bracketed):
    if len(tree) > 3:
        bracketed += "(" + str(tree[1]) + " "
        bracketed = bracket(tree[2], bracketed)[1]
        bracketed = bracket(tree[4], bracketed)[1]
        bracketed += ")"
    else:
        bracketed += "(" + str(tree[1]) +" " + str(tree[2]) + ")"
    return tree, bracketed

def wcalc(tree, weight):
    if len(tree) > 3:
        weight += tree[0]
        weight = wcalc(tree[2],weight)[1]
        weight = wcalc(tree[4],weight)[1]
    else:
        weight += tree[0]
    return tree, weight

def main():
    gr =                    sys.argv[1]
    senfile =               sys.argv[2]
    grammar =               readGrammar(gr)
    sentences =             open(senfile, "r")
    outfilename =           re.sub("\.sen",".out",sys.argv[2])
    outfile =               open(outfilename,'w')
    rank =                  0
    for sen in sentences:
        rank +=             1
        words =             parseSentence(sen)
        L =                 len(words)
        T =                 initializeTable(L, grammar, words)
        T =                 diagonal(T,L,grammar,words)
        T =                 fillIn(T,L,grammar,words)
        print >>outfile, rank,"\n","PARSING::\t\t",
        print rank,"\n","PARSING::\t\t",
        for w in words:
            print w,
            print >>outfile, w,
        print "\n",
        print >>outfile, '\n'
        for t in T[0][L-1]:
            if t[1] == 'ROOT': 
                weight = 0.0
                weight = wcalc(t, weight)[1]
                print "Tree",T[0][L-1].index(t)+1, "weight:",weight
                print >>outfile, "Tree",T[0][L-1].index(t)+1, "weight:",weight
                print "Tree",T[0][L-1].index(t)+1, "parse:"
                print >>outfile, "Tree",T[0][L-1].index(t)+1, "parse:"
                bracketed = ''
                bracketed = bracket(t, bracketed)[1]
                print bracketed
                print >>outfile, bracketed
                print '\n'
                print >>outfile, '\n'
                t = Tree.fromstring(bracketed)
                t.draw()
            else:
                print "No parse!\n"
                print >>outfile, "No parse!\n"



if __name__ == "__main__":
    main()