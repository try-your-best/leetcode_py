# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4620012.html
"""

class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		self.k = k
		return self._kthSmallest(root)

	def _kthSmallest(self, root: TreeNode) -> int:
		if not root:
			return -1
		val = self._kthSmallest(root.left)
		if self.k == 0:
			return val
		self.k -= 1
		if self.k == 0:
			return root.val
		return self._kthSmallest(root.right)


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(3)
	b = TreeNode(1)
	c = TreeNode(4)
	d = TreeNode(2)
	a.left = b
	a.right = c
	b.right = d
	printTreeByLevelWalk(a)
	print(sl.kthSmallest(a, 1))
	print(sl.kthSmallest(a, 2))