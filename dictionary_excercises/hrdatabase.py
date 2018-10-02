def HRDatabase():
    hr={}
    name=[]
    number=[]
    data=[]
    print("Enter Employee number and name. Type END when done\n")
    while True:
        line=input()
        if line=='END':
            break
        data=line.split(None,1)
        number=data[0]
        name=data[1]
        hr[number]=name
    print("Dictionary sorted by number: \n")
    for k in sorted(hr.keys()):
        print (k, hr[k])
    print("\nDictionary sorted by values: \n")
    for v in sorted(hr.values()):
        for k in hr.keys():
            if hr[k]==v:
                print(k, hr[k])