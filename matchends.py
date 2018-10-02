#Given a list of lists, return the number of lists which length is equal or higher than 2
# and the first and last elements of the sublist are the same
# example list ls = [[1],[1,2],[4,2,4],[3,3,3],[1,6,6,4],[1,1]]

def match_ends(ls):
	c=0
	for s in ls:
		if len(s)>=2 and s[0]==s[-1]:
			c+=1
	return c