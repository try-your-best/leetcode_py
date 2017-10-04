# -*- coding: utf-8 -*-

"""
39题
"""


from common.utils import TreeNode


class TreeDepth(object):

	def __init__(self, value=0):
		self.value = value


def isBalanced(pRoot):
	return isBalancedCore(pRoot, TreeDepth())


"""
主要思想还是后顺序遍历
"""


def isBalancedCore(pRoot, treeDepth):
	if pRoot is None:
		treeDepth.value = 0
		return True

	left = TreeDepth()
	right = TreeDepth()

	if isBalancedCore(pRoot.left, left) and isBalancedCore(pRoot.right, right):
		if abs(left.value - right.value) <= 1:
			treeDepth.value = (left.value if left.value > right.value else right.value)+1
			return True

	return False

if __name__ == "__main__":
	a1 = TreeNode(10)
	a2 = TreeNode(5)
	a3 = TreeNode(12)
	a4 = TreeNode(4)
	a5 = TreeNode(7)

	a1.left = a2
	a2.left = a4
	a2.right = a5
	print isBalanced(a1)

	a1.right = a3
	print isBalanced(a1)