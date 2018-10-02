def has_duplicates(l):
    for v in l:
        if l.count(v)>1:
            return True
    return False