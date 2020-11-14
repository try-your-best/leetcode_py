"""
https://www.cnblogs.com/grandyang/p/6666839.html
这题主要是弄清最长子序列的定义
"""


class Solution:
	def findLUSlength(self, a: str, b: str) -> int:
		return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
	sl =Solution()
	print(sl.findLUSlength("aaa", "aa"))