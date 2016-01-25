def split(s, sep):
  
  l = []
  temp_str = s
  while temp_str.find(sep) != -1:
    l.append(temp_str[0:temp_str.find(sep)])
    temp_str = temp_str[temp_str.find(sep) + len(sep):]
  l.append(temp_str)
  return l