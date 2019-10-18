# -*- coding: utf-8 -*-

# Time:  O(n), per operation
# Space: O(1)

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()


	def insert(self, word):
		"""
		Inserts a word into the trie.
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
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		node = self.childSearch(word)
		if node is not None:
			return node.is_string
		else:
			return False

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		return self.childSearch(prefix) is not None

	def childSearch(self, word):
		cur = self.root
		for w in word:
			if w not in cur.leaves:
				return None
			cur = cur.leaves[w]

		return cur

# Your Trie object will be instantiated and called as such:
trie = Trie();

trie.insert("apple");
print trie.search("apple");   # returns true
print trie.search("app");     # returns false
print trie.startsWith("app"); # returns true
trie.insert("app");
print trie.search("app");     # returns true