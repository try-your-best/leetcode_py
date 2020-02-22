# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4782695.html
"""

"""方便理解版本"""
class Solution:
	def hIndex(self, citations: List[int]) -> int:
		h = 0
		for i in range(len(citations)-1, -1, -1):
			if citations[i] >= h + 1:  # h+1 既是数量，满足条件最小值。当出现 h + 1 > citations[i], 则 citations[i] <= h < citations[i+1], 由于是升序的列表，完美满足 h index 含义
				h += 1
			else:
				break
		return h


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		h = 0
		for c in reversed(citations):
			if c >= h + 1:
				h += 1
			else:
				break
		return h


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		if not citations:
			return 0
		left = 0
		right = len(citations)-1
		length = len(citations)
		while left < right:
			mid = left + (right - left)//2
			h = length - mid
			if citations[mid] < h:
				left = mid + 1
			elif citations[mid] > h:
				right = mid
			else:
				return h
		h = length - right
		return h if citations[right] >= h else h-1


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		if not citations:
			return 0
		left = 0
		right = len(citations)-1
		length = len(citations)
		while left <= right:
			mid = left + (right - left)//2
			h = length - mid
			if citations[mid] < h:
				left = mid + 1
			elif citations[mid] > h:
				right = mid - 1
			else:
				return h

		return length - left


if __name__ == '__main__':
	sl = Solution()
	# print(sl.hIndex([0,1,3,5,6])) # 3
	# print(sl.hIndex([0,3,3,5,6])) # 3
	# print(sl.hIndex([0,3,4,5,6])) # 3
	# print(sl.hIndex([2,2])) # 2
	# print(sl.hIndex([1,2])) # 1
	print(sl.hIndex([1,1,2])) # 1
	# print(sl.hIndex([1])) # 1
	print(sl.hIndex([])) # 0
	print(sl.hIndex([0])) # 0