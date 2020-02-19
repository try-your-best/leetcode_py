# -*- coding: utf-8 -*-
__author__ = 'damon'


class NumArray(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""

		self._sum = [0] * (len(nums)+1)

		for i in range(1, len(nums)+1):
			self._sum[i] = self._sum[i-1] + nums[i-1]

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self._sum[j+1] - self._sum[i]


if __name__ == '__main__':
	na = NumArray([-2, 0, 3, -5, 2, -1])
	print(na.sumRange(0, 2))
	print(na.sumRange(2, 5))
	print(na.sumRange(0, 5))
