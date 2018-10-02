def Dice():
	d = {}
	for i in range(2,13):
		d[i]=[]
	for i in range(1,7):
		for j in range(1,7):
			d[i+j].append((i,j))
	for keys,values in d.items():
			print(keys)
			print(values)