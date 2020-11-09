from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4756677.html
"""

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		sum1 = n * (n+1) /2
		sum2 = sum(nums)
		return int(sum1-sum2)


class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		res = 0
		for i in range(len(nums)):
			res ^= (i+1) ^ nums[i]
		return res


"""
这是一种范式
"""
class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		nums = sorted(nums)
		# print(nums)
		left = 0
		right = len(nums)
		while left < right:
			mid = int((right + left) / 2)
			if nums[mid] > mid:
				right = mid
			else:
				left = mid + 1
		return right


if __name__ == '__main__':
	sl = Solution()
	print(sl.missingNumber([0,1]))
	print(sl.missingNumber([9,6,4,2,3,5,7,0,1]))
