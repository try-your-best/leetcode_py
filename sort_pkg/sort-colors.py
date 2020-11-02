# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


# class Solution:
# 	def sortColors(self, nums: List[int]) -> None:
# 		"""
# 		Do not return anything, modify nums in-place instead.
# 		"""
# 		count = [0] * 3
# 		for n in nums:
# 			count[n] += 1
#
# 		n = 0
# 		for i, v in enumerate(count):
# 			for _ in range(0, v):
# 				nums[n] = i
# 				n += 1


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		start = 0
		end = len(nums) - 1
		i = 0
		while i <= end:
			if nums[i] == 0:
				nums[start], nums[i] = nums[i], nums[start]
				start += 1
				i += 1
			elif nums[i] == 2:  # 注意这个分支 i 不要更新
				nums[end], nums[i] = nums[i], nums[end]
				end -= 1
			else:
				i += 1


if __name__ == "__main__":
	sl = Solution()
	nums = [2,0,2,1,1,0]
	sl.sortColors(nums)
	print(nums)