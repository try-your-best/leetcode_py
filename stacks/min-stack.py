# -*- coding: utf-8 -*-
__author__ = 'damon'


class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.normal_stack = []
		self.min_stack = []

	def push(self, x: int) -> None:
		self.normal_stack.append(x)
		if not self.min_stack or x <= self.min_stack[-1]: # 注意这里是小于等于，
			self.min_stack.append(x)

	def pop(self) -> None:
		x = self.normal_stack.pop()
		if x <= self.min_stack[-1]:
			self.min_stack.pop()

	def top(self) -> int:
		return self.normal_stack[-1]

	def getMin(self) -> int:
		return self.min_stack[-1]


if __name__ == '__main__':
	minStack = MinStack()
	minStack.push(-2)
	minStack.push(0)
	minStack.push(-3)
	print(minStack.getMin()) # --> Returns - 3.

	minStack.pop()
	print(minStack.top()) # --> Returns 0.
	print(minStack.getMin())  #--> Returns - 2.


