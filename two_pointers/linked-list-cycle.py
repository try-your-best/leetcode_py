# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
这道题是快慢指针的经典应用。只需要设两个指针，一个每次走一步的慢指针和一个每次走两步的快指针，
如果链表里有环的话，两个指针最终肯定会相遇。实在是太巧妙了，要是我肯定想不出来
"""

class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		fast = head
		slow = head

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

			if slow is fast:
				return True

		return False


if __name__ == '__main__':
	sl = Solution()

	a = ListNode(3)
	b = ListNode(2)
	c = ListNode(0)
	d = ListNode(4)
	a.next = b
	b.next = c
	c.next = d
	d.next = b

	print(sl.hasCycle(a))