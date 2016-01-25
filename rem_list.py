def remove_elements(lst):
    mi=min(lst)
    ma=max(lst)
    nl=[]
    for v in lst:
        if v != 3 and v != mi and v != ma:
            nl.append(v)
    return nl