# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root: return True
		return self._isSymmetric(root.left, root.right)

	def _isSymmetric(self, left:TreeNode, right:TreeNode):
		if not left and not right: return True
		if (left and not right) or (not left and right) or (left.val != right.val): return False
		return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)


class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root: return True
		left_stack = [root.left]
		right_stack = [root.right]
		while left_stack and right_stack:
			left = left_stack.pop()
			right = right_stack.pop()
			if not left and not right:
				continue
			if (left and not right) or (not left and right) or (left.val != right.val): return False
			left_stack.append(left.right)
			right_stack.append(right.left)

			left_stack.append(left.left)
			right_stack.append(right.right)

		return not left_stack and not right_stack


def func1():
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(2)
	d = TreeNode(3)
	e = TreeNode(3)
	g = TreeNode(4)
	f = TreeNode(4)
	a.left = b
	a.right = c
	b.left = d
	b.right = g
	c.left = f
	c.right = e
	print(sl.isSymmetric(a))


def func2():
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(2)
	d = TreeNode(3)
	e = TreeNode(3)
	a.left = b
	a.right = c
	b.right = d
	c.right = e
	print(sl.isSymmetric(a))


if __name__ == '__main__':
	func1()
	func2()
