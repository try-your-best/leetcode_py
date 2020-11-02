# -*- coding: utf-8 -*-


# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#

# 就是二分查找的变异

class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		left, right = 0, len(nums)-1

		# 注意是 <= , 不是 <。
		while left <= right:
			mid = (left + right) / 2
			# mid = left + (right - left) / 2

			if nums[mid] == target:
				return mid
			# 第一个条件是左边有序，并且利用有序判定在左边。第二是右边有序，并判定不在右边
			elif (nums[left] <= nums[mid] and nums[left] <= target < nums[mid]) or \
					(nums[left] > nums[mid] and not(nums[mid] < target <= nums[right])):
				right = mid - 1
			else:
				left = mid + 1

		return -1


if __name__ == "__main__":
	nums = [4, 5, 6, 7, 0, 1, 2]
	print Solution().search(nums, 6)