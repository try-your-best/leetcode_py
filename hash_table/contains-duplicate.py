# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution(object):

	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		return len(nums) > len(set(nums))

