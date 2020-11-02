# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List

"""
https://www.cnblogs.com/grandyang/p/6529857.html

这道题给了我们一个二进制的数组，让找邻近的子数组使其0和1的个数相等。对于求子数组的问题，需要时刻记着求累积和是一种很犀利的工具，但是这里怎么将子数组的和跟0和1的个数之间产生联系呢？
这里需要用到一个 trick，遇到1就加1，遇到0，就减1，这样如果某个子数组和为0，就说明0和1的个数相等，这个想法真是太叼了，不过博主木有想出来。知道了这一点，
就用一个 HashMap 建立子数组之和跟结尾位置的坐标之间的映射。如果某个子数组之和在 HashMap 里存在了，说明当前子数组减去 HashMap 中存的那个子数字，得到的结果是中间一段子数组之和，
必然为0，说明0和1的个数相等，更新结果 res。注意这里需要在 HashMap 初始化一个 0 -> -1 的映射，这是为了当 sum 第一次出现0的时候，即这个子数组是从原数组的起始位置开始，
需要计算这个子数组的长度，而不是建立当前子数组之和 sum 和其结束位置之间的映射。比如就拿例子1来说，nums = [0, 1]，当遍历0的时候，sum = -1，此时建立 -1 -> 0 的映射，
当遍历到1的时候，此时 sum = 0 了，若 HashMap 中没有初始化一个 0 -> -1 的映射，此时会建立 0 -> 1 的映射，而不是去更新这个满足题意的子数组的长度，所以要这么初始化，参见代码如下：
"""


class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		lookup = {0: -1}
		sum = 0
		max_len = 0
		for idx, n in enumerate(nums):
			sum += (1 if n == 1 else -1)
			if sum in lookup:
				max_len = max(max_len, idx-lookup[sum])
			else:
				lookup[sum] = idx

		return max_len


if __name__ == '__main__':
	sl = Solution()
	print(sl.findMaxLength([0,1]))
	print(sl.findMaxLength([0,1,0]))
	print(sl.findMaxLength([0,1,0,1,1,0,0]))