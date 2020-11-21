from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4280131.html
只买卖一次，所以用当前值进去前面的最小值
"""

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		cur_min = float('inf')
		for p in prices:
			cur_min = min(cur_min, p)
			max_profit = max(max_profit, p-cur_min)
		return max_profit


if __name__ == '__main__':
	sl = Solution()
	print(sl.maxProfit([7,1,5,3,6,4]))