# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *
"""
https://www.cnblogs.com/grandyang/p/4377150.html
"""


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		cur_sum = 0
		res = -float('inf')
		# print(res)
		for n in nums:
			cur_sum = max(cur_sum+n, n)
			res = max(res, cur_sum)

		return res


if __name__ == '__main__':
	sl = Solution()
	print(sl.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))