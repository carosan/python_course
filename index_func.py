#Write a function that accepts a list and its elements as input
#and returns the position at which that elements appears in the list. 
# This is the index function in Python. If the element is not in the list return -1

def index_fun(lst, num):
	if num not in lst:
		return -1
	else:
		for i in range(len(lst)):
			if lst[i] = num:
				pos = i
		return pos