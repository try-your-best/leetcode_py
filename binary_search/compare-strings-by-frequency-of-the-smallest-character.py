# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
		words = [Solution.f(w) for w in words]
		queries = [Solution.f(q) for q in queries]
		words.sort()
		return [Solution.findNum(query, words) for query in queries]

	@staticmethod
	def findNum(query_num, words_num):
		left = 0
		right = len(words_num)
		while left < right:
			mid = left + (right - left)//2
			if query_num >= words_num[mid]:
				left = mid + 1
			else:
				right = mid
		return len(words_num) - right

	@staticmethod
	def f(s:str):
		lookup = [0] * 26
		a_code = ord('a')
		for s_tmp in s:
			lookup[ord(s_tmp)-a_code] += 1
		for n in lookup:
			if n > 0:
				return n

if __name__ == '__main__':
	sl = Solution()
	print(sl.numSmallerByFrequency(["cbd"], ["zaaaz"]))
	print(sl.numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]))