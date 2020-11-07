from common.utils import *


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		last = 0
		dup_flag = False

		for i in range(1, len(nums)):
			if nums[last] == nums[i]:
				if not dup_flag:
					last += 1
					nums[last] = nums[i]
					dup_flag = True
			else:
				last += 1
				nums[last] = nums[i]
				dup_flag = False

		print(nums)
		return last + 1


if __name__ == '__main__':
	sl = Solution()
	print(sl.removeDuplicates([1,1,1,2,2,3]))
