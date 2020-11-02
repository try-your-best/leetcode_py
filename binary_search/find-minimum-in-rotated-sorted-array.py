# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def findMin(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		low = 0
		high = len(nums)-1
		while low <= high:
			mid = (low+high) // 2
			if mid > 0:
				if nums[mid] < nums[mid-1]:
					return nums[mid]
				else:
					if nums[low] <= nums[mid] > nums[high]: # 这里的等于号是因为，(low+high) // 2 会向下取整，low high 相邻时，low == mid
						low = mid + 1
					else:
						high = mid - 1
			else:
				low = mid + 1
		return nums[low-1]


"""
这样会简洁，但难想
"""
class Solution:
	def findMin(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2
			if nums[mid] > nums[high]:
				low = mid + 1
			else:
				high = mid
		return nums[high]


if __name__ == '__main__':
	sl = Solution()
	print(sl.findMin([3,4,5,1,2]))
	print(sl.findMin([4,5,6,7,0,1,2]))
	print(sl.findMin([3,1,2]))
	print(sl.findMin([3,1]))
	print(sl.findMin([1]))
	print(sl.findMin([1, 2])) # 1
	print(sl.findMin([2,3,4,5,1])) # 1