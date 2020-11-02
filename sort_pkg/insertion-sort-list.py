# -*- coding: utf-8 -*-
__author__ = 'damon'


from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4250107.html
链表的插入排序实现原理很简单，就是一个元素一个元素的从原链表中取出来，然后按顺序插入到新链表中，时间复杂度为 O(n2)，是一种效率并不是很高的算法，但是空间复杂度为 O(1)，以高时间复杂度换取了低空间复杂度
"""

class Solution:
	def insertionSortList(self, head: ListNode) -> ListNode:
		dummy = ListNode(None)
		while head:
			next_head = head.next
			cur = dummy
			while cur.next and cur.next.val <= head.val:
				cur = cur.next

			head.next = cur.next
			cur.next = head

			head = next_head

		return dummy.next


if __name__ == "__main__":
	sl = Solution()
	a = ListNode(4)
	b = ListNode(2)
	c = ListNode(1)
	d = ListNode(3)
	a.next = b
	b.next = c
	c.next = d
	print(a)
	print(sl.insertionSortList(a))

