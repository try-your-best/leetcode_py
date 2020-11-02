# -*- coding: utf-8 -*-
__author__ = 'damon'

from typing import List


class NumArray(object):

	def __init__(self, nums: List[int]):
		"""
		:type nums: List[int]
		"""
		self.nums = nums

	def update(self, i: int, val: int) -> None:
		"""
		:type i: int
		:type val: int
		:rtype: None
		"""
		self.nums[i] = val

	def sumRange(self, i: int, j: int) -> int:
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return sum(self.nums[i:j+1])


class SegmentTreeNode:
	def __init__(self, start, end, val):
		self.start = start
		self.end = end
		self.val = val
		self.left = None
		self.right = None

	@staticmethod
	def build(nums: List[int]):
		return SegmentTreeNode._build(0, len(nums)-1, nums)

	@staticmethod
	def _build(left:int, right:int, nums: List[int]):
		if left > right:
			return None
		root = SegmentTreeNode(left, right, None)
		if left == right:
			root.val = nums[left]
			return root

		mid = (left + right) // 2
		root.left = SegmentTreeNode._build(left, mid, nums)
		root.right = SegmentTreeNode._build(mid+1, right, nums)
		root.val = root.left.val + root.right.val
		return root


class NumArray(object):

	def __init__(self, nums: List[int]):
		"""
		:type nums: List[int]
		"""
		# self.nums = nums
		self.root = SegmentTreeNode.build(nums)

	def update(self, i: int, val: int) -> None:
		"""
		:type i: int
		:type val: int
		:rtype: None
		"""
		self._update(i, val, self.root)

	def _update(self, i: int, val: int, root:SegmentTreeNode):
		if root.left == root.right:
			root.val = val
			return
		mid = (root.start + root.end) // 2
		if i <= mid:
			self._update(i, val, root.left)
		else:
			self._update(i, val, root.right)
		root.val = root.left.val + root.right.val

	def sumRange(self, i: int, j: int) -> int:
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		return self._sumRange(i, j, self.root)

	def _sumRange(self, i: int, j: int, root:SegmentTreeNode):
		if i > root.end or j < root.start:
			return 0
		elif i <= root.start and root.end <= j:
			return root.val

		mid = (root.start + root.end) // 2
		if j <= mid:
			return self._sumRange(i, j, root.left)
		elif i > mid:
			return self._sumRange(i, j, root.right)
		else:
			return self._sumRange(i, j, root.left) + self._sumRange(i, j, root.right)


if __name__ == '__main__':
	na = NumArray([1, 3, 5, 7])
	print(na.sumRange(0, 2))
	print(na.sumRange(0, 3))
	na.update(1, 2)
	print(na.sumRange(0, 2))
	print(na.sumRange(0, 3))