# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

"""
https://www.cnblogs.com/grandyang/p/5177285.html
"""

# Time:  O(n)
# Space: O(1)
class Solution(object):
	def wiggleSort(self, nums):
		for i in range(1, len(nums)):
			if (i%2 == 1 and nums[i] < nums[i-1]) or (i%2 == 0 and nums[i] > nums[i-1]): # 如果原先序不符合条件，换下位置就符合条件了
				nums[i], nums[i-1] = nums[i-1], nums[i]


Main = Solution

# Time:  O(nlogn)
# Space: O(1)
class Solution:
	def wiggleSort(self, nums):
		nums.sort()
		i = 2
		while i < len(nums):
			nums[i], nums[i - 1] = nums[i - 1], nums[i]
			i += 2



if __name__ == "__main__":
	nums = [3, 5, 2, 1, 6, 4]
	# Solution().wiggleSort(nums)
	Main().wiggleSort(nums)
	print(nums)