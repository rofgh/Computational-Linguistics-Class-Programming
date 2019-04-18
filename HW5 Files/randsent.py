'''
On the CL:      
                -t as sys.argv[1] will draw trees, without it will just create sentences
                grammar.txt is the grammar to use  (either grammar.txt or grammar1.txt)
                sys.argv[2]/[3] is the number of sentences to create 

                "python randsent.py grammar.txt 5"  With just sentence creation
                OR
                "python randsent.py -t grammar1.txt 5"  With trees drawn
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
        prob = int(fields[0])
        lhs = fields[1]
        rhs = fields[2:]            # a list of RHS symbols
        rules[lhs].extend( [rhs]*prob )  # adds a list of the list of RHS symbols

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

'''
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

if len(sys.argv) < 2:
    print "Usage: python randsent.py <grammar-file> [number-of-sentences]"
    exit(0)

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
else:
    n = 1

# Turns grammar.txt into a dictionary of rules
grammar = readGrammarFile(file)
#print grammar
print
for i in range(n):
    if T: 
        bracketed = "( ROOT " + genNonTerminal("ROOT", grammar) + ")"
        print bracketed
        t = Tree.fromstring(bracketed)
        t.draw()
    else: 
        print genNonTerminal("ROOT", grammar)
        print

