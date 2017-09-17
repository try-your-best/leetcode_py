# -*- coding: utf-8 -*-


def binarySearch(ary, t):
	low = 0
	high = len(ary) - 1

	while low < high:
		mid = (low + high)/2

		if ary[mid] < t:
			low = mid + 1
		elif ary[mid] > t:
			high = mid - 1
		else:
			return mid

	return -1


if __name__ == '__main__':
	ary = [1, 3, 6, 7, 10]
	print binarySearch(ary, 6)