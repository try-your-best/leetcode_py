from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/6209746.html
"""

class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		res = []
		for i in range(len(nums)):
			idx = abs(nums[i]) - 1
			if nums[idx] < 0:
				res.append(idx+1)
			else:
				nums[idx] = - nums[idx]
		return res


if __name__ == '__main__':
	sl = Solution()
	print(sl.findDuplicates([4,3,2,7,8,2,3,1]))
