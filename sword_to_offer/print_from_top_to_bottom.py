# -*- coding: utf-8 -*-

from collections import deque
from common.utils import TreeNode


def printFromTopToBottom(pNode):
	if pNode is None:
		return

	nodeQueue = deque()
	nodeQueue.append(pNode)

	while nodeQueue:
		pCur = nodeQueue.popleft()
		print pCur.value

		if pCur.left is not None:
			nodeQueue.append(pCur.left)

		if pCur.right is not None:
			nodeQueue.append(pCur.right)


if __name__ == "__main__":
	a1 = TreeNode(1)
	a2 = TreeNode(2)
	a3 = TreeNode(3)
	a4 = TreeNode(4)
	a5 = TreeNode(5)

	a1.left = a2
	a1.right = a3
	a2.left = a4
	a2.right = a5

	printFromTopToBottom(a1)