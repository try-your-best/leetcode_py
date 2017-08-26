# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


def quick_sort(ary, left, right):
	if left < right:
		q = partition(ary, left, right)
		quick_sort(ary, left, q - 1)
		quick_sort(ary, q + 1, right)


def partition(ary, left, right):
	pivot = ary[right]
	i = left-1
	for j in xrange(left, right):
		if ary[j] <= pivot:
			i += 1
			ary[j], ary[i] = ary[i], ary[j]

	ary[i + 1], ary[right] = ary[right], ary[i + 1]

	return i+1


if __name__ == '__main__':
	ary = [4, 3, 1, 2]
	# ary = []
	quick_sort(ary, 0, len(ary) - 1)
	print ary