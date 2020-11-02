# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4640572.html
"""

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		return self._lowestCommonAncestor(root, p, q)

	def _lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		print(root, p, q)
		if not root: return root
		if root.val > max(p.val, q.val):
			return self._lowestCommonAncestor(root.left, p, q)
		elif root.val < min(p.val, q.val):
			return self._lowestCommonAncestor(root.right, p, q)
		else:
			return root


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(6)
	b = TreeNode(2)
	c = TreeNode(8)
	d = TreeNode(0)
	e = TreeNode(4)
	f = TreeNode(7)
	g = TreeNode(9)
	h = TreeNode(3)
	i = TreeNode(5)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.left = f
	c.right = g
	e.left = h
	e.right = i
	printTreeByLevelWalk(a)
	# print(sl.lowestCommonAncestor(a, b, c))
	print(sl.lowestCommonAncestor(a, b, e))