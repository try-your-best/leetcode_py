# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution:
	def isPalindrome(self, s: str) -> bool:
		left = 0
		right = len(s)-1
		while left < right:
			left_valid = self._isValid(s[left])
			right_valid = self._isValid(s[right])
			if left_valid and right_valid:
				if s[left].lower() != s[right].lower():
					return False
				left += 1
				right -= 1
			elif left_valid:
				right -= 1
			elif right_valid:
				left += 1
			else:
				left += 1
				right -= 1
		return True

	def _isValid(self, s: str):
		return '0' <= s <= '9' or 'a' <= s <= 'z' or 'A' <= s <= 'Z'


if __name__ == '__main__':
	sl =Solution()
	print(sl.isPalindrome('A man, a plan, a canal: Panama'))
	print(sl.isPalindrome('race a car'))
