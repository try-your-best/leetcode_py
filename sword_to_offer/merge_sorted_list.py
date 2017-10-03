# -*- coding: utf-8 -*-


from kth_node_from_end import ListNode
from reverse_list import printList


def mergeSortedList(pHead1, pHead2):
	if pHead1 is None:
		return pHead2
	elif pHead2 is None:
		return pHead1

	# pNewHead = None

	if pHead1.value <= pHead2.value:
		pNewHead = pHead1
		pNewHead.pNext = mergeSortedList(pHead1.pNext, pHead2)
	else:
		pNewHead = pHead2
		pNewHead.pNext = mergeSortedList(pHead1, pHead2.pNext)

	return pNewHead


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(3)
	a3 = ListNode(5)
	a4 = ListNode(7)
	a1.pNext = a2
	a2.pNext = a3
	a3.pNext = a4

	b1 = ListNode(2)
	b2 = ListNode(3)
	b3 = ListNode(4)
	b4 = ListNode(6)
	b1.pNext = b2
	b2.pNext = b3
	b3.pNext = b4

	# printList(mergeSortedList(a1, b1))
	printList(mergeSortedList(a1, None))




