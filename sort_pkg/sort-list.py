# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

class Solution:
	def sortList(self, head: ListNode) -> ListNode:
		if head is None or head.next is None:
			return head

		fast = head
		slow = head

		# 快慢指针得到中间点
		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next

		# 将链表拆成两半
		fast = slow.next
		slow.next = None

		# 左右两半分别排序
		p1 = self.sortList(head)
		p2 = self.sortList(fast)

		# 合并
		return self.merge(p1, p2)

	def merge(self, p1, p2):
		if p1 is None:
			return p2
		elif p2 is None:
			return p1

		dummy = ListNode(0)
		cur = dummy

		while p1 and p2:
			if p1.val <= p2.val:
				cur.next = p1
				p1 = p1.next
			else:
				cur.next = p2
				p2 = p2.next

			cur = cur.next

		if p1:
			cur.next = p1
		else:
			cur.next = p2

		return dummy.next