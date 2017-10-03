# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


class Solution:

	# @param {string[]} words
	# @param {string} word1
	# @param {string} word2
	# @return {integer}
	def shortestDistance(self, words, word1, word2):
		idx1, idx2, minDist = None, None, len(words)
		for idx, word in enumerate(words):
			if word == word1:
				idx1 = idx
			elif word == word2:
				idx2 = idx

			if idx1 is not None and idx2 is not None:
				minDist = min(minDist, abs(idx1-idx2))

		return minDist


if __name__ == "__main__":
	words = ["practice", "makes", "perfect", "coding", "makes"]
	word1 = 'coding'
	word2 = 'practice'
	print Solution().shortestDistance(words, word1, word2)