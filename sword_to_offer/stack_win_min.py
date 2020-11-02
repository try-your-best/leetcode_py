# -*- coding: utf-8 -*-


class StackWithMin(object):

	def __init__(self):
		self._data = []
		self._minData = []

	def push(self, value):
		self._data.append(value)
		if not self._minData or self._minData[-1] > value:
			self._minData.append(value)
		else:
			self._minData.append(self._minData[-1])

	def pop(self):
		self._minData.pop()
		return self._data.pop()

	def min(self):
		return self._minData[-1]


if __name__ == "__main__":
	stack = StackWithMin()
	stack.push(3)
	print stack.min()
	stack.push(4)
	print stack.min()
	stack.push(2)
	print stack.min()
	stack.push(1)
	print stack.min()
	stack.pop()
	print stack.min()