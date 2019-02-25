import sys
import re

# this regexp will match any vowel symbol
V = r"[0123456789$@EI{VQUiu#cq]"

def ins_cost(c):
    return 1

def del_cost(c):
    return 1

def sub_cost(c, d, tLastLetter, sLastLetter, tPenultLetter, sPenultLetter, tLen, sLen):
    if c == d:
        if tLastLetter == c and sLastLetter == d:
            if tPenultLetter == sPenultLetter:
                if tLen == sLen: return -3
                else: return -1.5
            else: return -1
        else: return 0
    else: return 2

def min_edit(source='', target='', verbose=False):
    sLen = len(source)
    tLen = len(target)
    dist = [[0]*(sLen+1) for i in range(tLen+1)]
    if len(source) == 1:
        sPenultLetter = "k"
    else:
        sPenultLetter = source[-2]
    if len(target) == 1:
        tPenultLetter = "l"
    else:
        tPenultLetter = target[-2]

    
    ## PART 1 - fill in the values of dist using the min_edit algorithm here##
    for i in range(1, tLen+1):
        dist[i][0] = dist[i-1][0] + del_cost(target[i-1])
    for j in range(1, sLen+1):
        dist[0][j] = dist[0][j-1] + ins_cost(source[j-1])
    
    
    for i in range(1, tLen+1):
        for j in range(1, sLen+1):
            dist[i][j] = min(   dist[i-1][j]   + del_cost(target[i-1]),
                                dist[i][j-1]   + ins_cost(source[j-1]),
                                dist[i-1][j-1] + sub_cost(target[i-1], source[j-1], target[-1], source[-1], tPenultLetter, sPenultLetter, tLen, sLen))
    ## if verbose is set to True, will print out the min_edit table
    if verbose:
        #print the matrix
        for j in range(sLen+1)[::-1]:
            if j > 0: print source[j-1],
            else: print '#',
            for i in range(tLen+1):
                print '\t' + str(dist[i][j]),
            print
        print '#\t#\t' + '\t'.join(list(target)) + '\n'
        
    
    # returns the cost for the full transformation
    return dist[tLen][sLen]
    
def main():
    s = sys.argv[1]
    t = sys.argv[2]
    print min_edit(source=s, target=t,verbose=True)

if __name__ == "__main__":
    main()