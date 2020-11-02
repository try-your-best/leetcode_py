# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = (low + high)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				high = mid - 1
			else:
				low = mid + 1

		if nums[low] == target:
			return low
		elif nums[low] > target:
			return low
		else:
			return low + 1



"""
这种更简洁，但是上面那种更直观
"""
class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low <= high:
			mid = (low + high)//2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				high = mid - 1
			else:
				low = mid + 1
		return low


if __name__ == '__main__':
	sl = Solution()
	print(sl.searchInsert([1,3,5,6], 5))
	print(sl.searchInsert([1,3,5,6], 2))
	print(sl.searchInsert([1,3,5,6], 7))
	print(sl.searchInsert([1,3,5,6], 0))