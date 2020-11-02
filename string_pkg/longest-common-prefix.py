# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if len(strs) < 1:
			return ''
		common = []
		for i in range(0, len(strs[0])):
			for j in range(1, len(strs)):
				if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
					return ''.join(common)
			common.append(strs[0][i])

		return ''.join(common)


if __name__ == '__main__':
	sl =Solution()
	print(sl.longestCommonPrefix(["flower","flow","flight"]))
	print(sl.longestCommonPrefix(["dog","racecar","car"]))
	print(sl.longestCommonPrefix(["dog"]))
	print(sl.longestCommonPrefix(["aa", "a"]))