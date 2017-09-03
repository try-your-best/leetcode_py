# -*- coding: utf-8 -*-


def insertion_sort(ary):
	for j in xrange(1, len(ary)):
		key = ary[j]
		i = j-1
		while i >= 0 and key < ary[i]:
			ary[i+1] = ary[i]
			i -= 1
		ary[i+1] = key


if __name__ == '__main__':
	ary = [4, 3, 1, 2, 6]
	# ary = []
	insertion_sort(ary)
	print ary