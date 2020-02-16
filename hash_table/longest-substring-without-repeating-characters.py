# -*- coding: utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#

# 解题思路：使用一个哈希表，记录字符的索引。例如对于字符串'zwxyabcabczbb'，
# 当检测到第二个'a'时，由于之前已经有一个'a'了，所以应该从第一个a的下一个字符重新开始测算长度，
# 但是要把第一个a之前的字符在哈希表中对应的值清掉，如果不清掉的话，就会误以为还存在重复的。
# 比如检测到第二个'z'时，如果第一个'z'对应的哈希值还在，那就出错了，
# 所以要把第一个'a'之前的字符的哈希值都重置才行。

# Time:  O(n)
# Space: O(1)

class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		longest, start, visited = 0, 0, [False] * 256
		for idx, char in enumerate(s):
			if visited[ord(char)]:
				while char != s[start]:
					visited[ord(s[start])] = False  # 注意清除掉重复词的第一词之前的词
					start += 1
				start += 1
			else:
				visited[ord(char)] = True

			longest = max(longest, idx-start+1)

		return longest


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		look_up = {}
		start = 0
		max_len = 0
		for index, cur_s in enumerate(s):
			if cur_s in look_up and look_up[cur_s] >= start:  # 注意小于 start 的就不算重复了
				max_len = max(max_len, index - start)
				start = look_up[cur_s] + 1
			look_up[cur_s] = index

		max_len = max(max_len, len(s) - start)

		return max_len


if __name__ == '__main__':
	sl = Solution()
	print(sl.lengthOfLongestSubstring("abcabcbb"))
	print(sl.lengthOfLongestSubstring("bbbbb"))
	print(sl.lengthOfLongestSubstring("pwwkew"))
	print(sl.lengthOfLongestSubstring("abba"))