from common.utils import *

"""
利用 1 ≤ a[i] ≤ n ，把是否发现的信息藏在 a[a[i]-1] 中，取个反号
https://www.cnblogs.com/grandyang/p/6209746.html
"""

class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		for i in range(0, len(nums)):
			idx = abs(nums[i]) - 1 #  注意取 abs，得到原值
			if nums[idx] > 0:
				nums[idx] = -nums[idx]

		res = []

		for i in range(0, len(nums)):
			if nums[i] > 0:
				res.append(i+1)

		return res


if __name__ == '__main__':
	sl = Solution()
	print(sl.findDisappearedNumbers([4,3,2,7,8,2,3,1]))