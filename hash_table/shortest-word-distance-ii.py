# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/5187640.html
注意有 shortest-word-distance， 
"""

import collections

class WordDistance:
	# initialize your data structure here.
	# @param {string[]} words
	def __init__(self, words):
		self.word_index = collections.defaultdict(list)
		for i in range(len(words)):
			self.word_index[words[i]].append(i)

	# @param {string} word1
	# @param {string} word2
	# @return {integer}
	# Adds a word into the data structure.
	def shortest(self, word1, word2):
		w1_index = self.word_index[word1]
		w2_index = self.word_index[word2]
		w1_index_len = len(w1_index)
		w2_index_len = len(w2_index)
		i, j = 0, 0
		min_len = float("inf")
		while i < w1_index_len and j < w2_index_len:
			min_len = min(min_len, abs(w1_index[i]-w2_index[j]))
			if w1_index[i] < w2_index[j]:
				i += 1
			else:
				j += 1
		return min_len


if __name__ == '__main__':
	wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
	print(wd.shortest('coding', 'practice'))
	print(wd.shortest('makes', 'coding'))