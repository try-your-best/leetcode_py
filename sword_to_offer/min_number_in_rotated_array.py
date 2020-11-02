# -*- coding: utf-8 -*-

"""
剑指offer 第8题
"""


def minInRotatedArray(nums):
	if not nums:
		return None

	left, right = 0, len(nums)-1
	mid = left
	while nums[left] >= nums[right]:
		if right - left == 1:
			mid = right
			break

		mid = (left+right)/2

		if nums[mid] == nums[left] and nums[mid] == nums[right]:
			return min(nums[left: right+1])
		elif nums[mid] >= nums[left]:
			left = mid
		else:
			right = mid

	return nums[mid]


if __name__ == '__main__':
	print minInRotatedArray([3, 4, 5, 1, 3])
	print minInRotatedArray([1])
	print minInRotatedArray([1, 2, 3])
	print minInRotatedArray([1, 0, 1, 1])

	import sys
	print sys.getsizeof(1)
	print sys.getsizeof(1L)

	print 0b10