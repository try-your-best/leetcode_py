
class Solution:
	def hammingDistance(self, x: int, y: int) -> int:
		n = x ^ y
		n_sum = 0
		for i in range(32):
			n_sum += (n >> i) & 1
		return n_sum


if __name__ == '__main__':
	sl = Solution()
	print(sl.hammingDistance(1, 4))