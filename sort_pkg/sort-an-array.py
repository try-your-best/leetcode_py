# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		# self.quickSort(nums, 0, len(nums)-1)
		self.mergeSort(nums, 0, len(nums)-1)
		return nums

	def quickSort(self, nums: List[int], left:int, right:int):
		if left >= right:
			return
		p = self.partition(nums, left, right)
		self.quickSort(nums, left, p-1)
		self.quickSort(nums, p+1, right)

	def partition(self, nums: List[int], left:int, right:int):
		pivot = nums[right]
		i = left - 1
		for j in range(left, right):
			if nums[j] <= pivot:
				i += 1
				nums[i], nums[j] = nums[j], nums[i]

		i += 1
		nums[i], nums[right] = nums[right], nums[i]
		return i

	def mergeSort(self, nums: List[int], left:int, right:int):
		if left >= right:
			return
		mid = (left + right) // 2
		self.mergeSort(nums, left, mid)
		self.mergeSort(nums, mid+1, right)
		self.merge(nums, left, mid, right)

	def merge(self, nums, left, mid, right):
		tmp = nums[left:right+1]
		i = 0
		j = mid+1-left
		k = left
		while i <= mid-left and j <= right-left:
			# print(i, j)
			if tmp[i] <= tmp[j]:
				nums[k] = tmp[i]
				i += 1
			else:
				nums[k] = tmp[j]
				j += 1

			k += 1

		while i <= mid-left:
			nums[k] = tmp[i]
			i += 1
			k += 1

		while j <= right-left:
			nums[k] = tmp[j]
			j += 1
			k += 1


if __name__ == "__main__":
	sl = Solution()
	print(sl.sortArray([5,2,3,1]))