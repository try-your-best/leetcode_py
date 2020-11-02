# -*- coding: utf-8 -*-

# Time:  O(nlogn)
# Space: O(1)
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#


class Solution:
	# @param num, a list of integers
	# @return a string
	def largestNumber(self, num):
		num = [str(x) for x in num]
		# 因为默认是升序， x+y 取得大值时，要让 x 的值小
		num.sort(cmp=lambda x, y: cmp(y + x, x + y))
		largest = ''.join(num)
		# 假设所有 num 都是 0
		return largest.lstrip('0') or '0'


if __name__ == "__main__":
	num = [3, 30, 34, 5, 9]
	print(Solution().largestNumber(num))

	print('10' < '100')  # True
	print('20' < '100')  # False
