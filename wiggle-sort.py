# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


# Time:  O(n)
# Space: O(1)
class Solution(object):
	def wiggleSort(self, nums):
		for i in xrange(1, len(nums)):
			if (i%2 and nums[i] <= nums[i-1]) or (not i%2 and nums[i] >= nums[i]):
				nums[i], nums[i-1] = nums[i-1], nums[i]


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
	def wiggleSort(self, nums):
		nums.sort()
		i = 2
		while i < len(nums):
			nums[i], nums[i - 1] = nums[i - 1], nums[i]
			i += 2

if __name__ == "__main__":
	nums = [3, 5, 2, 1, 6, 4]
	# Solution().wiggleSort(nums)
	Solution2().wiggleSort(nums)
	print nums