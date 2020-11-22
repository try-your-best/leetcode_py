# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/4032934.html
这道寻找旋转有序数组的最小值肯定不能通过直接遍历整个数组来寻找，这个方法过于简单粗暴，这样的话，旋不旋转就没有意义。
应该考虑将时间复杂度从简单粗暴的 O(n) 缩小到 O(lgn)，这时候二分查找法就浮现在脑海。这里的二分法属于博主之前的总结帖 
LeetCode Binary Search Summary 二分搜索法小结 中的第五类，也是比较难的那一类，没有固定的 target 值比较，
而是要跟数组中某个特定位置上的数字比较，决定接下来去哪一边继续搜索。这里用中间的值 nums[mid] 和右边界值 nums[right] 
进行比较，若数组没有旋转或者旋转点在左半段的时候，中间值是一定小于右边界值的，所以要去左半边继续搜索，
反之则去右半段查找，最终返回 nums[right]
"""

class Solution:
	def findMin(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		low = 0
		high = len(nums)-1
		while low <= high:
			mid = (low+high) // 2
			if mid > 0:
				if nums[mid] < nums[mid-1]:
					return nums[mid]
				else:
					if nums[low] <= nums[mid] > nums[high]: # 这里的等于号是因为，(low+high) // 2 会向下取整，low high 相邻时，low == mid
						low = mid + 1
					else:
						high = mid - 1
			else:
				low = mid + 1
		return nums[low-1]


"""
这样会简洁，但难想
"""
class Solution:
	def findMin(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2
			if nums[mid] > nums[high]:
				low = mid + 1
			else:
				high = mid
		# print(low, high)
		return nums[high]


if __name__ == '__main__':
	sl = Solution()
	print(sl.findMin([3,4,5,1,2]))
	print(sl.findMin([4,5,6,7,0,1,2]))
	print(sl.findMin([3,1,2]))
	print(sl.findMin([3,1]))
	print(sl.findMin([1]))
	print(sl.findMin([1, 2])) # 1
	print(sl.findMin([2,3,4,5,1])) # 1