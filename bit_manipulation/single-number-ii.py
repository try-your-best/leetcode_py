from common.utils import *


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		res = 0
		for i in range(0, 32):
			sum_n = 0
			for n in nums:
				sum_n += (n >> i) & 1
			# print(sum_n)
			res += (sum_n % 3) << i

		if (res >> 31) & 1 == 1:  # python 的 int 不是 32 位，要处理负数情况
			res = res | (-1 << 32)
			# res |= (sum_n % 3) << i
		return res


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		one = 0  # Int 各个位上 1 出现 1 次的掩码
		two = 0
		three = 0
		for n in nums:
			two |= one & n  # 注意，这里用 |=，而不是 =，two 原先表示两次 1 的状态要保留
			one ^= n
			three = one & two
			one &= ~ three
			two &= ~ three
		return one


if __name__ == '__main__':
	sl = Solution()
	print(sl.singleNumber([2,2,3,2]))
	print(sl.singleNumber([0,1,0,1,0,1,99]))
	print(sl.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
	# print(-1>>5)
	# print(2 >>2)

