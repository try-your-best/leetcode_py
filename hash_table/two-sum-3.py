# -*- coding: utf-8 -*-
__author__ = 'damon'

from collections import defaultdict


class TwoSum(object):
	def __init__(self):
		"""
		initialize your data structure here
		"""
		self.lookup = defaultdict(int)

	def add(self, number):
		"""
		Add the number to an internal data structure.
		:rtype: nothing
		"""
		self.lookup[number] += 1

	def find(self, value):
		"""
		Find if there exists any pair of numbers which sum is equal to the value.
		:type value: int
		:rtype: bool
		"""
		for n in self.lookup.keys():
			diff = value - n
			if diff in self.lookup and (diff != n or self.lookup[diff] > 1):
				return True
		return False


if __name__ == '__main__':
	ts = TwoSum()
	ts.add(1)
	ts.add(1)
	ts.add(2)
	ts.add(2)
	ts.add(2)
	ts.add(3)

	print(ts.find(2))
	print(ts.find(3))
	print(ts.find(6))