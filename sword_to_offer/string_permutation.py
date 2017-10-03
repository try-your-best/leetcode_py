# -*- coding: utf-8 -*-


def permutation(strList, start):
	strLen = len(strList)
	if start == strLen - 1:
		print ''.join(strList)

	for idx in xrange(start, strLen):
		strList[start], strList[idx] = strList[idx], strList[start]
		permutation(strList, start+1)
		strList[start], strList[idx] = strList[idx], strList[start]


def permuteString(string):
	permutation(list(string), 0)


if __name__ == "__main__":
	permuteString('abc')
