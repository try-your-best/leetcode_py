# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import TreeNode


class Solution(object):

	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		vals = []
		self._preOrder(root, vals)
		return vals

	def _preOrder(self, node, vals):
		if node is None:
			return

		vals.append(node.val)
		self._preOrder(node.left, vals)
		self._preOrder(node.right, vals)


if __name__ == '__main__':
	sl = Solution()

	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	a.right = b
	b.left = c

	print(sl.preorderTraversal(a))
