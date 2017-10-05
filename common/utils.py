# -*- coding: utf-8 -*-


class TreeNode(object):

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class NTreeNode(object):

	def __init__(self, value):
		self.value = value
		self.children = []

	def __repr__(self):
		return 'TNode({})'.format(self.value)


def printList(pHead):
	values = []
	while pHead:
		values.append(pHead.value)
		pHead = pHead.pNext
	print values