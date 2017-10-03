# -*- coding: utf-8 -*-

"""
保证所有压人栈的顺序均不相等。 反例 [1, 2, 1, 3], [1, 3, 2, 1] 是合法，但下面的算法返回 False

"""


def isPopOrder(pushOrder, popOrder):
	if not pushOrder or not popOrder:
		return False

	stack = []

	pushIdx = 0
	pushOrderLen = len(pushOrder)

	for popValue in popOrder:
		while not stack or stack[-1] != popValue:
			if pushIdx < pushOrderLen:
				stack.append(pushOrder[pushIdx])
				pushIdx += 1
			else:
				return False
		stack.pop()

	return True


if __name__ == "__main__":
	print isPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
	print isPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
	print isPopOrder([1], [1])

	# 保证所有压人栈的顺序均不相等
	print isPopOrder([1, 2, 1, 3], [1, 3, 2, 1])