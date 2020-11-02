# -*- coding: utf-8 -*-

"""
24题
"""


def verifySequenceOfBst(nums):
	return verifySequenceOfBstCore(nums, 0, len(nums)-1)


def verifySequenceOfBstCore(nums, low, high):
	if not nums:
		return False

	root = nums[high]
	i = low

	while i < high and nums[i] < root:
		i += 1

	j = i
	while j < high:
		if nums[j] < root:
			return False
		j += 1

	if i - low > 0:
		if not verifySequenceOfBstCore(nums, low, i-1):
			return False

	if high - i > 0:
		if not verifySequenceOfBstCore(nums, i, high-1):
			return False

	return True


if __name__ == "__main__":
	print verifySequenceOfBst([5, 7, 6, 9, 11, 10, 8])
	print verifySequenceOfBst([7, 4, 6, 5])