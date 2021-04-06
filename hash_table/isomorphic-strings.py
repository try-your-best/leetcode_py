# -*- coding: utf-8 -*-
__author__ = 'damon'

from collections import defaultdict

"""
同构字符串 
https://www.cnblogs.com/grandyang/p/4465779.html
"""

class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		s_dict = defaultdict(list)
		t_dict = defaultdict(list)

		for idx, a in enumerate(s):
			s_dict[a].append(idx)

		for idx, a in enumerate(t):
			t_dict[a].append(idx)

		return set([tuple(x) for x in s_dict.values()]) == set([tuple(x) for x in t_dict.values()])


class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		"""
		核心思想是对应的字符上次出现的位置要相同
		"""
		if len(s) != len(t):
			return False

		s_lookup = [-1] * 256
		t_lookup = [-1] * 256

		for idx in range(0, len(s)):
			s_code = ord(s[idx])
			t_code = ord(t[idx])
			if s_lookup[s_code] != t_lookup[t_code]:
				return False
			s_lookup[s_code] = idx
			t_lookup[t_code] = idx

		return True


if __name__ == '__main__':
	sl = Solution()
	print(sl.isIsomorphic('egg', 'add'))
	print(sl.isIsomorphic('foo', 'bar'))
	print(sl.isIsomorphic('paper', 'title'))