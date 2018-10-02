#Write a function that takes in a list of numbers, and

#(a) Removes from the list the maximum value of all the elements

#(b) Removes from the list the minimum value of all the elements

#(c) Removes all occurrences of the number 3 from the list

#Return the remaining list after removing all the above
#elements.

#For example, if the input list is [1,3,5,6,2,3,5,6,8,8], the
#output list should be [5,6,2,5,6].

def remove_elements(lst):
    mi=min(lst)
    ma=max(lst)
    nl=[]
    for v in lst:
        if v != 3 and v != mi and v != ma:
            nl.append(v)
    return nl