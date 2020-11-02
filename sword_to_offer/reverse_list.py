# -*- coding: utf-8 -*-

"""
第16题，反转链表
思路： 要用三个指针去遍历， pNode 和 pPrev 跨栈传递, pNext 栈中新建
"""

from common.utils import printList
from kth_node_from_end import ListNode


def reverseList(pHead):
	pNode = pHead
	pPrev = None
	pNewHead = None

	while pNode is not None:
		pNext = pNode.pNext
		if pNext is None:
			pNewHead = pNode

		pNode.pNext = pPrev
		pPrev = pNode
		pNode = pNext

	return pNewHead


def reverseListRecurse(pNode, pPrev):
	if pNode is None:
		return None

	pNext = pNode.pNext
	pNode.pNext = pPrev
	if pNext is None:
		return pNode
	else:
		return reverseListRecurse(pNext, pNode)


def reverseList2(pHead):
	return reverseListRecurse(pHead, None)


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	a1.pNext = a2
	# a2.pNext = a3
	# a3.pNext = a4
	printList(a1)
	# printList(reverseList(a1))
	printList(reverseList2(a1))
