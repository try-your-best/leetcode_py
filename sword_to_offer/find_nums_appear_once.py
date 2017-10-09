# -*- coding: utf-8 -*-


def findNumsAppearOnce(nums):
	if not nums or len(nums) < 2:
		return None, None

	resultXOR = 0
	for num in nums:
		resultXOR ^= num

	idx = findFirstBitIs1(resultXOR)
	num1, num2 = 0, 0

	for num in nums:
		if isBit1(num, idx):
			num1 ^= num
		else:
			num2 ^= num

	return num1, num2


def findFirstBitIs1(num):
	idx = 0
	while num & 1 != 1 and idx < 32:
		num >>= 1
		idx += 1

	return idx


def isBit1(num, idx):
	return (num >> idx) & 1 == 1


if __name__ == "__main__":
	# print isBit1(4, findFirstBitIs1(4))
	print findNumsAppearOnce([1, 1, 2, 2, 3, 4])
	# print isBit1(4, 0)
	# print isBit1(3, 0)
