# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		self._walk(root, 0)
		return root

	def _walk(self, root: TreeNode, cur_sum: int):
		if root is None:
			return cur_sum
		if root.right:
			cur_sum = self._walk(root.right, cur_sum)
		root.val += cur_sum
		cur_sum = root.val
		if root.left:  # 注意，左节点的 sum 也是有用的，看 test2
			cur_sum = self._walk(root.left, root.val)
		return cur_sum


def test1():
	sl = Solution()
	a = TreeNode(2)
	b = TreeNode(0)
	c = TreeNode(3)
	d = TreeNode(-4)
	e = TreeNode(1)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	s = sl.convertBST(a)
	pass


def test2():
	"""
	[1,0,4,-2,null,3]
	1
	0，4
	-2，null， 3
	[8,8,4,6,null,7]
	"""
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(0)
	c = TreeNode(4)
	d = TreeNode(-2)
	e = TreeNode(3)
	a.left = b
	a.right = c
	b.left = d
	c.left = e
	printTreeByLevelWalk(a)
	s = sl.convertBST(a)
	printTreeByLevelWalk(s)
	pass

if __name__ == '__main__':
	test2()