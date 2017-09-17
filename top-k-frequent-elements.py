# -*- coding: utf-8 -*-

# Given a non-empty array of integers,
# return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid,
# 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better
# than O(n log n), where n is the array's size.


# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(n)

import collections
from heapq import nlargest


class Solution(object):

	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		counts = collections.defaultdict(int)
		for num in nums:
			counts[num] += 1

		numPairs = [(num, count) for num, count in counts.iteritems()]
		self.selectTopK(numPairs, k)
		return [numPair[0] for numPair in numPairs[:k]]

	def selectTopK(self, numPairs, k):
		def partition(ary, left, right):
			pivot = ary[right]
			i = left - 1

			for j in xrange(left, right):
				if ary[j][1] >= pivot[1]:
					i += 1
					ary[j], ary[i] = ary[i], ary[j]

			ary[i+1], ary[right] = ary[right], ary[i+1]

			return i+1

		left, right = 0, len(numPairs)-1
		index = partition(numPairs, left, right)

		while index != k-1:
			if index < k-1:
				left = index+1
			else:
				right = index-1
			index = partition(numPairs, left, right)


class Solution2(object):

	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		counts = collections.defaultdict(int)
		for num in nums:
			counts[num] += 1

		numPairs = [(num, count) for num, count in counts.iteritems()]
		topK = nlargest(k, numPairs, key=lambda x: x[1])
		return [numPair[0] for numPair in topK]


if __name__ == "__main__":
	nums = [1,1,1,2,2,3]
	nums = [1, 1, 6, 6, 3]
	# print Solution().topKFrequent(nums, 2)
	print Solution2().topKFrequent(nums, 2)