# -*- coding: utf-8 -*-
__author__ = "damon"

from typing import List

"""
https://www.cnblogs.com/grandyang/p/4606700.html
从快排的换位中借鉴思想
"""

class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		i = len(nums)
		for j in range(len(nums)-1, -1, -1):
			if nums[j] == val:
				i -= 1
				nums[i], nums[j] = nums[j], nums[i]
		return i


if __name__ == '__main__':
	sl = Solution()
	print(sl.removeElement([3,2,2,3], 3))
	print(sl.removeElement([3], 3))