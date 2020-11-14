from common.utils import *

"""
https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/longest-uncommon-subsequence-ii.py
https://www.cnblogs.com/grandyang/p/6680548.html
"""

class Solution:
	def findLUSlength(self, strs: List[str]) -> int:
		strs.sort(key=len, reverse=True)
		# print(strs)
		for i in range(len(strs)):
			found = True
			for j in range(len(strs)):
				# print(i, j, strs[i], strs[j])
				if len(strs[i]) > len(strs[j]):
					break
				# print(self.isSubStr(strs[i], strs[j]))
				if i != j and self.isSubStr(strs[i], strs[j]):
					found = False
					break
			if found:
				return len(strs[i])
		return -1

	def isSubStr(self, sub, b):  # 注意 substr 的定义
		i = 0
		for s in b:
			if s == sub[i]:
				i += 1
			if i == len(sub):
				break
		return i == len(sub)




if __name__ == '__main__':
	sl =Solution()
	print(sl.findLUSlength(["aabbcc", "aabbcc","bc"]))
	# print(sl.findLUSlength(["aba", "cdc", "eae"]))
	print(sl.findLUSlength(["aaa","aaa","aa"])) # -1
	print(sl.isSubStr("bc", "aabbcc"))