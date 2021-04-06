from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4741122.html
"""


class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		n = 0
		for v in nums:
			n ^= v
		for i in range(32):
			if (n >> i) & 1 == 1:
				break
		val1 = 0
		val2 = 0
		mask = 1 << i
		for v in nums:
			if v & mask == mask:
				val1 ^= v
			else:
				val2 ^= v
		return [val1, val2]


class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		n = 0
		for v in nums:
			n ^= v
		for i in range(32):
			if (n >> i) & 1 == 1:
				break
		val1 = 0
		val2 = 0
		mask = 1 << i
		for v in nums:
			if (v >> i) & 1 == 1:
				val1 ^= v
			else:
				val2 ^= v
		return [val1, val2]


if __name__ == '__main__':
	sl = Solution()
	print(sl.singleNumber([1,2,1,3,2,5]))
	# print(sl.singleNumber([-1,0]))
	# print(sl.singleNumber([1,0]))
