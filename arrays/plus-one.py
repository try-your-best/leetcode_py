
from common.utils import *


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		for i in range(len(digits)-1, -1, -1):
			if digits[i] < 9:
				digits[i] += 1
				break
			else:
				digits[i] = 0
				if i == 0:
					digits.insert(0, 1)

		return digits


if __name__ == '__main__':
	sl = Solution()
	print(sl.plusOne([4,3,2,1]))
	print(sl.plusOne([9]))
	print(sl.plusOne([9, 9]))