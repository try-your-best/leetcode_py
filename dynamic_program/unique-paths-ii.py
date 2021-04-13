# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4353680.html
这道题是之前那道 Unique Paths 的延伸，在路径中加了一些障碍物，还是用动态规划 Dynamic Programming 来解，使用一个二维的 dp 数组，大小为 (m+1) x (n+1)，
这里的 dp[i][j] 表示到达 (i-1, j-1) 位置的不同路径的数量，那么i和j需要更新的范围就是 [1, m] 和 [1, n]。状态转移方程跟之前那道题是一样的，
因为每个位置只能由其上面和左面的位置移动而来，所以也是由其上面和左边的 dp 值相加来更新当前的 dp 值，如下所示：

dp[i][j] = dp[i-1][j] + dp[i][j-1]

这里就能看出来初始化 d p数组的大小为 (m+1) x (n+1)，是为了 handle 边缘情况，当i或j为0时，减1可能会出错。当某个位置是障碍物时，其 dp 值为0，
直接跳过该位置即可。这里还需要初始化 dp 数组的某个值，使得其能正常累加。当起点不是障碍物时，其 dp 值应该为1，即dp[1][1] = 1，
由于其是由 dp[0][1] + dp[1][0] 更新而来，所以二者中任意一个初始化为1即可。由于之后 LeetCode 更新了这道题的 test case，
使得使用 int 型的 dp 数组会有溢出的错误，所以改为使用 long 型的数组来避免 overflow，代码如下：

"""

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		print(obstacleGrid)
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		dp = [[0] * (n+1) for _ in range((m+1))]  # 初始化为 0
		# for d in dp:
		# 	print(id(d))
		# print(dp)
		dp[0][1] = 1
		for i in range(1, m+1):
			for j in range(1, n+1):
				if obstacleGrid[i-1][j-1] != 0:
					continue
				# print(i, j, dp[i-1][j], dp[i][j-1])
				dp[i][j] = dp[i-1][j] + dp[i][j-1]

		# print(dp)
		return dp[m][n]


class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		row = len(obstacleGrid)
		col = len(obstacleGrid[0])
		dp = [0] * (col+1)
		dp[1] = 1  # 这个初始化起决定作用
		for i in range(1, row+1):
			for j in range(1, col+1):
				if obstacleGrid[i-1][j-1] == 1:
					dp[j] = 0
				else:
					dp[j] += dp[j-1]

		return dp[col]


if __name__ == '__main__':
	sl = Solution()
	obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
	]
	print(sl.uniquePathsWithObstacles(obstacleGrid))