# -*- coding: utf-8 -*-
__author__ = 'DamonHao'
"""
Given an arrays of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Time:  O(n)
# Space: O(n)
from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""注意，nums 是无序的"""
		look_up = {}
		for index, value in enumerate(nums):
			diff = target - value
			if diff in look_up:
				return [look_up[diff], index]
			else:
				look_up[value] = index

		return []


if __name__ == "__main__":
	s = Solution()
	nums = [2, 11, 7, 15]
	print(s.twoSum(nums, 9))
	print(s.twoSum(nums, 17))
	print(s.twoSum(nums, 20))