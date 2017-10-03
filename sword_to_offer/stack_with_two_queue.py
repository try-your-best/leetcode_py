# -*- coding: utf-8 -*-

from collections import deque

"""
python  list 本身就有支持 stack 的操作的接口
"""


class Stack(object):

	def __init__(self):
		self.queue1 = deque()
		self.queue2 = deque()

	def push(self, element):
		if not self.queue1 and not self.queue2:
			self.queue1.append(element)
		elif self.queue1 and not self.queue2:
			self.queue1.append(element)
		elif not self.queue1 and self.queue2:
			self.queue2.append(element)
		else:
			raise Exception('error')

	def pop(self):
		if self.queue1:
			for _ in xrange(len(self.queue1)-1):
				self.queue2.append(self.queue1.popleft())
			return self.queue1.popleft()
		else:
			for _ in xrange(len(self.queue2)-1):
				self.queue1.append(self.queue2.popleft())
			return self.queue2.popleft()


if __name__ == "__main__":
	s = Stack()
	s.push(1)
	s.push(2)
	print s.pop()
	s.push(3)
	print s.pop()
	print s.pop()


