# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution:
	def reverseStr(self, s: str, k: int) -> str:
		i = 0
		reverse = True
		end = len(s)
		s_list = list(s)
		while i < end:
			if reverse:
				n = i
				m = min(i+k-1, end-1)
				while n < m:
					s_list[n], s_list[m] = s_list[m], s_list[n]
					n += 1
					m -= 1

				reverse = False
			else:
				reverse = True

			i = i + k

		return ''.join(s_list)


if __name__ == '__main__':
	sl =Solution()
	print(sl.reverseStr('abcdefg', 2))