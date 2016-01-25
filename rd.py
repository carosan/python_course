def remove_duplicates(nums):
    nl=[]
    for v in nums:
        if v not in nl:
            nl.append(v)
    return nl