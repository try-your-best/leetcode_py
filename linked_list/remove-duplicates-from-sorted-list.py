from common.utils import *


class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return head
		dummy = ListNode(None)
		dummy.next = head
		cur = head
		while cur.next:
			next = cur.next
			while cur.val == next.val and next.next:
				next = next.next

			if cur.val != next.val:
				cur.next = next
				cur = next
			else:
				cur.next = None

		return dummy.next


if __name__ == '__main__':
	sl = Solution()
	print(sl.deleteDuplicates(genLinkList([1, 1, 2])))
	print(sl.deleteDuplicates(genLinkList([1, 1, 2, 3, 3])))