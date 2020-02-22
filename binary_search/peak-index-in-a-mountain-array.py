# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/10527596.html
这道题 mid 与 left 和 right 比较是没有信息含量，只能跟相邻节点比较。不断收缩。构建 A[mid] < A[mid+1] 让代码更简介，因为
mid = left + (right-left) // 2 会有 mid < right,  right=len(A) - 1会保证不越界。
"""

class Solution:
	def peakIndexInMountainArray(self, A: List[int]) -> int:
		left = 0
		right = len(A) - 1
		while left < right:
			mid = left + (right-left) // 2
			if mid > 0:
				if A[mid-1] < A[mid]:
					left = mid + 1
				else:
					right = mid
			else:
				left = mid + 1
		return left - 1


class Solution:
	def peakIndexInMountainArray(self, A: List[int]) -> int:
		left = 0
		right = len(A) - 1
		while left < right:
			mid = left + (right-left) // 2
			if A[mid] < A[mid+1]:
				left = mid + 1
			else:
				right = mid
		return right



if __name__ == '__main__':
	sl = Solution()
	print(sl.peakIndexInMountainArray([0,1,0])) # 1
	print(sl.peakIndexInMountainArray([0,2,1,0])) # 1
