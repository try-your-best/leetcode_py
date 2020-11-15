# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		dummy = ListNode(None)

		cur = dummy
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next

			cur = cur.next

		if l1:
			cur.next = l1

		if l2:
			cur.next = l2

		return dummy.next


class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		dummy = ListNode(None)
		cur = dummy
		l1_p = l1
		l2_p = l2

		while l1_p is not None and l2_p is not None:
			if l1_p.val < l2_p.val:
				cur.next = l1_p
				l1_p = l1_p.next
			else:
				cur.next = l2_p
				l2_p = l2_p.next
			cur = cur.next
		if l1_p is not None:
			cur.next = l1_p
		if l2_p is not None:
			cur.next = l2_p

		return dummy.next


if __name__ == '__main__':
	sl = Solution()
	l1 = genLinkList([1, 2, 4])
	l2 = genLinkList([1, 3, 4])
	# print(l1)
	# print(l2)
	print(sl.mergeTwoLists(l1, l2))