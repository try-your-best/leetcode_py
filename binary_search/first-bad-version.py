# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4790469.html
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	return version >= 7


class Solution:
	def firstBadVersion(self, n: int) -> int:
		low = 1
		high = n
		while low <= high:
			mid = (low + high)//2
			if isBadVersion(mid):
				if mid == 1 or not isBadVersion(mid-1):
					return mid
				else:
					high = mid - 1
			else:
				low = mid + 1
		return low


class Solution:
	def firstBadVersion(self, n: int) -> int:
		left = 1
		right = n
		while left < right:
			mid = (left + right)//2
			if isBadVersion(mid):
				right = mid
			else:
				left = mid + 1
		return right


if __name__ == '__main__':
	sl = Solution()
	print(sl.firstBadVersion(6))