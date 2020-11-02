# -*- coding: utf-8 -*-
__author__ = "damon"


# class Solution(object):
# 	def removeDuplicates(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: int
# 		"""
# 		cur = None
# 		i = 0
# 		j = len(nums)
#
# 		while i < j:
# 			if nums[i] != cur:
# 				cur = nums[i]
# 				i += 1
# 			else:
# 				nums.pop(i)
# 				j -= 1
#
# 		return j


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
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
