# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4313384.html
这道题要求解码方法，跟之前那道 Climbing Stairs 非常的相似，但是还有一些其他的限制条件，比如说一位数时不能为0，两位数不能大于 26，其十位上的数也不能为0，除去这些限制条件，跟爬梯子基本没啥区别
"""

class Solution:
	def numDecodings(self, s: str) -> int:
		n = len(s)
		dp = [0] * (n+1)

		dp[0] = 1

		for i in range(1, n+1):
			if i == 1:
				if s[i-1] != '0':
					dp[i] = 1
			else:
				if s[i-1] != '0':
					if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
						dp[i] = dp[i-1] + dp[i-2]
					else:
						dp[i] = dp[i-1]
				else:
					if s[i - 2] == '1' or s[i - 2] == '2':
						dp[i] = dp[i-2]

		return dp[n]


class Solution:
	def numDecodings(self, s: str) -> int:
		valid_set = set([str(i) for i in range(1, 27)])
		n = len(s)
		dp = [0] * (n+1)
		dp[0] = 1
		dp[1] = 1 if s[0] in valid_set else 0
		for i in range(2, n+1):
			if s[i-1] in valid_set:
				dp[i] += dp[i-1]
			if s[i-2:i] in valid_set:
				dp[i] += dp[i-2]

		return dp[n]




if __name__ == '__main__':
	sl = Solution()
	print(sl.numDecodings('226')) # 3 "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
	print(sl.numDecodings('2213')) #
	print(sl.numDecodings('201')) #
	print(sl.numDecodings('301')) #
	print(sl.numDecodings('1301')) #
	print(sl.numDecodings('0'))  # 0
