f = open("mini_train.txt", mode = "r+")
for i in f.readlines():
	x = i.split()
	y = x.pop(0)
	for z in x:
		print z,
	print

