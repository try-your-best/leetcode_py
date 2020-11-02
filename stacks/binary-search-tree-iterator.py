# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
注意空间复杂度要求是 O(h)
"""


class BSTIterator:

	def __init__(self, root: TreeNode):
		self.stack = []
		# self._walk(root)
		while root:
			self.stack.append(root)
			root = root.left

	def next(self) -> int:
		"""
		@return the next smallest number
		"""
		top = self.stack.pop()
		root = top.right
		while root:
			self.stack.append(root)
			root = root.left
		return top.val

	def hasNext(self) -> bool:
		"""
		@return whether we have a next smallest number
		"""
		return bool(self.stack)


if __name__ == '__main__':
	a = TreeNode(7)
	b = TreeNode(3)
	c = TreeNode(15)
	d = TreeNode(9)
	e = TreeNode(20)
	a.left = b
	a.right = c
	c.left = d
	c.right = e

	iterator = BSTIterator(a);
	print(iterator.next())    # return 3
	print(iterator.next())    # return 7
	print(iterator.hasNext()) # return true
	print(iterator.next())    # return 9
	print(iterator.hasNext()) # return true
	print(iterator.next())   # return 15
	print(iterator.hasNext()) # return true
	print(iterator.next())   # return 20
	print(iterator.hasNext()) # return false