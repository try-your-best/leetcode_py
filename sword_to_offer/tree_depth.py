# -*- coding: utf-8 -*-

from common.utils import TreeNode


def treeDepth(pRoot):
	if pRoot is None:
		return 0
	left = treeDepth(pRoot.left)
	right = treeDepth(pRoot.right)
	return left+1 if left > right else right+1


if __name__ == "__main__":
	a1 = TreeNode(10)
	a2 = TreeNode(5)
	a3 = TreeNode(12)
	a4 = TreeNode(4)
	a5 = TreeNode(7)

	a1.left = a2
	print treeDepth(a1)
	a1.right = a3
	print treeDepth(a1)
	a2.left = a4
	a2.right = a5
	print treeDepth(a1)