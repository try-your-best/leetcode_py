# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def middleNode(self, head: ListNode) -> ListNode:
		dummy = ListNode(-1)
		dummy.next = head
		slow = dummy
		fast = dummy

		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next

		return slow.next


if __name__ == '__main__':
	sl = Solution()
	print(sl.middleNode(genLinkList([1, 2, 3, 4, 5])))