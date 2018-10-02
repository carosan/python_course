#Given a list of numbers, return a list with
#the list in sorted order, except group all
#the elements whose value is 3 at the
#beginning. lst = [3,8,44,2,1,3,2]

def front_3(lst):
	nl = []
	ol = []
	for v in lst:
    	if v == 3:
        	nl.append(v)
        	lst.remove(v)
	ol = sorted(lst)
	nl =nl + ol
	return nl