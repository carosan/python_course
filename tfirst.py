def front_3(lst):
	nl=[]
	for v in lst:
		if v==3:
			nl.append(v)
			lst.remove(v)
	lo = lst.sort()
    nl= nl + lo
	return nl
	