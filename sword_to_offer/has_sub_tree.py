# -*- coding: utf-8 -*-

"""
树的子结构，第18题
"""


from common.utils import TreeNode


def hasSubTree(pRoot1, pRoot2):
	result = False

	if pRoot1 is not None and pRoot2 is not None:
		if pRoot1.value == pRoot2.value:
			result = isTree1HasTree2(pRoot1, pRoot2)
		if not result:
			result = hasSubTree(pRoot1.left, pRoot2)
		if not result:
			result = hasSubTree(pRoot1.right, pRoot2)

	return result


def isTree1HasTree2(pRoot1, pRoot2):
	if pRoot2 is None:
		return True
	if pRoot1 is None:
		return False
	if pRoot1.value != pRoot2.value:
		return False
	return isTree1HasTree2(pRoot1.left, pRoot2.left) and isTree1HasTree2(pRoot1.right, pRoot2.right)


if __name__ == "__main__":
	a1 = TreeNode(1)
	a2 = TreeNode(2)
	a3 = TreeNode(3)
	a4 = TreeNode(4)
	a5 = TreeNode(5)

	a1.left = a2
	a2.left = a3
	a3.left = a4
	a3.right = a5

	b1 = TreeNode(3)
	b2 = TreeNode(4)
	b3 = TreeNode(5)

	b1.left = b2
	b1.right = b3

	print hasSubTree(a1, b1)
