# given a list of elements, return a dictionary with the number of times each element repeats in the list

lst = [4,3,6,1,0,4,1,1,6,0,5]

def count_num(lst):
    dv = {}
    for i in lst:
        if i not in dv.keys():
            dv[i] = 1
        else:
            dv[i] +=1
    return dv

print(count_num(lst))
       
		
		