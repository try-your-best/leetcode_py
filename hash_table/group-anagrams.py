# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List
import collections

"""
https://www.cnblogs.com/grandyang/p/4385822.html
"""

# class Solution:
# 	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# 		look_up = {}
# 		for s in strs:
# 			key = ''.join(sorted(s))
# 			if key in look_up:
# 				look_up[key].append(s)
# 			else:
# 				look_up[key] = [s]
#
# 		return list(look_up.values())


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		look_up = collections.defaultdict(list)
		counter = [0] * 26
		for s in strs:
			for char in s:
				counter[ord(char)-ord('a')] += 1
			look_up[tuple(counter)].append(s)
			counter = [0] * 26

		return list(look_up.values())


if __name__ == '__main__':
	sl = Solution()
	print(sl.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))