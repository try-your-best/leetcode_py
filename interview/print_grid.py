# -*- coding: utf-8 -*-
__author__ = 'damon'

# ## 请在下方描述你的面试题内容( 支持Markdown )
# test
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# grid = [
# 	[1, 2, 3, 4],
# 	[5, 6, 7, 8],
# 	[9, 10, 11, 12],
# 	[13, 14, 15, 16]
# ]
#
# grid = [
# 	[1, 2, 3, 4, 5],
# 	[6, 7, 8, 9, 10],
# 	[11, 12, 13, 14, 15],
# 	[16, 17, 18, 19, 20],
# 	[21, 22, 23, 24, 25],
# ]

grid = [
	[1, 2, 3],
	[6, 7, 8],
	[11, 12, 13],
	[16, 17, 18],
	[21, 22, 23],
]

grid = [
	[1, 2, 3, 4, 5],
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
]



def printDebug(flag, i1, i2, i, j, k, h):
	# print('#'.join([flag, str(i1), str(i2), str(i), str(j), str(k), str(h)]))
	pass


def printGrid(grid):
	m = len(grid)
	n = len(grid[0])

	i = 0
	j = m - 1
	k = 0
	h = n - 1
	while i < j or k < h:
		# to right
		for cur in range(k, h + 1):
			print(grid[i][cur])
			printDebug('a', i, cur, i, j, k, h)

		# to down
		for cur in range(i + 1, j + 1):
			print(grid[cur][h])
			printDebug('b', i, cur, i, j, k, h)

		# to left
		if i < j:
			for cur in range(h - 1, k - 1, -1):
				print(grid[j][cur])
				printDebug('c', i, cur, i, j, k, h)

		# to up
		if k < h:
			for cur in range(j - 1, i, -1):
				print(grid[cur][k])
				printDebug('d', i, cur, i, j, k, h)

		i += 1
		j -= 1
		k += 1
		h -= 1


printGrid(grid)