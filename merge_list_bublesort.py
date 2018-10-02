#given 2 lists, return one sorted list

lst1 = [1,2,6]
lst2 = [0,3,4]

def linear_merge(list1, list2):
    nl = lst1 + lst2
    #a loop that iterates from the end of the list to the beginning
    for i in range(len(nl)-1, 0, -1):
        #a loop that compares
        for j in range(i):
            if nl[j] > nl[j+1]:
                tmp = nl[j]
                nl[j] = nl[j+1]
                nl[j+1] = tmp
    return(nl)

print(linear_merge(lst1, lst2))