from common.utils import *


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		n = 0
		for m in nums:
			n = n ^ m
		return n


if __name__ == '__main__':
	sl = Solution()
	print(sl.singleNumber([2,2,1]))
	print(sl.singleNumber([4,1,2,1,2]))
	print(sl.singleNumber([1]))