# -*- coding: utf-8 -*-


# 复杂度
# 空间复杂度：O(1), in-place排序
# 最差/平均/最优时间复杂度：O(nlgn)
# 注意
# 维护堆的时候注意，表示左子树和右子树的下标都不能超出堆的大小。
# 堆排序时，注意调整堆的大小。


def left_child(i):
	return 2*i+1


def right_child(i):
	return 2*i+2


def heapify(ary, i, heap_size):
	left, right = left_child(i), right_child(i)

	largest = left if left < heap_size and ary[left] > ary[i] else i
	largest = right if right < heap_size and ary[right] > ary[largest] else largest

	if i != largest:
		ary[i], ary[largest] = ary[largest], ary[i]
		heapify(ary, largest, heap_size)


def heapify_loop(ary, i, heap_size):
	while True:
		left, right = left_child(i), right_child(i)

		largest = left if left < heap_size and ary[left] > ary[i] else i
		largest = right if right < heap_size and ary[right] > ary[largest] else largest

		if i == largest:
			break
		ary[i], ary[largest] = ary[largest], ary[i]
		i = largest


def build_max_heap(ary):
	heap_size = len(ary)
	# 当下标1开始时，叶子节点是从 heap_size//2 + 1 开始，从 0 开始时，最后一个非叶子节点是 heap_size//2-1
	for i in range(heap_size//2-1, -1, -1):  # 自底向上
		heapify_loop(ary, i, heap_size)


def heap_sort(ary):
	build_max_heap(ary)
	heap_size = len(ary)

	for i in range(heap_size-1, -1, -1):
		ary[i], ary[0] = ary[0], ary[i]
		heap_size -= 1
		heapify(ary, 0, heap_size)


import heapq


def py_heap():
	ary = [5, 1, 3, 2, 2, 1]
	# heapq.heapify(ary)
	# print(ary)
	print(heapq.nlargest(3, ary))
	print(heapq.nsmallest(2, ary))



if __name__ == '__main__':
	# ary = [4, 3, 1, 2, 6]
	# # ary = []
	# heap_sort(ary)
	# print(ary)
	py_heap()