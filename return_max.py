
#returns the max element in a list
def return_max(lst):
	ma = lst[0]
	for i in range(len(lst)-1):
		if lst[i] > ma:
			ma = lst[i]
	return ma