from common.utils import *


class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		if numRows == 0:
			return []
		res = [[1]]
		for i in range(1, numRows):
			cur = [1] * (i+1)
			for j in range(1, i):
				cur[j] = res[i-1][j-1] + res[i-1][j]

			res.append(cur)

		return res


if __name__ == '__main__':
	sl = Solution()
	res = sl.generate(5)
	for r in res:
		print(r)