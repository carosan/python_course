def sort_print(d):
    print("Sorted by keys:")
    for n in sorted(d.keys()):
        print(n, d[n])
    print("Sorted by values: ")
    for n in sorted(d.values()):
        for k in d.keys():
            if d[k]==n:
                print(k, d[k])