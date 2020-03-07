# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		zero_idx = 0
		not_zero_idx = 0
		n = len(nums)
		while zero_idx < n and not_zero_idx < n:
			while zero_idx < n and nums[zero_idx] != 0:
				zero_idx += 1

			#  注意条件 not_zero_idx <= zero_idx，要找到 not_zero_idx > zero_idx
			while not_zero_idx < n and (nums[not_zero_idx] == 0 or not_zero_idx <= zero_idx):
				not_zero_idx += 1

			if zero_idx < not_zero_idx < n:
				nums[zero_idx], nums[not_zero_idx] = nums[not_zero_idx], nums[zero_idx]


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		zero_idx = 0
		for i in range(len(nums)):
			if nums[i]:
				nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
				zero_idx += 1


if __name__ == '__main__':
	sl =Solution()
	a = [0,1,0,3,12]
	# a = [1, 0]
	# a = [1,0,3,12]
	sl.moveZeroes(a)
	print(a)