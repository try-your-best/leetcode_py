# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/5237170.html
Time:  O(h)
Space: O(1)
"""

from common.utils import *


class Solution(object):
	def closestValue(self, root: TreeNode, target:float) -> int:
		return self._closestValue(root, target)

	def _closestValue(self, root: TreeNode, target: float) -> int:
		if not root:
			return None
		a = root.val
		node = root.left if target < a else root.right
		if not node:
			return a
		b = self._closestValue(node, target)
		return a if abs(a - target) < abs(b - target) else b


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
	print(sl.closestValue(a, 1.2))
	print(sl.closestValue(a, 1.6))