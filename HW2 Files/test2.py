import sys

def ins_cost(c):
    return 1

def del_cost(c):
    return 1

def sub_cost(c, d):
    if c == d: return 0
    else: return 2

source = sys.argv[1]
target = sys.argv[2]
n = len(source)
m = len(target)
d = [[0]*(m+1) for i in range(n+1)]
d[0][0] = 0
for i in range(1, n+1):
	d[i][0] = d[i-1][0] + del_cost(source[i-1])
for j in range(1, m+1):
	d[0][j] = d[0][j-1] + ins_cost(target[j-1])

for i in range(1, n+1):
	for j in range(1, m+1):
		d[i][j] = min(	d[i-1][j] 	+ del_cost(source[i-1]),
						d[i][j-1] 	+ ins_cost(target[j-1]),
						d[i-1][j-1]	+ sub_cost(source[i-1], target[j-1]))


for x in reversed(d):
	print x
print "Total cost:",d[n][m]