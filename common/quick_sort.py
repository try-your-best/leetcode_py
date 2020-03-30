# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

"""
在最坏的情况下，待排序的序列为正序或者逆序, 复杂度为 O(n^2). 关键是 partition 返回的下标不要偏。

快排的局限性
（1）快排是一个效率很高的排序算法，但是对于长度很小的序列，快排效率低。研究表明长度在5~25的数组，快排不如插入排序。
（2）pivot选择不当，将导致树的不平衡，这样导致快排的时间复杂度为o(n^2);
（3）但数组中有大量重复的元素，快排效率将非常之低。

"""

import random


def quick_sort(ary):
	quick_sort_core(ary, 0, len(ary)-1)
	return ary


def quick_sort_core(ary, left, right):
	if left < right:
		# p = partition(ary, left, right)
		p = partition2(ary, left, right)
		# p = partition3(ary, left, right)
		quick_sort_core(ary, left, p-1)
		quick_sort_core(ary, p+1, right)


def partition(ary, left, right):
	pivot = ary[right]
	i = left - 1  # i 始终指向 <= pivot 的值
	for j in range(left, right):  # 只迭代到 right-1
		if ary[j] <= pivot:
			i += 1
			ary[i], ary[j] = ary[j], ary[i]

	i += 1
	ary[i], ary[right] = ary[right], ary[i]

	return i


def partition2(ary, left, right):
	if right - left >= 2:
		mid = left + int((right-left)/2)
		# 找三者中间值并让中间值是 ary[right], 预防取到最大或最小值
		if ary[left] < ary[mid] < ary[right]:
			ary[mid], ary[right] = ary[right], ary[mid]
		elif ary[mid] < ary[left] < ary[right]:
			ary[left], ary[right] = ary[right], ary[left]

	pivot = ary[right]

	i = left - 1  # i 始终指向 <= pivot 的值
	for j in range(left, right):
		if ary[j] <= pivot:
			i += 1
			ary[i], ary[j] = ary[j], ary[i]

	i += 1
	ary[i], ary[right] = ary[right], ary[i]

	return i


def partition3(ary, left, right):
	if right - left >= 2:
		ra = random.randint(left, right)
		ary[ra], ary[right] = ary[right], ary[ra]

	pivot = ary[right]

	i = left - 1  # i 始终指向 <= pivot 的值
	for j in range(left, right):
		if ary[j] <= pivot:
			i += 1
			ary[i], ary[j] = ary[j], ary[i]

	i += 1
	ary[i], ary[right] = ary[right], ary[i]

	return i


if __name__ == '__main__':
	ary = [4, 3, 1, 2, 4, 8, 9]
	print(quick_sort(ary))