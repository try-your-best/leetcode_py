# -*- coding: utf-8 -*-


class ListNode(object):

	def __init__(self, value, pNext=None):
		self.value = value
		self.pNext = pNext

	def __repr__(self):
		return str(self.value)


def findKthToTail(pHead, k):
	if pHead is None or k <= 0:
		return None

	pAhead = pHead

	for _ in xrange(k-1):
		if pAhead.pNext is not None:
			pAhead = pAhead.pNext
		else:
			return None

	pBehind = pHead

	while pAhead.pNext is not None:
		pAhead = pAhead.pNext
		pBehind = pBehind.pNext

	return pBehind


if __name__ == '__main__':
	a1 = ListNode(1)
	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	a1.pNext = a2
	a2.pNext = a3
	a3.pNext = a4

	print findKthToTail(a1, 1)
	print findKthToTail(a1, 4)
	print findKthToTail(a1, 5)
	print findKthToTail(a1, 0)
	print findKthToTail(None, 1)
