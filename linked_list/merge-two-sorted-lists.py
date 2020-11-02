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


if __name__ == '__main__':
	sl = Solution()
	print(sl.mergeTwoLists(genLinkList([1, 2, 4]), genLinkList([1, 3, 4])))