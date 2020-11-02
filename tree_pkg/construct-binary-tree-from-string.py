# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *


class Solution(object):
	NUMS = set([str(n) for n in range(0, 10)])

	def str2tree(self, s: str):
		if s == "":
			return None
		root, _ = self._buildTree(s, 0)
		return root

	def _buildTree(self, s: str, idx: int):
		start = idx
		if s[idx] == '-':
			idx += 1
		while idx < len(s) and s[idx].isdigit():  #
			idx += 1
		root = TreeNode(int(s[start:idx]))
		if idx < len(s):
			cur_s = s[idx]
			if cur_s == '(':
				root.left, idx = self._buildTree(s, idx + 1)
				if idx < len(s):
					cur_s = s[idx]
					if cur_s == '(':
						root.right, idx = self._buildTree(s, idx + 1)
			elif cur_s == ')':
				return root, idx + 1
		return root, idx + 1


if __name__ == '__main__':
	sl = Solution()
	r = sl.str2tree("4(2(3)(1))(6(5))")
	r = sl.str2tree("-4(-21(3)(1))(6(5))")
	a = 1


