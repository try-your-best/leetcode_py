"""
因为是回文，如果前半段有不是 a， 直接替换，这样最小。如果回文全是 a，则把最后一位改成 b

"""

class Solution:
	def breakPalindrome(self, palindrome: str) -> str:
		mid = int(len(palindrome)/2)
		str_list = list(palindrome)
		for i in range(mid):
			if str_list[i] > "a":
				str_list[i] = "a"
				return "".join(str_list)
		if len(str_list) > 1:
			str_list[-1] = "b"
			return "".join(str_list)
		else:
			return ""


if __name__ == '__main__':
	sl =Solution()
	print(sl.breakPalindrome("abccba"))
	print(sl.breakPalindrome("a"))
	print(sl.breakPalindrome("aa"))
