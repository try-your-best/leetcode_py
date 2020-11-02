# -*- coding: utf-8 -*-

"""
https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.md
"""


class Solution:
		"""
		@param A, B: Two strings.
		@return: The length of longest common subsequence of A and B.  不要求子序列连续
		"""
		def longestCommonSubsequence(self, A, B):
			n, m = len(A), len(B)
			dp = [[0] * (m+1) for _ in range(n+1)]

			for i in range(n):
				for j in range(m):
					if A[i] == B[j]:
						dp[i+1][j+1] = dp[i][j] + 1
					else:
						dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

			return dp[n][m]

		def longestCommonSubsequence2(self, A, B):
			n, m = len(A), len(B)
			dp = [0] * (m+1)

			for i in range(n):
				for j in range(m):
					if A[i] == B[j]:
						dp[j+1] = dp[j] + 1
					else:
						dp[j+1] = max(dp[j], dp[j+1])  # dp[j] ==  dp[i+1][j] 其实是已更新的值

			return dp[m]


if __name__ == "__main__":
	s = Solution()
	print(s.longestCommonSubsequence('abc', 'ac'))
	print(s.longestCommonSubsequence('abcdefg', 'dfg'))
	print(s.longestCommonSubsequence2('abc', 'ac'))
	print(s.longestCommonSubsequence2('abcdefg', 'dfg'))
