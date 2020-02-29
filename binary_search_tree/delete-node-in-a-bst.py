# -*- coding: utf-8 -*-
__author__ = 'damon'


from common.utils import *


# class Solution:
# 	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
# 		return self._findAndDeleteNode(root, None, False, key)
#
# 	def _findAndDeleteNode(self, root: TreeNode, parent: TreeNode, is_left: bool, key: int):
# 		if not root:
# 			return
# 		if key == root.val:
# 			# print(root, parent, is_left)
# 			node = self._deleteNode(root, parent, is_left)
# 			return node
# 		elif key < root.val:
# 			self._findAndDeleteNode(root.left, root, True, key)
# 		else:
# 			self._findAndDeleteNode(root.right, root, False, key)
# 		return root
#
# 	def _deleteNode(self, root: TreeNode, parent: TreeNode, is_left: bool):
# 		if root.left:
# 			node = root.left
# 			self._deleteNode(root.left, node, True)
# 			node.right = root.right
# 		elif root.right:
# 			node = root.right
# 			self._deleteNode(root.right, node, False)
# 			node.left = None
# 		else:
# 			node = None
#
# 		if parent:
# 			if is_left:
# 				parent.left = node
# 			else:
# 				parent.right = node
# 		return node


"""
https://www.cnblogs.com/grandyang/p/6228252.html
先来看一种递归的解法，首先判断根节点是否为空。由于 BST 的左<根<右的性质，使得可以快速定位到要删除的结点，对于当前结点值不等于 key 的情况，
根据大小关系对其左右子结点分别调用递归函数。若当前结点就是要删除的结点，先判断若有一个子结点不存在，就将 root 指向另一个结点，
如果左右子结点都不存在，那么 root 就赋值为空了，也正确。难点就在于处理左右子结点都存在的情况，需要在右子树找到最小值，即右子树中最左下方的结点，
然后将该最小值赋值给 root，然后再在右子树中调用递归函数来删除这个值最小的结点，参见代码如下：
"""

class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		return self._deleteNode(root, key)

	def _deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		if not root:
			return root
		if key < root.val:
			root.left = self._deleteNode(root.left, key)
		elif key > root.val:
			root.right = self._deleteNode(root.right, key)
		else:
			if not root.left or not root.right:
				root = root.left if root.left  else root.right
			else:
				cur = root.right
				while cur.left:
					cur = cur.left
				root.val = cur.val
				root.right = self._deleteNode(root.right, cur.val)

		return root


def func1():
	"""[5,3,6,2,4,null,7]"""
	a = TreeNode(5)
	b = TreeNode(3)
	c = TreeNode(6)
	d = TreeNode(2)
	e = TreeNode(4)
	f = TreeNode(7)
	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	printTreeByLevelWalk(a)
	sl = Solution()
	root = sl.deleteNode(a, 3)
	printTreeByLevelWalk(root)


def fun2():
	"""[3,1,4,null,2] 3 -> [4,1,null,null,2]"""
	a = TreeNode(3)
	b = TreeNode(1)
	c = TreeNode(4)
	d = TreeNode(2)
	a.left = b
	a.right = c
	b.right = d
	printTreeByLevelWalk(a)
	sl = Solution()
	root = sl.deleteNode(a, 3)
	printTreeByLevelWalk(root)


if __name__ == '__main__':
	fun2()