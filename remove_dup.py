# Given a list, remove the duplicated elements of the list and return a new list
# Example nums = [1,4,2,2,3,1,2,3,10,7], return [1,4,3,10,7]

def remove_duplicates(nums):
    nl=[]
    for v in nums:
        if v not in nl:
            nl.append(v)
    return nl