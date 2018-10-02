def invertDic(d):
	nd={}
	for val in d.values():
		nd[val]=[] #create an empty list with the values
	for key in d.keys():
		nd[d[key]].append(key)#append the key in d as a value in nd
	return nd