# -*- coding: utf-8 -*-

from reverse_word_in_sentence import reverse


def leftRotateString(string, n):
	if not string or n <= 0 or len(string) <= n:
		return string

	strList = list(string)
	strListLen = len(strList)

	reverse(strList, 0, n-1)
	reverse(strList, n, strListLen-1)
	reverse(strList, 0, strListLen-1)
	return ''.join(strList)


if __name__ == "__main__":
	print leftRotateString('abcdefg', 2)
	print leftRotateString('abcdefg', 6)
	print leftRotateString('abcdefg', 7)
	print leftRotateString('abcdefg', 0)