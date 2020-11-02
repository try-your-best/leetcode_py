# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def findMin(self, nums: List[int]) -> int:
		return self._finMin(nums, 0, len(nums)-1)

	def _finMin(self, nums: List[int], left:int, right:int) -> int:
		while left <= right:
			mid = (left + right) // 2
			if mid > 0:
				if nums[mid] < nums[mid-1]:
					return nums[mid]
				elif nums[left] == nums[mid] == nums[right]:
					return min(self._finMin(nums, left + 1, mid), self._finMin(nums, mid, right - 1))
				elif nums[left] <= nums[mid] > nums[right]:
					left = mid + 1
				else:
					right = mid - 1
			else:
				left = mid + 1
		return nums[left - 1]


class Solution:
	def findMin(self, nums: List[int]) -> int:
		left = 0
		right = len(nums)-1
		while left < right:
			mid = left + (right-left) //2
			if nums[mid] > nums[right]:
				left = mid + 1
			elif nums[mid] < nums[right]:
				right = mid
			else:  # 相等时只能得出 nums[right] 不是最小数
				right -= 1
		return nums[right]


class Solution:
	def findMin(self, nums: List[int]) -> int:
		return self._finMin(nums, 0, len(nums)-1)

	def _finMin(self, nums: List[int], left:int, right:int) -> int:
		while left < right:
			mid = left + (right-left) //2
			if nums[mid] > nums[right]:
				left = mid + 1
			elif nums[mid] < nums[right]:
				right = mid
			else:
				return min(self._finMin(nums, left, mid), self._finMin(nums, mid+1, right))
		return nums[right]


if __name__ == '__main__':
	sl = Solution()
	print(sl.findMin([1,3,5]))
	print(sl.findMin([2,2,2,0,1]))
	print(sl.findMin([1,1, 0,1]))
	print(sl.findMin([1,0,1,1,1]))
	print(sl.findMin([1,2]))
	print(sl.findMin([1,1]))
	print(sl.findMin([0,1,1]))
	# print(bool(0 == 0 == 1))