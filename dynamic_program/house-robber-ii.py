# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4518674.html
"""

class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		elif len(nums) == 1:
			return nums[0]
		else:
			return max(self._rob(nums, 0, len(nums)-2), self._rob(nums, 1, len(nums)-1))

	def _rob(self, nums: List[int], left: int, right: int) -> int:
		if left == right:
			return nums[left]
		n = right-left+1
		dp = [0] * n
		dp[0] = nums[left]
		dp[1] = max(nums[left], nums[left+1])
		for i in range(2, n):
			dp[i] = max(dp[i-1], dp[i-2]+nums[left+i])

		return dp[n-1]


if __name__ == '__main__':
	sl = Solution()
	print(sl.rob([2,3,2]))
	print(sl.rob([1,2,3,1]))