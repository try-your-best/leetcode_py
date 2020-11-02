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


if __name__ == '__main__':
	sl = Solution()
	# print(sl.rotateRight(genLinkList([1,2,3,4,5]),2))
	print(sl.rotateRight(genLinkList([0,1,2]), 4))
