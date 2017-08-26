# -*- coding: utf-8 -*-

# Time:  O(n)
# Space: O(1)
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
#


"""
它限定了两个队列都是升序的。其实可以是降序，也可以是不同序。
"""


class Solution(object):

	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		last, i, j = m + n - 1, m - 1, n - 1

		while i >= 0 and j >= 0:
			if nums1[i] > nums2[j]:
				nums1[last] = nums1[i]
				last, i = last - 1, i - 1
			else:
				nums1[last] = nums2[j]
				last, j = last - 1, j - 1

		while j >= 0:
			nums1[last] = nums2[j]
			last, j = last - 1, j - 1


if __name__ == "__main__":
	A = [1, 3, 5, 0, 0, 0, 0]
	B = [2, 4, 6, 7]
	Solution().merge(A, 3, B, 4)
	print A

