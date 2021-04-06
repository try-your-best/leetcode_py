# -*- coding: utf-8 -*-
"""
https://www.cnblogs.com/grandyang/p/4447233.html

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Time:  O(k), where k is the steps to be happy number
Space: O(k)

"""


class Solution:
	# @param {integer} n
	# @return {boolean}
	def isHappy(self, n):
		nums = set()
		while n != 1 and n not in nums:
			nums.add(n)
			# n = self.nextNum(n)
			n = self.nextNum2(n)
		return n == 1

	def nextNum(self, n):
		num = 0
		for i in str(n):
			num += int(i)**2
		return num

	def nextNum2(self, n):
		num = 0
		while n != 0:
			num += (n%10)**2
			n //= 10  #  注意 py3的修改
		return num


if __name__ == '__main__':
	print(Solution().isHappy(19))
	print(Solution().isHappy(11))
	n = 21
	n //= 10
	print(n)