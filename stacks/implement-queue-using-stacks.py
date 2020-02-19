# -*- coding: utf-8 -*-
__author__ = 'damon'

"""
https://www.cnblogs.com/grandyang/p/4626238.html
用 python 不大会出这种题
"""


class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.stack = []

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		tmp = []
		while self.stack:
			tmp.append(self.stack.pop())

		self.stack.append(x)

		while tmp:
			self.stack.append(tmp.pop())

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		return self.stack.pop()

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		return self.stack[-1]

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		return not self.stack
