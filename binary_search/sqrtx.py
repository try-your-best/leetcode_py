# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution:
	def mySqrt(self, x: int) -> int:
		low = 0
		high = x
		while low < high:
			mid = (low + high)//2
			mid_square = mid ** 2
			if mid_square == x:
				return mid
			elif mid_square < x:
				low = mid + 1
			else:
				high = mid - 1

		low_square = low ** 2
		if low_square <= x:
			return low
		else:
			return low - 1


if __name__ == '__main__':
	sl = Solution()
	print(sl.mySqrt(4))
	print(sl.mySqrt(8))
	print(sl.mySqrt(1))
	print(sl.mySqrt(0))