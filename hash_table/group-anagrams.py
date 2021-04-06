# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List
import collections

"""
https://www.cnblogs.com/grandyang/p/4385822.html
让我们群组给定字符串集中所有的错位词，所谓的错位词就是两个字符串中字母出现的次数都一样，只是位置不同，比如 abc，bac, cba 等它们就互为错位词，
那么如何判断两者是否是错位词呢，可以发现如果把错位词的字符顺序重新排列，那么会得到相同的结果，所以重新排序是判断是否互为错位词的方法
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