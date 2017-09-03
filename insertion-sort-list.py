# -*- coding: utf-8 -*-


class ListNode(object):

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))
		else:
			return "Nil"


class Solution(object):

	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		dummy = ListNode(0)

		while head:
			temp = dummy
			next = head.next

			while temp.next and temp.next.val < head.val:
				temp = temp.next

			head.next = temp.next
			temp.next = head
			head = next

		return dummy.next


# 思想是 mergesort， 参考 https://siddontang.gitbooks.io/leetcode-solution/content/linked_list/sort_list.html
class Solution2(object):

	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
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


if __name__ == "__main__":
	head = ListNode(3)
	head.next = ListNode(5)
	head.next.next = ListNode(1)
	# print Solution().sortList(head)
	print Solution2().sortList(head)
