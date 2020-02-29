# -*- coding: utf-8 -*-
__author__ = 'damon'


from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4997417.html
"""


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if not prices:
			return 0

		n = len(prices)
		buy = [0] * (n+1)
		sell = [0] * (n+1)

		buy[1] = -prices[0]
		sell[1] = 0

		for i in range(2, n+1):
			buy[i] = max(buy[i-1], sell[i-2]-prices[i-1])
			sell[i] = max(sell[i-1], buy[i-1]+prices[i-1])

		return sell[n]


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if not prices:
			return 0

		buy = 0
		pre_buy = -float('inf')
		sell = 0
		pre_sell = 0

		for price in prices:
			# buy[i] = max(buy[i-1], sell[i-2]-prices[i-1])
			# sell[i] = max(sell[i-1], buy[i-1]+prices[i-1])
			buy = max(pre_buy, pre_sell - price)
			pre_sell = sell
			sell = max(pre_sell, pre_buy + price)
			pre_buy = buy

		return sell


if __name__ == '__main__':
	sl = Solution()
	print(sl.maxProfit([1,2,3,0,2]))
	print(sl.maxProfit([1]))