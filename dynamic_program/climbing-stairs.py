# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4079165.html
"""

class Solution:
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		a = 1
		b = 2
		c = 0
		for i in range(2, n):
			c = b + a
			a = b
			b = c

		return c


if __name__ == '__main__':
	sl = Solution()
	print(sl.climbStairs(2))
	print(sl.climbStairs(3))