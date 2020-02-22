# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution:
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		if len(letters) == 1:
			return letters[0]
		left = 0
		right = len(letters)
		while left < right:
			mid = left + (right - left)//2
			if letters[mid] <= target:
				left = mid + 1
			else:
				right = mid
		return letters[right] if right < len(letters) else letters[0]


if __name__ == '__main__':
	sl = Solution()
	print(sl.nextGreatestLetter(["c", "f", "j"], "a")) # c
	print(sl.nextGreatestLetter(["c", "f", "j"], "c")) # f
	print(sl.nextGreatestLetter(["c", "f", "j"], "d")) # f
	print(sl.nextGreatestLetter(["c", "f", "j"], "g")) # j
	print(sl.nextGreatestLetter(["c", "f", "j"], "j")) # c
	print(sl.nextGreatestLetter(["c", "f", "j"], "k")) # c
	print(sl.nextGreatestLetter(["c"], "k")) # c