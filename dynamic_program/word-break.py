# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4257740.html
DP 解法的两大难点，定义 dp 数组跟找出状态转移方程，先来看 dp 数组的定义，这里我们就用一个一维的 dp 数组，其中 dp[i] 表示范围 [0, i) 
内的子串是否可以拆分，注意这里 dp 数组的长度比s串的长度大1，是因为我们要 handle 空串的情况，我们初始化 dp[0] 为 true，然后开始遍历。
注意这里我们需要两个 for 循环来遍历，因为此时已经没有递归函数了，所以我们必须要遍历所有的子串，我们用j把 [0, i) 范围内的子串分为了两部分，[0, j) 
和 [j, i)，其中范围 [0, j) 就是 dp[j]，范围 [j, i) 就是 s.substr(j, i-j)，其中 dp[j] 是之前的状态，我们已经算出来了，可以直接取，
只需要在字典中查找 s.substr(j, i-j) 是否存在了，如果二者均为 true，将 dp[i] 赋为 true，并且 break 掉，此时就不需要再用j去分 [0, i) 范围了，
因为 [0, i) 范围已经可以拆分了。最终我们返回 dp 数组的最后一个值，就是整个数组是否可以拆分的布尔值了，代码如下：
"""

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		word_set = set(wordDict)
		n = len(s)
		dp = [False] * (n + 1)
		dp[0] = True
		for i in range(1, n+1):
			for j in range(1, i+1):
				# 注意是 dp[j-1]， [0,j) 和 [j,i), 注意开和闭区间
				if dp[j-1] and s[j-1:i] in word_set:
					dp[i] = True
					break

		return dp[n]


if __name__ == '__main__':
	sl = Solution()
	print(sl.wordBreak("leetcode", ["leet", "code"]))
	print(sl.wordBreak("applepenapple", ["apple", "pen"]))
	print(sl.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))