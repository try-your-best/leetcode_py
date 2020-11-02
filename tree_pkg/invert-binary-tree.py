# -*- coding: utf-8 -*-

from common.utils import TreeNode

"""
Time:  O(n)
Space: O(h)
DFS, Recursive solution.
"""


class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root is None:
			return None

		root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

		return root


