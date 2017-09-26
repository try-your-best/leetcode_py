# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# Time:  O(n)
# Space: O(n)

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		lookUp = {}
		for idx, num in enumerate(nums):
			diff = target - num
			if diff in lookUp:
				return [lookUp[diff], idx]
			else:
				lookUp[num] = idx

		return []

if __name__ == "__main__":
	nums = [2, 7, 11, 15]
	print Solution().twoSum(nums, 9)
	print Solution().twoSum(nums, 17)
	print Solution().twoSum(nums, 20)