# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


# Time:  O(n)
# Space: O(n)
# Counting sort.
class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		n = len(citations)
		count = [0] * (n+1)

		for x in citations:
			if x >= n:
				count[n] += 1
			else:
				count[x] += 1

		h = 0
		for idx in xrange(n, 0, -1):
			h += count[idx]
			if h >= idx:
				return idx

		return 0

# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations.sort(reverse=True)
		h = 0
		for x in citations:
				if x >= h + 1:
						h += 1
				else:
						break
		return h


if __name__ == "__main__":
	citations = [3, 0, 6, 1, 5]
	# print Solution().hIndex(citations)
	print Solution2().hIndex(citations)