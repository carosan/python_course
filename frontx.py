def front_x(words):
	n=[]
	xwords=0
	words.sort()
	for w in words:
		if w[0]=="x":
			n.insert(xwords,w)
			xwords+=1
		else:
			n.append(w)
	return n
	