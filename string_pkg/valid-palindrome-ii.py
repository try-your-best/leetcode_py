


class Solution:
	def validPalindrome(self, s: str) -> bool:
		i = 0
		j = len(s) - 1
		# print(len(s))
		# print(s[0:22])
		# print(s[80:len(s)])
		while i < j:
			if s[i] == s[j]:
				i += 1
				j -= 1
			else:
				return self.isValid(s, i+1, j) or self.isValid(s, i, j-1)

		return True

	def isValid(self, s, left, right):
		while left < right:
			if s[left] != s[right]:
				return False
			left += 1
			right -= 1
		return True


if __name__ == '__main__':
	sl =Solution()
	print(sl.validPalindrome('aba'))
	print(sl.validPalindrome('abca'))
	print(sl.validPalindrome('abcaca'))
	print(sl.validPalindrome('abcbaca'))
	s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
	print(sl.validPalindrome(s))
	# print(s[19:82])
	# print(sl.validPalindrome(s[19:82]))