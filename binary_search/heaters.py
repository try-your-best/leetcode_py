# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/6181626.html
"""

class Solution:
	def findRadius(self, houses: List[int], heaters: List[int]) -> int:
		heaters.sort()
		max_radius = 0
		for h in houses:
			left = 0
			right = len(heaters)-1
			while left < right: # 用这种方法来逼近，真NB
				mid = left + (right-left)//2
				if heaters[mid] < h:
					left = mid + 1
				else:
					right = mid
			# heaters[right] >= houses
			if right == 0:
				max_radius = max(max_radius, abs(h-heaters[right]))
			else:
				max_radius = max(max_radius, min(abs(h-heaters[right]), abs(h-heaters[right-1])))

		return max_radius


class Solution:
	def findRadius(self, houses: List[int], heaters: List[int]) -> int:
		heaters.sort()
		max_radius = 0
		heaters_len = len(heaters)
		for h in houses:
			left = 0
			right = heaters_len # 注意取值
			while left < right: # 用这种方法来逼近，真NB
				mid = left + (right-left)//2
				if heaters[mid] < h:
					left = mid + 1
				else:
					right = mid
			# heaters[right] >= houses
			if right == 0:
				max_radius = max(max_radius, heaters[right] - h)
			elif right == heaters_len:
				max_radius = max(max_radius, h - heaters[right-1])
			else:
				max_radius = max(max_radius, min(heaters[right]-h, h-heaters[right-1]))

		return max_radius


if __name__ == '__main__':
	sl = Solution()
	print(sl.findRadius([1,2,3],[2])) # 1
	print(sl.findRadius([1,2,3,4],[1,4])) #1
	print(sl.findRadius([2],[1,4])) #1
	print(sl.findRadius([8],[1,4])) #3