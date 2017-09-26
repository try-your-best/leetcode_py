# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


class Solution:
		"""
		@param A, B: Two strings.
		@return: The length of longest common subsequence of A and B.
		"""
		def longestCommonSubsequence(self, A, B):
			n, m = len(A), len(B)
			dp = [[0] * (m+1) for _ in xrange(n+1)]

			for i in xrange(n):
				for j in xrange(m):
					if A[i] == B[j]:
						dp[i+1][j+1] = dp[i][j] + 1
					else:
						dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

			return dp[n][m]

if __name__ == "__main__":
	print Solution().longestCommonSubsequence('abc', 'ac')
	print Solution().longestCommonSubsequence('abcdefg', 'dfg')
