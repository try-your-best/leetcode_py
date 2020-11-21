# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4383632.html
"""

class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		elif len(nums) == 1:
			return nums[0]
		n = len(nums)
		dp = [0] * (n+1)
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range(2, n):
			dp[i] = max(dp[i-1], dp[i-2] + nums[i])

		return dp[n-1]


class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		n = len(nums)
		dp = [0] * (n+1)
		dp[1] = nums[0]
		for i in range(2, n+1):
			dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
		return dp[n]


if __name__ == '__main__':
	sl = Solution()
	print(sl.rob([1,2,3,1])) # 4
	print(sl.rob([2,7,9,3,1])) # 12