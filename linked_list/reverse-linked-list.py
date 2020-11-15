from common.utils import *


class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		if not head:
			return head
		pre = None
		cur = head

		while cur.next:
			next = cur.next
			cur.next = pre
			# print(cur)

			pre = cur
			cur = next

		cur.next = pre

		return cur


if __name__ == '__main__':
	sl = Solution()
	print(sl.reverseList(genLinkList([1,2,3,4,5])))