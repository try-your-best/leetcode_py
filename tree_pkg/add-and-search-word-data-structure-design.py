# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
Trie, DFS

Time:  O(min(n, h)), per operation
Space: O(min(n, h))
"""


from common.utils import TrieNode


class WordDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def addWord(self, word: str):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: None
		"""
		cur = self.root
		for w in word:
			if w not in cur.leaves:
				cur.leaves[w] = TrieNode()
			cur = cur.leaves[w]
		cur.is_string = True

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		return self._searchChild(self.root, word, 0)

	def _searchChild(self, node, word, word_idx):
		"""这里 node 代表 word[word_idx] 的父节点"""
		if len(word) == word_idx:
			return node.is_string

		w = word[word_idx]
		if w == ".":
			for cur in node.leaves.values():
				if self._searchChild(cur, word, word_idx+1):
					return True
			return False
		else:
			if w in node.leaves:
				return self._searchChild(node.leaves[w], word, word_idx+1)
			else:
				return False


if __name__ == "__main__":
	wd = WordDictionary()

	wd.addWord("bad")
	wd.addWord("dad")
	wd.addWord("mad")

	print(wd.search("pad"))  # false
	print(wd.search("bad"))  # true
	print(wd.search(".ad"))  # true
	print(wd.search("b.."))  # true