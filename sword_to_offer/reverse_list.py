# -*- coding: utf-8 -*-


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


def printList(pHead):
	values = []
	while pHead:
		values.append(pHead.value)
		pHead = pHead.pNext
	print values


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	a1.pNext = a2
	a2.pNext = a3
	a3.pNext = a4
	printList(a1)
	printList(reverseList(a1))
