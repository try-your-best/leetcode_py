# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://strstr.io/Leetcode1064-Fixed-Point/

Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i. Return -1 if no such i exists.

Example 1: Input: [-10,-5,0,3,7] Output: 3 Explanation: For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Example 2: Input: [0,2,5,8,17] Output: 0 Explanation: A[0] = 0, thus the output is 0.

Example 3: Input: [-10,-5,3,4,7,9] Output: -1 Explanation: There is no such i that A[i] = i, thus the output is -1.

Note: 1 <= A.length < 10^4 -10^9 <= A[i] <= 10^9

# Time:  O(logn)
# Space: O(1)
"""


class Solution(object):
	def fixedPoint(self, A: List[int]) -> int:
		left = 0
		right = len(A) - 1
		ret = -1

		while left <= right:
			mid = left + (right - left) // 2
			if A[mid] == mid:
				ret = mid
				right = mid - 1
			elif A[mid] < mid:  # 注意条件 A of distinct integers， 所以当  A[mid] < mid，可以推论 A[mid-1] < mid-1，因此 mid 之前都没有符合条件的
				left = mid + 1
			else:
				right = mid - 1

		return ret

class Solution(object):
	def fixedPoint(self, A: List[int]) -> int:
		left = 0
		right = len(A) - 1

		while left <= right:
			mid = left + (right - left) // 2
			if A[mid] < mid:  # 注意条件 A of distinct integers， 所以当  A[mid] < mid，可以推论 A[mid-1] < mid-1，因此 mid 之前都没有符合条件的
				left = mid + 1
			else:
				right = mid - 1
		# 代入两个 case 就知道这时用 left， 也可以说只有 A[mid] < mid，left = mid + 1， 那么最终结束时，left 是符合条件的。
		return left if A[left] == left else -1


if __name__ == '__main__':
	sl = Solution()
	print(sl.fixedPoint([-10,-5,0,3,7])) # 3
	print(sl.fixedPoint([0,2,5,8,17]))  # 0
	print(sl.fixedPoint([-10,-5,3,4,7,9])) #-1
	print(sl.fixedPoint([0,1,2])) # 0
	print(sl.fixedPoint([-1,1,2,4,6])) #1
	print(sl.fixedPoint([-1,1])) # 1