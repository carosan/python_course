#Implement the min function to find the lowest element in a list


lst = [4,3,6,3,4,2,3,6,5]

def return_min(lst):
    mi = lst[0]
    for i in range(len(lst)-1):
        if lst[i] < mi:
            mi=lst[i]
    return mi
    
print(return_min(lst))
	