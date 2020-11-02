# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def countNodes(self, root: TreeNode) -> int:
		if not root:
			return 0
		left_height = self._leftHeight(root)
		right_height = self._rightHeight(root)
		if left_height == right_height:
			return 2**left_height - 1
		return self.countNodes(root.left) + self.countNodes(root.right) + 1

	def _leftHeight(self, root: TreeNode) -> int:
		height = 0
		while root:
			height += 1
			root = root.left
		return height

	def _rightHeight(self, root: TreeNode) -> int:
		height = 0
		while root:
			height += 1
			root = root.right
		return height


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	a.left = b
	a.right = c
	print(sl.countNodes(a))