# -*- coding: utf-8 -*-
__author__ = 'damon'


"""
这道题让求所有不同的路径的个数，一开始还真把博主难住了，因为之前好像没有遇到过这类的问题，所以感觉好像有种无从下手的感觉。
在网上找攻略之后才恍然大悟，原来这跟之前那道 Climbing Stairs 很类似，那道题是说可以每次能爬一格或两格，问到达顶部的所有不同爬法的个数。
而这道题是每次可以向下走或者向右走，求到达最右下角的所有不同走法的个数。那么跟爬梯子问题一样，需要用动态规划 Dynamic Programming 来解，
可以维护一个二维数组 dp，其中 dp[i][j] 表示到当前位置不同的走法的个数，然后可以得到状态转移方程为:  dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，
这里为了节省空间，使用一维数组 dp，一行一行的刷新也可以，代码如下：

"""

class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
			dp = [1] * n
			for i in range(1, m):
				for j in range(1, n):
					dp[j] += dp[j-1]

			return dp[n-1]


if __name__ == '__main__':
	sl = Solution()
	print(sl.uniquePaths(3, 2))
	print(sl.uniquePaths(7, 3))