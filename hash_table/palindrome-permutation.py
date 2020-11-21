# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/5223238.html
注意：不能用异或，因为无法处理奇数情况
"""

class Solution(object):
	def canPermutePalindrome(self, s):
		lookup = {}
		for cur_s in s:
			lookup[cur_s] = lookup.get(cur_s, 0) + 1

		c = 0
		for val in lookup.values():
			if val % 2 == 1:
				c += 1
		return c == 0 or (len(s) % 2 == 1 and c == 1)


if __name__ == '__main__':
	sl = Solution()
	print(sl.canPermutePalindrome('code'))  # false
	print(sl.canPermutePalindrome('aab')) # true
	print(sl.canPermutePalindrome('carerac')) # true