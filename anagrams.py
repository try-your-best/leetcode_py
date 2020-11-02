# -*- coding: utf-8 -*-


# 这道题让我们群组给定字符串集中所有的错位词，所谓的错位词就是两个字符串中字母出现的次数都一样，
# 只是位置不同，比如abc，bac, cba等它们就互为错位词，那么我们如何判断两者是否是错位词呢，
# 我们发现如果把错位词的字符顺序重新排列，那么会得到相同的结果，所以重新排序是判断是否互为错位词的方法，
# 由于错位词重新排序后都会得到相同的字符串，我们以此作为key，将所有错位词都保存到字符串数组中，
# 建立key和字符串数组之间的映射，最后再存入结果res中即可，擦巾代码如下：


import collections


# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)

class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		strDict = collections.defaultdict(list)

		for s in strs:
			sortedStr = ''.join(sorted(s))
			strDict[sortedStr].append(s)

		result = [value for value in strDict.itervalues()]
		return result


if __name__ == '__main__':
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(Solution().groupAnagrams(strs))