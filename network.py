
'''
on CL:  python network.py originuser destinationuser
        python network.py William Ren 
'''
import sys
from collections import defaultdict

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],}

def genRecipList(sender, recipient):
    path = []
    for x in network:
        if recipient == x:
            
            for r in network[x]:
                if r == sender:
                    path.insert(0, r)
                    break
            for r in network[x]:
                genRecipList(, )
    return path




sender =        sys.argv[1]
recipient =     sys.argv[2]
print genRecipList(sender, recipient)



