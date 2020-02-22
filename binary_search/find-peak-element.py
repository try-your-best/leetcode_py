# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

# Time:  O(logn)
# Space: O(1)

"""
https://www.cnblogs.com/grandyang/p/4217175.html
"""

class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				return i
		return len(nums) - 1


class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		left = 0
		right = len(nums)-1
		while left < right:
			mid = left + (right - left)//2
			if nums[mid] < nums[mid+1]:
				left = mid + 1
			else:
				right = mid
		return right


if __name__ == '__main__':
	sl = Solution()
	print(sl.findPeakElement([1,2,3,1]))
	print(sl.findPeakElement([1,2,1,3,5,6,4]))
	print(sl.findPeakElement([1]))
