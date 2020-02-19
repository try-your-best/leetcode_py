# -*- coding: utf-8 -*-
__author__ = 'damon'


from common.utils import *


class Diameter:
	def __init__(self):
		self.val = 0


class Solution:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		res = Diameter()
		self._maxDepth(root, res)
		return res.val

	def _maxDepth(self, root: TreeNode, res: Diameter):
		if root is None:
			return 0
		left = self._maxDepth(root.left, res)
		right = self._maxDepth(root.right, res)
		res.val = max(res.val, left+right)
		return max(left, right) + 1


class Solution(object):
	def diameterOfBinaryTree(self, root):
		self.ans = 1
		def depth(node):
			if not node: return 0
			L = depth(node.left)
			R = depth(node.right)
			self.ans = max(self.ans, L+R+1)
			return max(L, R) + 1
		depth(root)
		return self.ans - 1


def test1():
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(4)
	e = TreeNode(5)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	print(sl.diameterOfBinaryTree(a))

def test2():
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(4)
	e = TreeNode(5)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	print(sl.diameterOfBinaryTree(a))

if __name__ == '__main__':
	test1()