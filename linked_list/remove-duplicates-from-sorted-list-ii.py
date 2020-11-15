from common.utils import *


class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return head

		dummy = ListNode(None)
		dummy.next = head
		cur = dummy
		while cur.next and cur.next.next:
			p1 = cur.next
			p2 = cur.next.next
			if p1.val != p2.val:
				cur = cur.next
			else:
				while p1.val == p2.val and p2.next:
					p2 = p2.next
				if p1.val != p2.val:
					cur.next = p2
				else:
					cur.next = None

		return dummy.next


if __name__ == '__main__':
	sl = Solution()
	print(sl.deleteDuplicates(genLinkList([1, 1, 2, 3])))