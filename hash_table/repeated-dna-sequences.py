# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List


class Solution:
	def findRepeatedDnaSequences(self, s: str) -> List[str]:
		ret = set()
		if len(s) <= 10:
			return list(ret)

		look_up = set()
		mask = 0xfffff
		map_code = {'A': 0x0, 'C': 0x1, 'G': 0x2, 'T': 0x3}
		str_code = 0

		for idx in range(0, 10):
			str_code = (str_code << 2) + map_code[s[idx]]
		look_up.add(str_code & mask)

		for idx in range(10, len(s)):
			str_code = ((str_code << 2) + map_code[s[idx]]) & mask
			if str_code in look_up:
				ret.add(s[idx-9:idx+1])
			else:
				look_up.add(str_code)

		return list(ret)


if __name__ == '__main__':
	sl = Solution()
	print(sl.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
