# -*- coding: utf-8 -*-
__author__ = 'damon'


"""
https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/
用栈模拟，两个叶子节点把父节点替换成叶子节点 '#'
"""

class Solution:
	def isValidSerialization(self, preorder: str) -> bool:
		strs = preorder.split(',')
		stack = []
		for i in range(0, len(strs)):
			s = strs[i]
			if s == '#':
				while len(stack) >= 2 and stack[-1] == '#' and stack[-2] != '#':
					stack.pop()
					stack.pop()
				stack.append('#')
			else:
				stack.append(s)
		return len(stack) == 1 and stack[0] == '#'


class Solution:
	def isValidSerialization(self, preorder: str) -> bool:
		if preorder == "#":
			return True
		stack = []
		for s in preorder.split(","):
			if s == "#":
				if not stack:
					return False
				elif stack[-1] == "#":
					while len(stack) >= 2 and stack[-1] == "#":
						stack.pop()
						stack.pop()
					if stack and stack[-1] == "#":
						return False
					stack.append("#")
				else:
					stack.append(s)
			else:
				stack.append(s)
		return len(stack) == 1 and stack[-1] == "#"


if __name__ == '__main__':
	sl = Solution()
	# print(sl.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
	# print(sl.isValidSerialization("1,#"))
	# print(sl.isValidSerialization("9,#,#,1"))
	# print(sl.isValidSerialization("#"))
	print(sl.isValidSerialization("1,#,#,#,#"))
	"""
	9,3,4,#,#,1,#,#,2,#,6,#,#
	9,3,#,1,#,#,2,#,6,#,#
	9,#,2,#,6,#,#
	#
	"""