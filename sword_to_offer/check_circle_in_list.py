# -*- coding: utf-8 -*-

"""
判断一个单向链表是否形成了环形结构。
思路：定义两指针，一个指针一次走一步，另外一个一次走两步，
如果快的指针追上慢的，则链表形成环，如果快的走到了链表末尾都没有追上，则链表无环！
"""

from kth_node_from_end import ListNode


def checkCircleInList(pHead):
	if pHead is None:
		return False

	dummy = ListNode(0, pHead)  # 借助虚拟头节点，简化处理
	pFast = dummy
	pSlow = dummy

	while pFast is not None and pFast.pNext is not None:
		pFast = pFast.pNext
		pFast = pFast.pNext
		pSlow = pSlow.pNext
		if id(pFast) == id(pSlow):
			return True

	return False


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	a1.pNext = a2
	a2.pNext = a3
	a3.pNext = a4
	print checkCircleInList(a1)
	a4.pNext = a3
	print checkCircleInList(a1)