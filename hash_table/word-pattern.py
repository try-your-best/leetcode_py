# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4857022.html
"""

# Time:  O(n)
# Space: O(n)
class Solution(object):
	def wordPattern(self, pattern, string):
		strs = string.split(' ')
		if len(pattern) != len(strs): return False
		p2w = {}
		w2p = {}
		for p, w in zip(pattern, strs):
			if p in p2w:
				if p2w[p] != w: return False
			elif w in w2p:
				if w2p[w] != p: return False  # 注意双向映射
			else:
				p2w[p] = w
				w2p[w] = p

		return True

"""
参考同构词思路
isomorphic-strings
"""

class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		strs = s.split(' ')
		if len(pattern) != len(strs): return False
		p_dict = {}
		s_dict = {}

		for idx, p in enumerate(pattern):
			w = strs[idx]
			if p not in p_dict and w not in s_dict:
				p_dict[p] = idx
				s_dict[w] = idx
			elif p in p_dict and w in s_dict:
				if p_dict[p] == s_dict[w]:
					p_dict[p] = idx
					s_dict[w] = idx
				else:
					return False
			else:
				return False
		return True


class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		strs = s.split(' ')
		if len(pattern) != len(strs): return False
		p_dict = {}
		s_dict = {}

		for idx, p in enumerate(pattern):
			w = strs[idx]
			if p_dict.get(p) == s_dict.get(w):
				p_dict[p] = idx
				s_dict[w] = idx
			else:
				return False

		return True


if __name__ == '__main__':
	sl = Solution()
	print(sl.wordPattern('abba', 'dog cat cat dog'))
	print(sl.wordPattern('abba', 'dog cat cat fish'))
	print(sl.wordPattern('aaaa', 'dog cat cat dog'))
	print(sl.wordPattern('abba', 'dog dog dog dog'))  # False  注意是双向映射