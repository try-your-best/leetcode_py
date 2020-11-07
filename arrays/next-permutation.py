from common.utils import *


class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		for i in range(len(nums)-2, -1, -1):
			if nums[i] < nums[i+1]:
				for j in range(len(nums)-1, i, -1):
					if nums[j] > nums[i]:
						nums[i], nums[j] = nums[j], nums[i]
						self._reverse(nums, i+1, len(nums)-1)
						return
		self._reverse(nums, 0, len(nums)-1)

	def _reverse(self, nums: List[int], begin, end) -> None:
			while begin < end:
				nums[begin], nums[end] = nums[end], nums[begin]
				begin += 1
				end -= 1


if __name__ == '__main__':
	sl = Solution()

	nums = [1, 2, 3]
	sl.nextPermutation(nums)
	print(nums)

	nums = [1, 2, 7, 4, 3, 1]
	sl.nextPermutation(nums)
	print(nums)