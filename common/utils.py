# -*- coding: utf-8 -*-

from typing import List, Set

class TreeNode(object):

	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.val)
# class TreeNode(object):
#
# 	def __init__(self, value, left=None, right=None):
# 		self.val = value
# 		self.left = left
# 		self.right = right


class NTreeNode(object):

	def __init__(self, value):
		self.value = value
		self.children = []

	def __repr__(self):
		return 'TNode({})'.format(self.value)


class TrieNode(object):
	# Initialize your data structure here.
	def __init__(self):
		self.is_string = False
		self.leaves = {}


def printList(pHead):
	values = []
	while pHead:
		values.append(pHead.value)
		pHead = pHead.pNext
	print(values)


def convertTree2LevelWalkList(root: TreeNode):
	queue = [root]
	ret = []

	while queue:
		cur = queue.pop(0)
		if cur is None:
			ret.append(None)
		else:
			ret.append(cur.val)
			queue.append(cur.left)
			queue.append(cur.right)
	return ret


def printTreeByLevelWalk(root:TreeNode):
	ret = convertTree2LevelWalkList(root)
	n = len(ret)-1
	while n >= 0 and ret[n] is None:
		n -= 1
	print(ret[0:n+1])


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))
		else:
			return "Nil"


def genLinkList(vals):
	root = ListNode(vals[0])
	a = root
	for i in range(1, len(vals)):
		a.next = ListNode(vals[i])
		a = a.next
	return root

def printListNode(head:ListNode):
	ret = []
	while head:
		ret.append(str(head.val))
		head = head.next
	print('->'.join(ret))