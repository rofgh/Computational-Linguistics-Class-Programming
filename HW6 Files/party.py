import sys
import math
import random
from collections import defaultdict
from nltk.tree import Tree
import time

class Node(object):
    def __init__(self, name='', x=0, y=0, pos=[], weight=[], L=[], R=[]):
        self.name =     name
        self.x =        x
        self.y =        y
        self.pos =      pos 
        self.weight =   weight
        self.L =        L
        self.R =        R

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

def diagonal(table, L, grammar):
    for j in range(L):
        tags =      [tag[1] for tag in grammar[words[j]]]
        w =         [tag[0] for tag in grammar[words[j]]]      
        k = str(j)+str(j)
        k = Node(x=j,y=j,pos=tags,weight=w)
        table[j][j] =   [pre for pre in k.pos]
        print k.pos,k
    return table

def fillIn(table, L, grammar):
    return table

def initializeTable(L, gr):
    table = []
    for i in range(L):
        table.append([])    
        for j in range(L):
            table[i].append([])
    table = diagonal(table, L, readGrammar(gr))
    table = fillIn(table, L, readGrammar(gr))
    return table 

gr = sys.argv[1]
sentfile = sys.argv[2]
sentences = open(sentfile, "r")
for sen in sentences:
    words =             parseSentence(sen)
    print words
    grammar =           readGrammar(gr)
    L =                 len(words)
    table =             initializeTable(L, gr)
    '''
    for i in range(L):
        l = str(i)
        for j in range(L):
            poss = []
            k = str(j)
            h = l+k
            word = str(words[i]+'->'+words[j])
            tags = [tag for tag in grammar[words[j]]]
            # print words[j], tags
            p =   [pre for pre in tags]
            h = Node(name=word, x=l, y=k, pos=p)
            #print h.name,h.x,h.y,h.pos
    '''
    for i in table:
        print i
    for x in range(1):
        f = str(x)+str(x)
        print f.pos

