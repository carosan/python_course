def tim24hr(t):
	if t[-2:]=='am':
		return ('00'+ t.split(':')[1].replace('am','hr') if t.split(':')[0]== '12' else t.split(':')[0] + t.split(':')[1].replace('am','hr'))
	elif t[-2:] == 'pm':
		return (str(12+int(t.split(':')[0])) + t.split(':')[1].replace('pm','hr') if int(t.split(':')[0]) < 12 else '12' + t.split(':')[1].replace('pm','hr'))