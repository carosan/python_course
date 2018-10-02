def reverselookup(d,v):
	l=[]
	for key in d:
		if d[key]==v:
			l.append(key)
	l.sort()
	return l