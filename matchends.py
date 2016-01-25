def match_ends(ls):
	c=0
	for s in ls:
		if len(s)>=2 and s[0]==s[-1]:
			c+=1
	return c