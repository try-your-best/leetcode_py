# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution(object):
	def missingNumber(self, arr:List[int]):
		n = len(arr)
		return int(0.5 * (1+n) * n - sum(arr))


"""
假如序列有序，用二分
"""
class Solution(object):
	def missingNumber(self, arr: List[int]):
		arr.sort()
		left = 0
		right = len(arr)
		while left < right:
			mid = left + (right - left)//2
			if arr[mid] == mid:
				left = mid + 1
			else:  # arr[mid] < mid
				right = mid
		return right

Main = Solution


if __name__ == '__main__':
	sl = Main()
	print(sl.missingNumber([0, 1, 3]))
	print(sl.missingNumber([0, 1, 2]))