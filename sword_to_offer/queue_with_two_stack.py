# -*- coding: utf-8 -*-


class Queue(object):

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, element):
		self.stack1.append(element)

	def pop(self):
		if self.stack2:
			return self.stack2.pop()
		while self.stack1:
			self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


if __name__ == "__main__":
	q = Queue()
	q.push(1)
	q.push(2)
	q.push(3)
	print q.pop()
	print q.pop()
	print q.pop()

