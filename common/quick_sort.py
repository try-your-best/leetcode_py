# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

"""
在最坏的情况下，待排序的序列为正序或者逆序, 复杂度为 O(n^2). 关键是 partition 返回的下标不要偏。
"""


def quick_sort(array):
	quick_sort_core(array, 0, len(array)-1)
	return array


def quick_sort_core(array, left, righ):
	if left < righ:
		p = partition(array, left, righ)
		quick_sort_core(array, left, p-1)
		quick_sort_core(array, p+1, righ)


def partition(array, left, righ):
	pivot = array[righ]
	i = left - 1  # i 始终指向 <= pivot 的值
	for j in xrange(left, righ):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]

	i += 1
	array[i], array[righ] = array[righ], array[i]

	return i


if __name__ == '__main__':
	array = [4, 3, 1, 2]
	print quick_sort(array)