# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def findSpecialInteger(self, arr: List[int]) -> int:
		n = len(arr)
		q = n // 4
		for i in range(n-q):
			if arr[i] == arr[i+q]:
				return arr[i]
		return arr[0]


import bisect
class Solution:
	def findSpecialInteger(self, arr: List[int]) -> int:
		n = len(arr)
		q = n // 4
		for i in (n//4, n//2, 3*n//4):
			start = bisect.bisect_left(arr, arr[i])
			end = bisect.bisect_right(arr, arr[i])
			if (end - start) * 4 > n:
				# print(arr)
				return arr[i]
		return arr[0]


if __name__ == '__main__':
	sl = Solution()
	print(sl.findSpecialInteger([1,2,2,6,6,6,6,7,10]))