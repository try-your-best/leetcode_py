# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
这种表达就难看很多
"""
class Solution:
	def getMinimumDifference(self, root: TreeNode) -> int:
		self._min_diff = float('inf')
		self._inorder(root, None)
		return self._min_diff

	def _inorder(self, root: TreeNode, pre_val: int) -> int:
		if not root:
			return None
		left_val = self._inorder(root.left, pre_val)  # 还是要把 pre_val 传给 left
		if left_val is not None:
			pre_val = left_val
		if pre_val is not None:
			self._min_diff = min(self._min_diff, root.val - pre_val)
		pre_val = root.val
		right_val = self._inorder(root.right, pre_val)
		if right_val is not None:
			pre_val = right_val
		return pre_val

Main = Solution


class Solution:
	def getMinimumDifference(self, root: TreeNode) -> int:
		self._min_diff = float('inf')
		self._pre = None
		self._inorder(root)
		return self._min_diff

	def _inorder(self, root: TreeNode):
		if not root:
			return None
		self._inorder(root.left)
		if self._pre is not None:
			self._min_diff = min(self._min_diff, root.val - self._pre)
		self._pre = root.val
		self._inorder(root.right)

# Main = Solution

def func1():
	"""[0, null, 2236, 1277, 2776, 519]"""
	sl = Main()
	a = TreeNode(0)
	b = TreeNode(2236)
	c = TreeNode(1277)
	d = TreeNode(2776)
	e = TreeNode(519)
	a.right = b
	b.left = c
	b.right = d
	c.left = e
	printTreeByLevelWalk(a)
	print(sl.getMinimumDifference(a))

def func2():
	sl = Main()
	a = TreeNode(1)
	b = TreeNode(3)
	c = TreeNode(2)
	a.right = b
	b.left = c
	printTreeByLevelWalk(a)
	print(sl.getMinimumDifference(a))


if __name__ == '__main__':
	func1()