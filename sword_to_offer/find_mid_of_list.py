# -*- coding: utf-8 -*-

"""
求链表的中间节点
思路：定义两指针，一个指针一次走一步，另外一个一次走两步，
当快的指针到达链表结尾时，慢的指针正好到链表的中间！
"""

from kth_node_from_end import ListNode


def findMidOfList(pHead):
	if pHead is None:
		return None

	dummy = ListNode(0, pHead)  # 借助虚拟头节点，简化处理
	pFast = dummy
	pSlow = dummy

	while pFast is not None and pFast.pNext is not None:
		pFast = pFast.pNext
		pFast = pFast.pNext
		pSlow = pSlow.pNext

	return pSlow


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	print findMidOfList(a1)
	a1.pNext = a2
	print findMidOfList(a1)
	a2.pNext = a3
	print findMidOfList(a1)
	a3.pNext = a4
	print findMidOfList(a1)