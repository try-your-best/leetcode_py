# -*- coding: utf-8 -*-
__author__ = 'damon'


"""
https://www.cnblogs.com/grandyang/p/5187041.html
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class Solution(object):
	def shortestDistance(self, words, word1, word2):
		w1_idx = []
		w2_idx = []
		for idx, w in enumerate(words):
			if w == word1:
				w1_idx.append(idx)
			elif w == word2:
				w2_idx.append(idx)

		min_dist = len(words)

		for n1 in w1_idx:
			for n2 in w2_idx:
				min_dist = min(min_dist, abs(n1-n2))

		return min_dist


"""可以不用遍历所有位置的差值，利用从左到右遍历，利用位置关系，可以节省一些计算"""
class Solution(object):
	def shortestDistance(self, words, word1, word2):
		min_dist = len(words)
		w1_idx = None
		w2_idx = None
		for idx, w in enumerate(words):
			flag = False
			if w == word1:
				w1_idx = idx
				flag = True
			elif w == word2:
				w2_idx = idx
				flag = True

			if flag and w1_idx is not None and w2_idx is not None:
				min_dist = min(min_dist, abs(w1_idx - w2_idx))

		return min_dist


class Solution(object):
	def shortestDistance(self, words, word1, word2):
		p1 = None
		p2 = None
		w_len = len(words)
		min_dis = w_len
		for idx, w in enumerate(words):
			flag = False
			if w == word1:
				p1 = idx
				flag = True
			elif w == word2:
				p2 = idx
				flag = True

			if flag and p1 is not None and p2 is not None:
				min_dis = min(min_dis, abs(p1-p2))

		return min_dis


if __name__ == '__main__':
	sl = Solution()
	print(sl.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
	print(sl.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))

