# -*- coding: utf-8 -*-

"""
27题
"""

from common.utils import TreeNode


class NodeRef(object):
	def __init__(self, node):
		self.node = node


def convertTree(pNode, pLastNodeInList):
	if pNode is None:
		return

	pCur = pNode

	if pCur.left is not None:
		convertTree(pCur.left, pLastNodeInList)

	pCur.left = pLastNodeInList.node
	if pLastNodeInList.node is not None:
		pLastNodeInList.node.right = pCur

	pLastNodeInList.node = pCur

	if pCur.right is not None:
		convertTree(pCur.right, pLastNodeInList)


def convert(pNode):
	pLastNodeInList = NodeRef(None)
	convertTree(pNode, pLastNodeInList)
	pNewHead = pLastNodeInList.node

	while pNewHead is not None and pNewHead.left is not None:
		pNewHead = pNewHead.left

	return pNewHead


def printList(pHead):
	values = []
	while pHead:
		values.append(pHead.value)
		pHead = pHead.right
	print values

if __name__ == "__main__":
	a1 = TreeNode(10)
	a2 = TreeNode(6)
	a3 = TreeNode(14)
	a4 = TreeNode(4)
	a5 = TreeNode(8)
	a6 = TreeNode(12)
	a7 = TreeNode(16)

	a1.left = a2
	a1.right = a3
	a2.left = a4
	a2.right = a5
	a3.left = a6
	a3.right = a7

	pHead = convert(a1)
	printList(pHead)

