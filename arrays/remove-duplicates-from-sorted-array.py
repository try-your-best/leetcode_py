# -*- coding: utf-8 -*-
__author__ = "damon"

from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums:
			return 0

		last = 0
		for i in range(len(nums)):
			if nums[last] != nums[i]:
				last += 1
				nums[last] = nums[i]
		return last+1


if __name__ == '__main__':
	sl = Solution()

	nums = [1, 1, 2]
	print(sl.removeDuplicates(nums))
	print(nums)

	nums = [0,0,1,1,1,2,2,3,3,4]
	print(sl.removeDuplicates(nums))
	print(nums)
