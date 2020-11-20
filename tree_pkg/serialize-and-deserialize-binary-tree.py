# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import TreeNode

"""
https://www.cnblogs.com/grandyang/p/4913869.html
"""

class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		vals = []
		self._serialize(root, vals)
		return "$".join(vals)

	def _serialize(self, node, vals):
		if node:
			vals.append(str(node.val))
			self._serialize(node.left, vals)
			self._serialize(node.right, vals)
		else:
			vals.append("#")

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		return self._deserialize(data.split("$"), [0])

	def _deserialize(self, data, idxs):
		if len(data) == idxs[0]:
			return None

		val = data[idxs[0]]
		idxs[0] += 1
		if val == "#":
			return None
		else:
			node = TreeNode(int(val))
			node.left = self._deserialize(data, idxs)
			node.right = self._deserialize(data, idxs)
			return node


if __name__ == '__main__':
	cd = Codec()

	a = TreeNode(-1)
	b = TreeNode(0)
	c = TreeNode(1)
	# d = TreeNode(4)
	# e = TreeNode(5)

	a.left = b
	a.right = c
	# c.left = d
	# c.right = e

	print(cd.serialize(a))
	print(cd.serialize(cd.deserialize(cd.serialize(a))))