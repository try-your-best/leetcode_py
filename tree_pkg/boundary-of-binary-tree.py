# -*- coding: utf-8 -*-
__author__ = 'damon'

# Time:  O(n)
# Space: O(h)

from common.utils import *


class Solution(object):
	def boundaryOfBinaryTree(self, root:TreeNode):
		res = []
		self._leftBoundary(root, res)
		self._leaves(root, res)
		self._rightBoundary(root.right, res) # 注意，这里不是从 root 出发
		return res

	def _leftBoundary(self, root:TreeNode, res:List):
		if not root or (not root.left and not root.right):
			return
		res.append(root.val)
		self._leftBoundary(root.left, res)

	def _rightBoundary(self, root:TreeNode, res:List):
		if not root or (not root.left and not root.right):
			return
		self._rightBoundary(root.right, res)
		res.append(root.val)

	def _leaves(self, root:TreeNode, res:List):
		if not root:
			return
		if not root.left and not root.right:
			res.append(root.val)

		self._leaves(root.left, res)
		self._leaves(root.right, res)


def test1():
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(4)
	a.right = b
	b.left = c
	b.right = d
	print(sl.boundaryOfBinaryTree(a))



if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(4)
	a.right = b
	b.left = c
	b.right = d
	print(sl.boundaryOfBinaryTree(a))