from common.utils import *


class Solution:
	def rob(self, root: TreeNode) -> int:
		node_map = {}
		return self._dfs(root, node_map)

	def _dfs(self, root: TreeNode, node_map):
		if not root:
			return 0
		if root in node_map:
			return node_map[root]

		val = 0
		if root.left:
			left_val = self._dfs(root.left.left, node_map) + self._dfs(root.left.right, node_map)
			val += left_val
		if root.right:
			right_val = self._dfs(root.right.left, node_map) + self._dfs(root.right.right, node_map)
			val += right_val
		max_val = max(val + root.val, self._dfs(root.left, node_map) + self._dfs(root.right, node_map))
		# if root.left:
			# print("left={}".format(left_val))
		# if root.right:
		# 	print("right={}".format(right_val))
		# print("root_val={}".format(root.val), max_val, val + root.val, self._dfs(root.left, node_map) + self._dfs(root.right, node_map))
		node_map[root] = max_val
		return max_val


if __name__ == '__main__':
	sl = Solution()
	a = TreeNode(3)
	b = TreeNode(2)
	c = TreeNode(3)
	d = TreeNode(3)
	e = TreeNode(1)
	a.left = b
	a.right = c
	b.right = d
	c.right = e
	print(sl.rob(a))
