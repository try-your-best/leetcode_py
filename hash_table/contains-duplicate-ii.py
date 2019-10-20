# -*- coding: utf-8 -*-

__author__ = 'DamonHao'

"""
Given an arrays of integers and an integer k,
find out whether there are two distinct indices i and j in the arrays such that
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
			if num in lookup:
				if idx - lookup[num] <= k:
					return True

			lookup[num] = idx

		return False

if __name__ == "__main__":
	sl = Solution()
	print sl.containsNearbyDuplicate([1,2,3,1], 3)
	print sl.containsNearbyDuplicate([1,0,1,1], 1)
	print sl.containsNearbyDuplicate([1,2,3,1,2,3], 2)
