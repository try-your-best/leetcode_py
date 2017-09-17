# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

# Time:  O(nlogn)
# Space: O(n)

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?

# Sorting and reoder solution. (92ms)


class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		med = (len(nums) - 1) / 2
		nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]


class Solution2(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		temp = [num for num in nums]
		bigIdx = len(temp) - 1
		lessIdx = bigIdx/2

		for idx in xrange(len(temp)):
			if idx % 2:
				nums[idx] = temp[bigIdx]  # 下标都是从大到小，中间有些一样大小的数字
				bigIdx -= 1
			else:
				nums[idx] = temp[lessIdx]
				lessIdx -= 1


if __name__ == "__main__":
	nums = [1, 5, 1, 1, 6, 4]
	nums = [1, 3, 2, 2, 3, 1]
	# Solution().wiggleSort(nums)
	Solution2().wiggleSort(nums)
	print nums

