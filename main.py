from common.utils import TreeNode
from typing import List


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		"""
		:type citations: List[int]
		:rtype: int
		"""
		# 这里排的是论文数
		# 注意，这里做了优化，是 len(citations)， 而不是 max（citations）
		n = len(citations)
		count = [0] * (n+1)

		for x in citations:
			if x >= n:
				count[n] += 1
			else:
				count[x] += 1

		h = 0
		


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	a.right = b
	b.left = c
	print(sl.inorderTraversal(a))
	# print(sl.containsNearbyDuplicate([1,2,3,1], 3))
	# print(sl.containsNearbyDuplicate([1,0,1,1], 1))
	# print(sl.containsNearbyDuplicate([1,2,3,1,2,3], 2))

	# print(19%10)
	# print(sl.containsNearbyDuplicate([1,2,3,1], 3))
	# print(sl.containsNearbyDuplicate([1,0,1,1], 1))
	# print(sl.containsNearbyDuplicate([1,2,3,1,2,3], 2))
	# print sl.lengthOfLongestSubstring("bbbbb")
	# print sl.lengthOfLongestSubstring("pwwkew")
	# print sl.lengthOfLongestSubstring("abba")