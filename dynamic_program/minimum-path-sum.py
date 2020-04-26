# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4353255.html
这道题给了我们一个只有非负数的二维数组，让找一条从左上到右下的路径，使得路径和最小，限定了每次只能向下或者向右移动。
一个常见的错误解法就是每次走右边或下边数字中较小的那个，这样的贪婪算法获得的局部最优解不一定是全局最优解，因此是不行的。
实际上这道题跟之前那道 Dungeon Game 没有什么太大的区别，都需要用动态规划 Dynamic Programming 来做，这应该算是 DP 问题中比较简单的一类，
我们维护一个二维的 dp 数组，其中 dp[i][j] 表示到达当前位置的最小路径和。接下来找状态转移方程，因为到达当前位置 (i, j)  只有两种情况，
要么从上方 (i-1, j) 过来，要么从左边 (i, j-1) 过来，我们选择 dp 值较小的那个路径，即比较 dp[i-1][j] 和 dp[i][j-1]，将其中的较小值加上当前的数字 grid[i][j]，
就是当前位置的 dp 值了。但是有些特殊情况要提前赋值，比如起点位置，直接赋值为 grid[0][0]，还有就是第一行和第一列，其中第一行的位置只能从左边过来，
第一列的位置从能从上面过来，所以这两行要提前初始化好，然后再从 (1, 1) 的位置开始更新到右下角即可，反正难度不算大，代码如下：
"""

class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		m = len(grid)
		n = len(grid[0])
		dp = [[float('inf')] * (n+1) for _ in range(m+1)]
		dp[1][0] = 0
		for i in range(1, m+1):
			for j in range(1, n+1):
				dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

		return dp[m][n]


if __name__ == '__main__':
	sl = Solution()
	grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
	]
	print(sl.minPathSum(grid))