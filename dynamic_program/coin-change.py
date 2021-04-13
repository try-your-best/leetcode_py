# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


"""
https://www.cnblogs.com/grandyang/p/5138186.html
对于求极值问题，主要考虑动态规划 Dynamic Programming 来做，好处是保留了一些中间状态的计算值，可以避免大量的重复计算。
我们维护一个一维动态数组 dp，其中 dp[i] 表示钱数为i时的最小硬币数的找零，注意由于数组是从0开始的，所以要多申请一位，数组大小为 amount+1，
这样最终结果就可以保存在 dp[amount] 中了。初始化 dp[0] = 0，因为目标值若为0时，就不需要硬币了。其他值可以初始化是 amount+1，为啥呢？
因为最小的硬币是1，所以 amount 最多需要 amount 个硬币，amount+1 也就相当于当前的最大值了，注意这里不能用整型最大值来初始化，
因为在后面的状态转移方程有加1的操作，有可能会溢出，除非你先减个1，这样还不如直接用 amount+1 舒服呢。好，接下来就是要找状态转移方程了，没思路？
不要紧！回归例子1，假设我取了一个值为5的硬币，那么由于目标值是 11，所以是不是假如我们知道 dp[6]，那么就知道了组成 11 的 dp 值了？
所以更新 dp[i] 的方法就是遍历每个硬币，如果遍历到的硬币值小于i值（比如不能用值为5的硬币去更新 dp[3]）时，用 dp[i - coins[j]] + 1 
来更新 dp[i]，所以状态转移方程为：

dp[i] = min(dp[i], dp[i - coins[j]] + 1);
其中 coins[j] 为第j个硬币，而 i - coins[j] 为钱数i减去其中一个硬币的值，剩余的钱数在 dp 数组中找到值，
然后加1和当前 dp 数组中的值做比较，取较小的那个更新 dp 数组。
"""


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		dp = [float('inf')] * (amount+1)
		dp[0] = 0
		for i in range(1, amount+1):
			for c in coins:
				if c <= i:
					dp[i] = min(dp[i], dp[i-c]+1)

		# return dp[amount] if dp[amount] < float('inf') else -1
		return dp[amount] if dp[amount] <= amount else -1


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		dp = [amount+1] * (amount+1)
		dp[0] = 0
		for i in range(1, amount+1):
			for c in coins:
				if c <= i:
					dp[i] = min(dp[i], dp[i-c]+1)

		return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
	sl = Solution()
	print(sl.coinChange([1, 2, 5], 11)) # 3
	print(sl.coinChange([2], 3))
	print(float('inf') == float('inf'))
	print(float('inf') < float('inf'))
	print(float('inf')+1)