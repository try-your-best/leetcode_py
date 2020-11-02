# -*- coding: utf-8 -*-


def reverseSentence(string):
	if not string:
		return string

	strList = list(string)
	strListLen = len(strList)

	# 翻转整个句子
	reverse(strList, 0, strListLen-1)

	# 翻转单词
	wordStart, wordEnd = 0, 0
	while wordStart < strListLen:
		if strList[wordStart] == ' ':
			wordStart += 1
			wordEnd += 1
		elif wordEnd == strListLen or strList[wordEnd] == ' ':  # 注意这里的判断次序，避免溢出
			reverse(strList, wordStart, wordEnd-1)
			wordEnd += 1
			wordStart = wordEnd
		else:
			wordEnd += 1

	return ''.join(strList)


def reverse(strList, start, end):
	while start < end:
		strList[start], strList[end] = strList[end], strList[start]
		start += 1
		end -= 1


if __name__ == "__main__":
	print reverseSentence('I am a student.')
	print reverseSentence('   ')
	print reverseSentence('you are a    ')

