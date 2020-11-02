# -*- coding: utf-8 -*-


def getUglyNumber(index):
	if index <= 0:
		return 0

	uglyNums = [0] * index
	uglyNums[0] = 1

	index2 = 0
	index3 = 0
	index5 = 0

	nextIndex = 1

	while nextIndex < index:
		uglyNum = min(uglyNums[index2]*2, uglyNums[index3]*3, uglyNums[index5]*5)
		uglyNums[nextIndex] = uglyNum

		while uglyNums[index2]*2 <= uglyNum:
			index2 += 1

		while uglyNums[index3]*3 <= uglyNum:
			index3 += 1

		while uglyNums[index5]*5 <= uglyNum:
			index5 += 1

		nextIndex += 1

	return uglyNums[index-1]


if __name__ == "__main__":
	print getUglyNumber(1)
	print getUglyNumber(2)
	print getUglyNumber(3)
	print getUglyNumber(4)
	print getUglyNumber(5)
	print getUglyNumber(1500)