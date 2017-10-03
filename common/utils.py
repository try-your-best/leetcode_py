# -*- coding: utf-8 -*-


class TreeNode(object):

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def printList(pHead):
	values = []
	while pHead:
		values.append(pHead.value)
		pHead = pHead.pNext
	print values