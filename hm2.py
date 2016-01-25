def match_ends(words):
	count = 0
	for list in words:
		if len(list) >= 2 and list[0] == list[-1]:
			count += 1
	return count