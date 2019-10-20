

class Solution(object):
	def isValid(self, s):
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


# class Solution(object):
# 	def isValid(self, s):
# 		"""
# 		:type s: str
# 		:rtype: bool
# 		"""
# 		if not s:
# 			return True
#
# 		stack = []
#
# 		for cur_s in s:
# 			if cur_s in ("(", "{", "["):
# 				stack.append(cur_s)
# 			else:
# 				if not stack:
# 					return False
# 				top = stack.pop()
# 				if (top == "(") and (cur_s == ")") or \
# 						(top == "{") and (cur_s == "}") or \
# 						(top == "[") and (cur_s == "]") :
# 					continue
# 				else:
# 					return False
#
# 		if stack:
# 			return False
#
# 		return True

if __name__ == '__main__':
	sl = Solution()
	print sl.isValid("{")
	print sl.isValid("}")
	print sl.isValid("{}")
	print sl.isValid("{}}")
	print sl.isValid("{}[]")
	print sl.isValid("[{}]")
	print sl.isValid("()")

