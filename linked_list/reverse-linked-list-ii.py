from common.utils import *


class Solution:
	def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
		if not head or m == n:
			return head

		dummy = ListNode(None)
		dummy.next = head
		pre = dummy
		cur = head
		idx = 1
		start_pre = None
		start_cur = None
		reverse = False

		while cur:
			# print("a", cur.val)
			if idx == m:
				start_pre = pre
				start_cur = cur

				next = cur.next
				pre = cur
				cur = next
				reverse = True
			elif idx == n:
				start_pre.next = cur
				start_cur.next = cur.next
				cur.next = pre
				break
			else:
				if reverse:
					next = cur.next
					cur.next = pre
					pre = cur
					cur = next
				else:
					next = cur.next
					pre = cur
					cur = next

			idx += 1

		return dummy.next


if __name__ == '__main__':
	sl = Solution()
	# print(sl.reverseBetween(genLinkList([1,2,3,4,5]), 2, 4))
	# print(sl.reverseBetween(genLinkList([3,5]), 1, 2))
	print(sl.reverseBetween(genLinkList([3,5]), 1, 1))