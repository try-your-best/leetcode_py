# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

import functools

"""
https://www.cnblogs.com/grandyang/p/4225047.html
"""


class Solution:
	def largestNumber(self, nums: List[int]) -> str:
		if not nums:
			return ''
		nums_str = [str(x) for x in nums]

		def compare(x, y):
			x_y = x + y
			y_x = y + x
			if x_y == y_x:
				return 0
			elif x_y > y_x:
				return -1
			else:
				return 1
		nums_str.sort(key=functools.cmp_to_key(compare))

		return ''.join(nums_str) if nums_str[0] != '0' else '0'


if __name__ == "__main__":
	sl = Solution()
	print(sl.largestNumber([10,2]))
	print(sl.largestNumber([3,30,34,5,9]))  # "9534330"
	print(sl.largestNumber([0,0])) # 0 not 00
