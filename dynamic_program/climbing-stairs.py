# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4079165.html
"""

class Solution:
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		n1 = 1
		n2 = 2
		n3 = 0
		for i in range(2, n):
			n3 = n2 + n1
			n1 = n2
			n2 = n3

		return n3


if __name__ == '__main__':
	sl = Solution()
	print(sl.climbStairs(2))
	print(sl.climbStairs(3))