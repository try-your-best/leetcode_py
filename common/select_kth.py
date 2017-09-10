# -*- coding: utf-8 -*-

# 快排的一个经典应用， 复杂度是 O(n)


def partition(ary, left, right):
	pivot = ary[right]
	i = left - 1

	for j in xrange(left, right):
		if ary[j] <= pivot:
			i += 1
			ary[i], ary[j] = ary[j], ary[i]

	ary[i+1], ary[right] = ary[right], ary[i+1]
	return i+1


def select_kth(ary, k):
	left, right = 0, len(ary)-1
	index = partition(ary, left, right)

	while index != k-1:
		if index < k - 1:
			left = index + 1
			index = partition(ary, left, right)
		else:
			right = index - 1
			index = partition(ary, left, right)

	return ary[index]


if __name__ == '__main__':
	ary = [6, 1, 2, 3, 4, 5]
	print select_kth(ary, 3)