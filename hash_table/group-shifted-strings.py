# -*- coding: utf-8 -*-
__author__ = 'damon'

from collections import defaultdict

"""
https://www.cnblogs.com/grandyang/p/5204770.html

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
 

Note: For the return value, each inner list's elements must follow the lexicographic order.
通过间隔去编码
"""


class Solution(object):
	# @param {string[]} strings
	# @return {string[][]}
	def groupStrings(self, strings):
		lookup = defaultdict(list)
		for s in strings:
			key = tuple((ord(s[i+1])-ord(s[i])+26) % 26 for i in range(0, len(s)-1)) if len(s) > 1 else 0
			lookup[key].append(s)

		return list(lookup.values())





if __name__ == '__main__':
	sl = Solution()
	print(sl.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))