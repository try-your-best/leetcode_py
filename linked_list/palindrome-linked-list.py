from common.utils import *


class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		dummy = ListNode(None)
		dummy.next = head
		fast = dummy
		slow = dummy
		stack = []

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			stack.append(slow.val)

		if not fast:
			stack.pop()

		while slow.next:
			slow = slow.next
			if stack.pop() != slow.val:
				return False
		return True


if __name__ == '__main__':
	sl = Solution()
	print(sl.isPalindrome(genLinkList([1, 2])))
	print(sl.isPalindrome(genLinkList([1, 2, 2, 2, 1])))


