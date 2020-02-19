# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		if not nums:
			return []
		nums.sort()
		result = []

		for k in range(len(nums)):
			if nums[k] > 0:
				break
			if nums[k] == [k+1]:
				continue
			target = 0 - nums[k]
			i = k+1
			j = len(nums)-1

			while i < j:
				if nums[i] + nums[j] == target:
					result.append([nums[k], nums[i], nums[j]])
					i -= 1
					j -= 1
					while nums[i] == nums[i+1]:
						i += 1
					while nums[j] == nums[j-1]:
						j -= 1
				elif nums[i] + nums[j] < target:
					i += 1
				else:
					j -= 1

		return result


if __name__ == '__main__':
	sl = Solution()
	# nums = [-1, 1, 0, 2]
	nums = [-1,0,1,2,-1,-4]
	print(sl.threeSum(nums))
