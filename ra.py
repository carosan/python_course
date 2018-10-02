#Given a list of numbers, return a list where all adjacent
#equal elements have been reduced to a single element, so
#[1, 2, 2, 3,2,3] returns [1, 2, 3,2,3]. You may create a
#new list or modify the passed in list.

def remove_adjacent(nums):
	nl=[nums[0]]
	for i in nums:
		if i!= nl[-1]:
			nl.append(i)
	return nl
		