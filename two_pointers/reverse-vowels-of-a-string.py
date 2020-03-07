# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution:
	Vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

	def reverseVowels(self, s: str) -> str:
		left = 0
		right = len(s)-1
		s = list(s)
		while left < right:
			if s[left] in self.Vowels and s[right] in self.Vowels:
				s[left], s[right] = s[right], s[left]
				left += 1
				right -= 1
			elif s[left] in self.Vowels:
				right -= 1
			elif s[right] in self.Vowels:
				left += 1
			else:
				left += 1
				right -= 1
		return ''.join(s)


if __name__ == '__main__':
	sl =Solution()
	s = 'hello'
	print(sl.reverseVowels(s))
	# print(s)