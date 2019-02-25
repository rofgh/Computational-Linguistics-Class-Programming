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
# dist is a list of lists, (n+1)*(m+1)
dist = [[0]*(m+1) for i in range(n+1)]
dist[0][0] = 0
for i in range(1, n):
	dist[i][0] = dist[i-1][0]+del_cost(source[i])
for j in range(1, m):
	dist[0][j] = dist[0][j-1]+ins_cost(target[j])

for i in range(1, n):
	for j in range(1, m):
		dist[i][j] = min(dist[i-1][j] + del_cost(source[i]),
			 			dist[i][j-1] + ins_cost(target[j]),
			 			dist[i-1][j-1] + sub_cost(source[i], target[j]))

for x in reversed(dist):
	print x
print "Total cost:",dist[n][m]

