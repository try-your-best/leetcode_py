from common.utils import *

# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(1)

class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		begin = 0
		end = len(nums)-1
		m = self._partition(nums, begin, end)
		k_idx = k - 1
		while m != k_idx:
			if m < k:
				begin = m + 1
				m = self._partition(nums, begin, end)
			else:
				end = m - 1
				m = self._partition(nums, begin, end)

		return nums[m]

	def _partition(self, nums, begin, end):
		i = begin - 1
		p = nums[end]
		for j in range(begin, end):
			if nums[j] > p:
				i += 1
				nums[i], nums[j] = nums[j], nums[i]

		i += 1
		nums[i], nums[end] = nums[end], nums[i]

		return i


if __name__ == '__main__':
	sl = Solution()
	print(sl.findKthLargest([3,2,1,5,6,4], 2))
	print(sl.findKthLargest([3,2,3,1,2,4,5,5,6], 4))