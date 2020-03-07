# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		left = 0
		right = len(numbers) - 1

		while left < right:
			cur_sum = numbers[left] + numbers[right]
			if cur_sum < target:
				left += 1
			elif cur_sum > target:
				right -= 1
			else:
				return [left+1, right+1]


if __name__ == '__main__':
	sl = Solution()
	print(sl.twoSum([2,7,11,15], 9))