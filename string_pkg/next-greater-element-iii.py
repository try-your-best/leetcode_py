

"""
https://www.cnblogs.com/grandyang/p/6716130.html
跟 next permutation 原理相同
https://www.cnblogs.com/grandyang/p/4428207.html
"""

class Solution:
	def nextGreaterElement(self, n: int) -> int:
		n_list = [int(x) for x in str(n)]
		for i in range(len(n_list)-2, -1, -1):
			if n_list[i] >= n_list[i+1]:  # 注意等于号
				continue
			for j in range(len(n_list)-1, i, -1):
				if n_list[j] > n_list[i]:
					n_list[j], n_list[i] = n_list[i], n_list[j]
					break
			k = i + 1
			w = len(n_list) - 1
			while k < w:
				n_list[k], n_list[w] = n_list[w], n_list[k]
				k += 1
				w -= 1
			ret = int("".join([str(x) for x in n_list]))  # 注意，限制 32 bit
			if ret > 2**31:
				ret = -1
			return ret

		return -1


if __name__ == '__main__':
	sl =Solution()
	# print(sl.nextGreaterElement(12))
	# print(sl.nextGreaterElement(21))
	# print(sl.nextGreaterElement(127431)) # 127431 => 131247
	# print(sl.nextGreaterElement(11)) # 11 => -1
	print(sl.nextGreaterElement(1999999999))  # 11 => -1
	# print(2**31)