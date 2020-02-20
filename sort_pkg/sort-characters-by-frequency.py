# -*- coding: utf-8 -*-
__author__ = 'damon'

from collections import defaultdict


class Solution:
	def frequencySort(self, s: str) -> str:
		lookup = defaultdict(int)
		for char in s:
			lookup[char] += 1
		char_count = list(lookup.items())
		char_count.sort(key=lambda x: x[1], reverse=True)
		ret = [char * k for char, k in char_count]
		return ''.join(ret)

from collections import defaultdict
import functools

class Solution:
	def frequencySort(self, s: str) -> str:
		lookup = defaultdict(int)
		for char in s:
			lookup[char] += 1

		def compare(x, y):
			if lookup[x] > lookup[y] or (lookup[x]==lookup[y] and x > y):
				return -1
			else:
				return 1
		return ''.join(sorted(s, key=functools.cmp_to_key(compare)))


if __name__ == "__main__":
	sl = Solution()
	print(sl.frequencySort('tree'))
	print(sl.frequencySort('cccaaa'))
	print(sl.frequencySort('Aabb'))
	print(sl.frequencySort("loveleetcode"))