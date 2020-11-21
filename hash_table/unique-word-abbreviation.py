# -*- coding: utf-8 -*-
__author__ = 'damon'

from collections import defaultdict

"""
https://www.cnblogs.com/grandyang/p/5220589.html
保留头尾字符串，还有中间长度。除了判断缩写，还要判断单词是否在字典中。
"""

class ValidWordAbbr:
	def __init__(self, dictionary):
		self.lookup = defaultdict(set)
		for s in dictionary:
			self.lookup[self.abbr(s)].add(s)

	def isUnique(self, word):
		word_abbr = self.abbr(word)
		return word_abbr not in self.lookup or (len(self.lookup[word_abbr]) == 1 and word in self.lookup[word_abbr])

	@staticmethod
	def abbr(string):
		if len(string) <= 2:
			return string
		else:
			return ''.join([string[0], str(len(string)-2),string[-1]])


if __name__ == '__main__':
	vwa = ValidWordAbbr(["deer", "door", "cake", "card"])
	print(vwa.isUnique("dear")) #-> false
	print(vwa.isUnique("cart")) #-> true
	print(vwa.isUnique("cane")) #-> false
	print(vwa.isUnique("make")) #-> true



