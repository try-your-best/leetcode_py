# -*- coding: utf-8 -*-


def binarySearch(ary, t):
	low = 0
	high = len(ary) - 1

	# 注意等于的情况
	while low <= high:
		mid = int(low+(high - low)/2)  # 不写成 (high+low)/2 是为了防止溢出

		if ary[mid] < t:
			low = mid + 1
		elif ary[mid] > t:
			high = mid - 1
		else:
			return mid

	return -1


if __name__ == '__main__':
	ary = [1, 3, 6, 7, 10]
	print(binarySearch(ary, 6))
	ary = ([1, 2, 4, 6, 10])
	print(binarySearch(ary, 10))
	ary = [1, 2]
	print(binarySearch(ary, 6))