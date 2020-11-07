from common.utils import *

"""
https://www.cnblogs.com/grandyang/p/6932727.html
一个元素只能在一个嵌套中。可以根据是否访问过该元素优化计算
"""

class Solution:
	def arrayNesting(self, nums: List[int]) -> int:
		visit = set()
		max_len = 0
		for i in range(len(nums)):
			max_len = max(max_len, self._nest(nums, i, visit))

		return max_len

	def _nest(self, nums: List[int], start, visit:Set[int]):
		cur_set = set()
		val = nums[start]

		while val not in visit:
			visit.add(val)

			if val not in cur_set:
				cur_set.add(val)
				start = val
				val = nums[start]
			else:
				break

		return len(cur_set)


if __name__ == '__main__':
	sl = Solution()
	print(sl.arrayNesting([5,4,0,3,1,6,2]))