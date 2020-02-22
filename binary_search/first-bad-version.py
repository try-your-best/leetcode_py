# -*- coding: utf-8 -*-
__author__ = 'damon'


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


if __name__ == '__main__':
	sl = Solution()
	print(sl.firstBadVersion(10))