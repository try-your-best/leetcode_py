from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/6208062.html
"""

class Solution:
	def totalHammingDistance(self, nums: List[int]) -> int:
		res = 0
		for i in range(32):
			cnt = 0
			n_len = len(nums)
			for n in nums:
				if n & (1 << i):
					cnt += 1
			res += cnt * (n_len - cnt)
		return res


if __name__ == '__main__':
	sl = Solution()
	print(sl.totalHammingDistance([4, 14, 2]))