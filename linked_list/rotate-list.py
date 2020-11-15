# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head:
			return head

		cur = head
		n = 0
		while cur:
			n += 1
			cur = cur.next

		k %= n

		slow = head
		fast = head
		i = 0
		while i < k and fast:
			fast = fast.next
			i += 1

		if not fast:
			return head

		while fast.next:
			fast = fast.next
			slow = slow.next

		fast.next = head
		fast = slow.next
		slow.next = None
		return fast


class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if head is None:
			return head
		dummy = ListNode(None)
		dummy.next = head
		list_len = 0
		fast = dummy
		while fast.next is not None:
			list_len += 1
			fast = fast.next

		if list_len == 1:
			return head

		k_step = k % list_len
		if k_step == 0:
			return dummy.next

		fast = dummy
		slow = dummy
		for i in range(k_step):
			fast = fast.next

		while fast.next is not None:
			fast = fast.next
			slow = slow.next

		fast.next = dummy.next
		dummy.next = slow.next
		slow.next = None

		return dummy.next

if __name__ == '__main__':
	sl = Solution()
	# print(sl.rotateRight(genLinkList([1,2,3,4,5]),2))
	print(sl.rotateRight(genLinkList([0,1,2]), 4))
	print(sl.rotateRight(genLinkList([]), 0))
