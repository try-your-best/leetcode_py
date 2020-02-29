# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		if not matrix or not matrix[0] or (type(matrix[0][0]) is list and not matrix[0][0]):
			self.dp = None
			return
		m = len(matrix)
		n = len(matrix[0])
		dp = [[0] * (n+1) for _ in range(m+1)]
		self.dp = dp

		for i in range(1, m+1):
			for j in range(1, n+1):
				dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i-1][j-1]

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		dp = self.dp
		if not dp:
			return 0
		return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1]

def func1():

	matrix = [
		[3, 0, 1, 4, 2],
		[5, 6, 3, 2, 1],
		[1, 2, 0, 1, 5],
		[4, 1, 0, 1, 7],
		[1, 0, 3, 0, 5]
	]

	sl = NumMatrix(matrix)
	print(sl.sumRegion(2, 1, 4, 3))
	print(sl.sumRegion(1, 1, 2, 2))
	print(sl.sumRegion(1, 2, 2, 4))


def func2():
	# print(not 0)
	matrix = [
		[[]]
	]  # 这个输入是错误格式吧

	print(len(matrix))

	sl = NumMatrix(matrix)
	print(sl.sumRegion(2, 1, 4, 3))
	print(sl.sumRegion(1, 1, 2, 2))
	print(sl.sumRegion(1, 2, 2, 4))


if __name__ == '__main__':
	func2()

