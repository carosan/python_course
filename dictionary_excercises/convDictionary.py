def convertDic(d):
	vector=[]
	for i in range(max(d)+1):
		if i in d:
			vector.append(d[i])
		else:
			vector.append(0)
	return vector