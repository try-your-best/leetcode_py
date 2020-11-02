# -*- coding: utf-8 -*-

"""
25题
"""

from common.utils import TreeNode


def findPath(pRoot, expectedSum):
	if pRoot is None:
		return
	findPathCore(pRoot, expectedSum, [], 0)
	pass


def findPathCore(pRoot, expectedSum, path, curSum):
	curSum += pRoot.value
	path.append(pRoot.value)

	if pRoot.left is None and pRoot.right is None:
		if curSum == expectedSum:
			print path
	else:
		if pRoot.left is not None:
			findPathCore(pRoot.left, expectedSum, path, curSum)

		if pRoot.right is not None:
			findPathCore(pRoot.right, expectedSum, path, curSum)

	path.pop()


if __name__ == "__main__":
	a1 = TreeNode(10)
	a2 = TreeNode(5)
	a3 = TreeNode(12)
	a4 = TreeNode(4)
	a5 = TreeNode(7)

	a1.left = a2
	a1.right = a3
	a2.left = a4
	a2.right = a5

	findPath(a1, 22)


