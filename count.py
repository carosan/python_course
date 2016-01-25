def count_elements(lst):
	nl=[]
	for v in lst:
		if v not in nl:
			print(v, " appears ", lst.count(v), " times")
			nl.append(v)
		
		