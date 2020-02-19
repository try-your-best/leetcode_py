# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		k = m+n-1
		i = m-1
		j = n-1
		while k >= 0:
			if i >= 0 and j >= 0:
				if nums1[i] > nums2[j]:
					nums1[k] = nums1[i]
					i -= 1
				else:
					nums1[k] = nums2[j]
					j -= 1
			elif j >= 0:
				nums1[k] = nums2[j]
				j -= 1
			else:
				break
			k -= 1


if __name__ == "__main__":
	sl = Solution()
	nums1 = [1, 2, 3, 0, 0, 0]
	nums2 = [2, 5, 6]
	sl.merge(nums1, 3, nums2, 3)
	print(nums1)
