"""
https://www.cnblogs.com/grandyang/p/4694988.html
"""

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		m = [0] * 26
		for cur in s:
			m[ord(cur)-ord('a')] += 1
		for cur in t:
			idx = ord(cur) - ord('a')
			m[idx] -= 1
			if m[idx] < 0:
				return False
		return True


if __name__ == '__main__':
	sl =Solution()
	print(sl.isAnagram("anagram", "nagaram"))
	print(sl.isAnagram("rat", "car"))
	print(sl.isAnagram("ab", "a"))
