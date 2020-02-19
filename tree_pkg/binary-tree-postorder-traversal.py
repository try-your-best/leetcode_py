# -*- coding: utf-8 -*-
__author__ = 'damon'

from common.utils import TreeNode
from typing import List


class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		ret = []
		self._postorderTraversal(root, ret)
		return ret

	def _postorderTraversal(self, root: TreeNode, ret: List[int]):
		if root is None:
			return
		self._postorderTraversal(root.left, ret)
		self._postorderTraversal(root.right, ret)
		ret.append(root.val)


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(1)
	b = TreeNode(2)
	c = TreeNode(3)
	a.right = b
	b.left = c

	print(sl.postorderTraversal(a))