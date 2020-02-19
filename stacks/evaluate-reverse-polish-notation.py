# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4247718.html
"""

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		for t in tokens:
			if t == '+':
				b = stack.pop()  # 注意 a，b 次序
				a = stack.pop()
				stack.append(a+b)
			elif t == '-':
				b = stack.pop()
				a = stack.pop()
				stack.append(a - b)
			elif t == '*':
				b = stack.pop()
				a = stack.pop()
				stack.append(a * b)
			elif t == '/':
				b = stack.pop()
				a = stack.pop()
				stack.append(int(a / b))
			else:
				stack.append(int(t))
		return stack.pop()


if __name__ == '__main__':
	sl = Solution()
	print(sl.evalRPN(["2", "1", "+", "3", "*"]))
	print(sl.evalRPN(["4", "13", "5", "/", "+"]))
	print(sl.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

