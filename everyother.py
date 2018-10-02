def every_other(s):
    ns=''
    c=len(s)-1
    while(c>=0):
        ns=ns+s[c]
        c=c-2
    return ns