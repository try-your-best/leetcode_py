# -*- coding: utf-8 -*-

"""
45题， 具体解法看书
"""


def lastRemaining(n, m):
	if n < 1 or m < 1:
		return -1

	last = 0

	for i in xrange(2, n+1):
		last = (last + m) % i

	return last


if __name__ == "__main__":
	print lastRemaining(5, 3)