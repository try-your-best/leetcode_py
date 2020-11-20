from common.utils import *

import heapq


class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		self._k = k
		self._min_heap = []
		for n in nums:
			self.add(n)

	def add(self, val: int) -> int:
		heapq.heappush(self._min_heap, val)
		if self._k < len(self._min_heap):
			heapq.heappop(self._min_heap)
		return self._min_heap[0]


if __name__ == '__main__':
	sl = KthLargest(3, [4, 5, 8, 2])
	print(sl.add(3))
	print(sl.add(5))
	print(sl.add(10))
	print(sl.add(9))
	print(sl.add(4))