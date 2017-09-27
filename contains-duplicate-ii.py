# -*- coding: utf-8 -*-

__author__ = 'DamonHao'

"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Time:  O(n)
# Space: O(n)
"""


class Solution(object):

	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		lookup = {}
		for idx, num in enumerate(nums):
			if num not in lookup:
				lookup[num] = idx
			else:
				if idx - lookup[num] <= k:
					return True
				lookup[num] = idx

		return False

if __name__ == "__main__":
	print Solution().containsNearbyDuplicate([1, 1, 2], 1)
	print Solution().containsNearbyDuplicate([1, 2, 1], 1)
