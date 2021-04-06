# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

"""
https://www.cnblogs.com/grandyang/p/4781203.html

Given an array of citations (each citation is a non-negative integer)
of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have
at least h citations each, and the other N − h papers have
no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5],
which means the researcher has 5 papers in total
and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and
the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


from common.utils import *

# Time:  O(n)
# Space: O(n)
# Counting sort.
class Solution:
	def hIndex(self, citations: List[int]) -> int:
		"""
		:type citations: List[int]
		:rtype: int
		"""
		# 这里排的是论文数
		# 注意，这里做了优化，是 len(citations)， 而不是 max（citations）
		n = len(citations)
		count = [0] * (n+1)

		for x in citations:
			if x >= n:
				count[n] += 1
			else:
				count[x] += 1

		h = 0
		for idx in range(n, 0, -1):
			h += count[idx]
			if h >= idx:
				return idx

		return 0

# Time:  O(nlogn)
# Space: O(1)


class Solution:
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations.sort(reverse=True)  # 这里排的是引用数
		h = 0
		for x in citations:
				if x >= h + 1:
						h += 1
				else:
						break
		return h


Main = Solution

if __name__ == "__main__":
	citations = [3, 0, 6, 1, 5]
	citations = [6, 5, 3, 1, 0]
	sl = Main()
	# print Solution().hIndex(citations)
	print(sl.hIndex(citations))