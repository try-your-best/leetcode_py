# -*- coding: utf-8 -*-
__author__ = 'damon'


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
				if w2p[w] != p: return False
			else:
				p2w[p] = w
				w2p[w] = p

		return True


if __name__ == '__main__':
	sl = Solution()
	print(sl.wordPattern('abba', 'dog cat cat dog'))
	print(sl.wordPattern('abba', 'dog cat cat fish'))
	print(sl.wordPattern('aaaa', 'dog cat cat dog'))
	print(sl.wordPattern('abba', 'dog dog dog dog'))  # False  注意是双向映射