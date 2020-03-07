# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution:
	def backspaceCompare(self, S: str, T: str) -> bool:
		return self._getFinalStr(S) == self._getFinalStr(T)

	def _getFinalStr(self, s: str):
		stack = []
		for char in s:
			if char == '#':
				if stack:
					stack.pop()
			else:
				stack.append(char)

		return ''.join(stack)


class Solution:
	def backspaceCompare(self, S: str, T: str) -> bool:
		i = len(S)-1
		j = len(T)-1
		c1 = 0
		c2 = 0
		while i >= 0 or j >= 0:
			while i >= 0 and (S[i] == '#' or c1 > 0):
				if S[i] == '#':
					c1 += 1
				else:
					c1 -= 1
				i -= 1

			while j >= 0 and (T[j] == '#' or c2 > 0):
				if T[j] == '#':
					c2 += 1
				else:
					c2 -= 1
				j -= 1

			# print('3', i, j)

			if i < 0 or j < 0:
				return i == j

			if S[i] != T[j]:
				# print('1', i, j)
				return False
			i -= 1
			j -= 1

		# print('2', i, j)
		return i == j


if __name__ == '__main__':
	sl = Solution()
	print(sl.backspaceCompare('ab#c', 'ad#c'))
	print(sl.backspaceCompare('a#c', 'b'))
	print(sl.backspaceCompare('nzp#o#g', 'b#nzp#o#g'))