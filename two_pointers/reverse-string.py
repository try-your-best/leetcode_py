# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		left = 0
		right = len(s)-1
		while left < right:
			s[left], s[right] = s[right], s[left]
			left += 1
			right -= 1


if __name__ == '__main__':
	sl =Solution()
	s = ["h","e","l","l","o"]
	sl.reverseString(s)
	print(s)
