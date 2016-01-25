def remove_adjacent(nums):
	nl=[nums[0]]
	for i in nums:
		if i!= nl[-1]:
			nl.append(i)
	return nl
		