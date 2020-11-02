# -*- coding: utf-8 -*-

from common.utils import NTreeNode


def getNodePath(pRoot, pNode, nodePath):
	"""
	主要思想是先序遍历
	"""
	if pRoot == pNode:
		# nodePath 中只添加 parent
		return True

	nodePath.append(pRoot)

	isFound = False
	for node in pRoot.children:
		if node:
			isFound = getNodePath(node, pNode, nodePath)
			if isFound:
				break

	if not isFound:
		nodePath.pop()

	return isFound


def getLastCommonNode(nodePath1, nodePath2):
	lastCommon = None
	for node1, node2 in zip(nodePath1, nodePath2):
		if node1 == node2:
			lastCommon = node1
		else:
			break

	return lastCommon


def getLastCommonParent(pRoot, pNode1, pNode2):
	if not pRoot or not pNode1 or not pNode2:
		return None

	nodePath1 =[]
	isFound = getNodePath(pRoot, pNode1, nodePath1)
	if not isFound:
		return None

	nodePath2 =[]
	isFound = getNodePath(pRoot, pNode2, nodePath2)
	if not isFound:
		return None

	return getLastCommonNode(nodePath1, nodePath2)


if __name__ == "__main__":
	a1 = NTreeNode(1)
	a2 = NTreeNode(2)
	a3 = NTreeNode(3)
	a4 = NTreeNode(4)
	a5 = NTreeNode(5)
	a6 = NTreeNode(6)

	a1.children = [a2, a3]
	a2.children = [a4, a5]

	print getLastCommonParent(a1, a4, a3)
	print getLastCommonParent(a1, a4, a5)
	print getLastCommonParent(a1, a4, a6)
	print getLastCommonParent(a1, a4, a1)



