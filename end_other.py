def end_other(s1,s2):
	s1l = s1.lower()
	s2l = s2.lower()
	
	if s1l.endswith(s2l) or s2l.endswith(s1l):
		return True
	return False
		