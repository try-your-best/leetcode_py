# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def decodeString(self, s: str) -> str:
		num_stack = []
		str_stack = []
		str_list = []
		i = 0
		k_keep = 0
		s_keep = ''
		s_len = len(s)
		while i < s_len:
			cur_s = s[i]
			if cur_s.isdigit():
				end = i + 1
				while end < s_len and s[end].isdigit():
					end += 1
				k_keep = int(s[i:end])
				i = end
			elif cur_s == '[':
				num_stack.append(k_keep)
				str_stack.append(s_keep)
				# k_keep = 0
				# s_keep = ''
				i += 1
			elif cur_s == ']':
				k_tmp = num_stack.pop()
				s_tmp = str_stack.pop()
				s_tmp = s_tmp * k_tmp
				if num_stack:
					str_stack[-1] += s_tmp
				else:
					str_list.append(s_tmp)
				i += 1
			else:  # alpha
				end = i + 1
				while end < s_len and s[end].isalpha():
					end += 1
				s_keep = s[i:end]
				i = end
				if str_stack:
					str_stack[-1] += s_keep
				else:
					str_list.append(s_keep)
				s_keep = ''
		return ''.join(str_list)

"""
能用 stack 的优先考虑递归，写起来简单。每次遇到 [，就是调用函数栈的时机。
"""
class Solution:
	def decodeString(self, s: str) -> str:
		self.i = 0
		return self._decode(s)

	def _decode(self, s: str):
		s_len = len(s)
		k_keep = 0
		s_keep = ''
		while self.i < s_len:
			cur_s = s[self.i]
			if cur_s.isdigit():
				end = self.i + 1
				while end < s_len and s[end].isdigit():
					end += 1
				k_keep = int(s[self.i:end])
				self.i = end
			elif cur_s == '[':
				self.i += 1  # 注意
				s_tmp = self._decode(s)
				s_keep += s_tmp * k_keep
			elif cur_s == ']':
				self.i += 1
				return s_keep
			else:
				end = self.i + 1
				while end < s_len and s[end].isalpha():
					end += 1
				s_keep += s[self.i:end]
				self.i = end
		return s_keep

# class Solution:
# 	def decodeString(self, s: str) -> str:
# 		num_stack = []
# 		str_stack = []
# 		str_list = []
# 		i = 0
# 		s_len = len(s)
# 		while i < s_len:
# 			cur_s = s[i]
# 			if cur_s.isdigit():
# 				end = i+1
# 				while end < s_len and s[end].isdigit():
# 					end += 1
# 				k = int(s[i:end])
# 				if len(num_stack) > len(str_stack):
# 					str_stack.append('')
# 				num_stack.append(k)
# 				i = end + 1  # encoded_string, s[end] == [
# 			elif cur_s.isalpha():
# 				end = i + 1
# 				while end < s_len and s[end].isalpha():
# 					end += 1
# 				s_tmp = s[i:end]
# 				if num_stack:
# 					if len(str_stack) < len(num_stack):
# 						str_stack.append(s_tmp)
# 					else:
# 						str_stack[-1] += s_tmp
# 				else:
# 					str_list.append(s_tmp)
# 				i = end
# 			elif cur_s == ']':
# 				k = num_stack.pop()
# 				s_tmp = str_stack.pop()
# 				s_tmp = s_tmp * k
# 				print(s_tmp)
# 				print(num_stack)
# 				print(str_stack)
# 				if not num_stack and not str_stack:
# 					str_list.append(s_tmp)
# 				else:
# 					str_stack[-1] += s_tmp
# 				i += 1
# 			else:
# 				raise Exception(cur_s)
# 		return ''.join(str_list)


if __name__ == '__main__':
	sl = Solution()
	# print(sl.decodeString('3[a]2[bc]'))
	# print(sl.decodeString('3[a2[c]]'))
	# print(sl.decodeString('2[abc]3[cd]ef'))
	# print(sl.decodeString("3[a]2[b4[F]c]"))  #  "aaabFFFFcbFFFFc"
	# print(sl.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
	print(sl.decodeString("2[2[y]]"))
	# print(sl.decodeString("ab2[c]"))