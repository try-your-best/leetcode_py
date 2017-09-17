# -*- coding: utf-8 -*-

# 计数排序是一种算法复杂度 O(n) 的排序方法，适合于小范围集合的排序。
# 比如100万学生参加高考，我们想对这100万学生的数学成绩（假设分数为0到100）做个排序。


def counting_sort(ary):
	"""in-place counting sort"""
	m = max(ary) + 1
	count = [0] * m  # init with zeros
	for a in ary:
			count[a] += 1  # count occurences
	i = 0
	for a in range(m):  # emit
			for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
					ary[i] = a
					i += 1
	return ary


if __name__ == '__main__':
	print counting_sort([1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1])