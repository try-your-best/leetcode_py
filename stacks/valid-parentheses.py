
"""
https://www.cnblogs.com/grandyang/p/4424587.html
"""

class Solution:
	def isValid(self, s: str) -> bool:
		"""
		:type s: str
		:rtype: bool
		"""
		if not s:
			return True

		stack = []
		lookup = {"(": ")", "{": "}", "[": "]"}  # 这种用法很巧妙

		for cur_s in s:
			if cur_s in lookup:
				stack.append(cur_s)
			else:
				if not stack or lookup[stack.pop()] != cur_s:
					return False

		return not stack


if __name__ == '__main__':
	sl = Solution()
	print(sl.isValid("{"))
	print(sl.isValid("}"))
	print(sl.isValid("{}"))
	print(sl.isValid("{}}"))
	print(sl.isValid("{}[]"))
	print(sl.isValid("[{}]"))
	print(sl.isValid("()"))

