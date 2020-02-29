# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def minDiffInBST(self, root: TreeNode) -> int:
		self._min_dist = float('inf')
		self._pre = None
		self._inorder(root)
		return self._min_dist

	def _inorder(self, root: TreeNode):
		if not root:
			return None
		self._inorder(root.left)
		if self._pre is not None:
			self._min_dist = min(self._min_dist, root.val - self._pre)
		self._pre = root.val
		self._inorder(root.right)


def func1():
	"""[4,2,6,1,3,null,null]"""
	a = TreeNode(4)
	b = TreeNode(2)
	c = TreeNode(6)
	d = TreeNode(1)
	e = TreeNode(3)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	printTreeByLevelWalk(a)
	sl = Solution()
	print(sl.minDiffInBST(a))


if __name__ == '__main__':
	func1()