def both_ends(s):
    if s==" ":
        ns="invalid input string"
    else:
        if len(s)<2:
            ns=""
        elif len(s)>=2:
            ns=s[:2]+s[-2:]
    return ns