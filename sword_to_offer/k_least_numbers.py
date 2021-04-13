# -*- coding: utf-8 -*-

"""
熟悉 heapq 的使用
"""


import heapq

class MaxHeap(object):

	def __init__(self):
		self._data = []

	def heappush(self, value):
		heapq.heappush(self._data, -value)

	def heappop(self):
		return - heapq.heappop(self._data)

	def size(self):
		return len(self._data)

	def top(self):
		return - self._data[0]

	def data(self):
		return [- num for num in self._data]


def getLeastNumbers(nums, k):

	if len(nums) <= k:
		return nums

	maxHeap = MaxHeap()

	for idx in range(k):
		maxHeap.heappush(nums[idx])

	for idx in range(k, len(nums)):
		num = nums[idx]
		if num < maxHeap.top():
			maxHeap.heappop()
			maxHeap.heappush(num)

	return maxHeap.data()


if __name__ == "__main__":
	print(getLeastNumbers([1, 2, 3, 4, 5, 6], 3))
	print(getLeastNumbers([1, 1, 1, 3], 2))
	print(getLeastNumbers([3, 2, 1], 4))



