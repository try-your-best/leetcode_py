# -*- coding: utf-8 -*-
__author__ = 'damon'


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