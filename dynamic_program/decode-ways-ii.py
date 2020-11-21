"""
https://www.cnblogs.com/grandyang/p/7279152.html
注意题目要求大数求余
"""

class Solution:
	def numDecodings(self, s: str) -> int:
		n = len(s)
		dp = [0] * (n+1)
		dp[0] = 1
		max_v = 10**9 + 7
		if s[0] == '0':
			dp[1] = 0
		elif s[0] == '*':
			dp[1] = 9
		else:
			dp[1] = 1
		for i in range(2, n+1):
			if s[i-1] == '0':
				if s[i-2] == '1' or s[i-2] == '2':
					dp[i] += dp[i-2]
				elif s[i-2] == '*':
					dp[i] += dp[i-2] * 2
			elif s[i-1] == '*':
				dp[i] += dp[i-1] * 9
				if s[i-2] == '1':
					dp[i] += dp[i-2] * 9
				elif s[i - 2] == '2':
					dp[i] += dp[i-2] * 6
				elif s[i - 2] == '*':
					dp[i] += dp[i-2] * 15
			else:
				dp[i] += dp[i-1]
				if s[i - 2] == '1' or  (s[i - 2] == '2' and s[i - 1] <= '6'):
					dp[i] += dp[i-2]
				elif s[i - 2] == '*':
					if s[i - 1] <= '6':
						dp[i] += dp[i-2] * 2
					else:
						dp[i] += dp[i-2]
		return dp[n] % max_v


if __name__ == '__main__':
	sl = Solution()
	# print(sl.numDecodings("*"))
	# print(sl.numDecodings("1*"))
	print(sl.numDecodings("**"))
	print(sl.numDecodings("***"))
	print(sl.numDecodings("*********"))