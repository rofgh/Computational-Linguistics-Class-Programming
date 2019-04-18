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

'''
readGrammarFile(fn)
is given:
            fn:     the grammar text file
returns:
            rules:  rules[LHS] will produce a list of the RHS, so rules is a dictionary...
                with lhs nonterminals/preterminals as keys and rhs pre-, non- and terminals as values 
'''
def readGrammarFile(fn):

    f = open(fn, "r")
    rules = defaultdict(lambda:[])

    for line in f:
        line = line.split('#')[0].strip()  # strip out comments and whitespace
        if line == '': continue
        fields = line.split()
        weight = str(fields[0])
        lhs = fields[1]
        try:
            rhs = (fields[2], fields[3])        # a list of RHS symbols
        except:
            rhs = (fields[2])
        rules[rhs].extend( [lhs] )  # adds a list of the list of RHS symbols
    for x in rules.items():
        print x
    return rules
'''

genNonTerminal(fn) is a recursive (i.e. it calls itself) program that produces our sentences through picking
            some rhs values for each lhs key until all the symbols being fed into the function are terminals
is given:
            nonterm: something to which the rules are applied (Starts as 'ROOT', and then within
            this function it is whatever nonterminals are produced in the tree)
            rules:  rules is a dictionary...
                with lhs nonterminals/preterminals as keys and rhs pre-, non- and terminals as values
returns:    
            result:  if all symbols are terminal this is the finished sentence, otherwise it is

def genNonTerminal(nonterm, rules):

    # grab a random RHS for this nonterminal from the grammar
    numrules = len(rules[nonterm])
    # randrange will produce from 0-numrules, exclusive.
    rule = rules[nonterm][ random.randrange(0,numrules) ]

    result = ""

    # go through each symbol in the chosen RHS
    for symbol in rule:
        if not symbol in rules:
            # this is a terminal symbol so write it out
            result += symbol + " "
        else:
            # this is a non-terminal symbol so recurse!
            if T == True:
                result += "( " + symbol + " "
            result += genNonTerminal(symbol, rules)
            if T == True:
                result += ")"

    return result

T = False   # Should trees be drawn?

# If insufficient arguments are provided
if len(sys.argv) < 2:
    print "Usage: python randsent.py <grammar-file> [number-of-sentences]"
    exit(0)
'''
def tagTheWord():
    exit()

def parseTheSentence(line):
    words = line.split()
    print line, words, '\n'
    L = len(words)
    for x in range(L):
        for rhs in grammar:
            for lhs in range(len(grammar[rhs])):
                for w in grammar[rhs][lhs]:
                    if w == words[x]:
                        print grammar[rhs][lhs]
                

# create a grammar from the grammar file
gr = sys.argv[1]
grammar = readGrammarFile(gr)

# 
sent = sys.argv[2]
sentences = open(sent, "r")
print
for line in sentences:
    sentence = parseTheSentence(line)

'''
# Main code
file = sys.argv[1]
if len(sys.argv) >= 3:
    # produce trees or not?
    if sys.argv[1] == '-t': 
        # if trees, argument 2 is the grammar
        file = sys.argv[2]
        # Trees are a go
        T =True
        # Which argument is the number of sentences to produce
        if len(sys.argv) >= 4: n = int(sys.argv[3])
        else: n = 1
    else: n = int(sys.argv[2])
# If no # of sentences was provided, just print 1
else:
    n = 1

# Turns grammar.txt into a dictionary of rules
grammar = readGrammarFile(file)
#print grammar
print
# for whatever number of sentences was asked for
for i in range(n):
    # if trees were asked for, use nltk to produce trees, and also print bracketed string sentences
    if T: 
        bracketed = "( ROOT " + genNonTerminal("ROOT", grammar) + ")"
        print bracketed
        t = Tree.fromstring(bracketed)
        t.draw()
    # if trees were not asked for, print a generated sentence
    else: 
        print genNonTerminal("ROOT", grammar)
        print
'''
