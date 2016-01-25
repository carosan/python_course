def reverse_list(l):
	nl=[]
	for c in range (0, len(l)):
		nl.append(l[len(l)-c-1])
	return nl