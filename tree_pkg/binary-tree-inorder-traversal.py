# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import TreeNode


class Solution(object):

	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""

		vals = []
		self._inOrder(root, vals)
		return vals

	def _inOrder(self, node, vals):
		if node is None:
			return

		self._inOrder(node.left, vals)

		vals.append(node.val)

		self._inOrder(node.right, vals)


if __name__ == '__main__':
	sl = Solution()

	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	a.right = b
	b.left = c

	print(sl.inorderTraversal(a))