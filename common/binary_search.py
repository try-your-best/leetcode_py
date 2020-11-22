# -*- coding: utf-8 -*-

"""
https://www.cnblogs.com/grandyang/p/6854825.html
"""

def binarySearch(ary, t):
	low = 0
	high = len(ary) - 1

	# 注意等于的情况
	while low <= high:
		mid = int(low+(high - low)/2)  # 不写成 (high+low)/2 是为了防止溢出

		if ary[mid] < t:
			low = mid + 1
		elif ary[mid] > t:
			high = mid - 1
		else:
			return mid

	return -1

"""
第二类： 查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数
"""
def findFirstGreater(nums, target):
	left = 0
	right = len(nums)  # target 有可能比序列中任何值大，这里初始值要是 len(nums)
	while left < right:
		mid = (right+left) // 2
		if nums[mid] < target:
			left = mid + 1
		else:
			right = mid
	return right


"""
第三类： 查找第一个大于目标值的数，可变形为查找最后一个不大于目标值的数
"""
def findLastLesser(nums, target):
	left = 0
	right = len(nums)
	while left < right:
		mid = (right+left) // 2
		if nums[mid] <= target:
			left = mid + 1
		else:
			right = mid
	return right


def fun1():
	ary = [1, 3, 6, 7, 10]
	print(binarySearch(ary, 6))
	ary = ([1, 2, 4, 6, 10])
	print(binarySearch(ary, 10))
	ary = [1, 2]
	print(binarySearch(ary, 6))


def fun2():
	ary = [2, 4, 5, 6, 9]
	print(findFirstGreater(ary, 3))
	print(findFirstGreater(ary, 10))
	print(findFirstGreater(ary, 0))


def fun3():
	ary = [2, 4, 5, 6, 9]
	print(findLastLesser(ary, 3))


if __name__ == '__main__':
	fun3()
