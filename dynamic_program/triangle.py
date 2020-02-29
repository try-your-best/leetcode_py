# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
动态规划最重要的是先得到核心表达式，然后在开始处理边界条件
"""


class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		m = len(triangle)
		n = len(triangle[-1])
		dp = [0] * n
		dp[0] = triangle[0][0]
		for i in range(1, m):
			max_j = len(triangle[i])-1
			dp[max_j] = dp[max_j-1] + triangle[i][max_j]
			for j in range(max_j-1, 0, -1):  # not 0 is not included
				# print('a',j, dp[j], dp[j-1], triangle[i][j])
				dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
			dp[0] += triangle[i][0]
			# print(i, dp)

		# print(dp)
		return min(dp)


def func1():
	sl = Solution()
	triangle = [
			[2],
			[3, 4],
			[6, 5, 7],
			[4, 1, 8, 3]
		]
	print(sl.minimumTotal(triangle))


if __name__ == '__main__':
	func1()

