# -*- coding: utf-8 -*-


from .utils import TreeNode


def preorderWalk(node):
	if node is not None:
		print(node.value)
		preorderWalk(node.left)
		preorderWalk(node.right)


def preorderWalkLoop(node):
	nodeStack = []
	while node or nodeStack:
		while node:  # 注意是 while 并且与最外层while循环顺序的对应
			print(node.value)
			nodeStack.append(node)
			node = node.left

		if nodeStack:  # 注意是 if 并且与最外层while循环顺序的对应
			node = nodeStack.pop()
			node = node.right


def inorderWalk(node):
	if node is not None:
		inorderWalk(node.left)
		print(node.value)
		inorderWalk(node.right)


def inorderWalkLoop(node):
	nodeStack = []
	while node or nodeStack:
		while node:  # 注意是 while 并且与最外层while循环顺序的对应
			nodeStack.append(node)
			node = node.left

		if nodeStack:  # 注意是 if 并且与最外层while循环顺序的对应
			node = nodeStack.pop()
			print(node.value)
			node = node.right


def postorderWalk(node):
	if node is not None:
		postorderWalk(node.left)
		postorderWalk(node.right)
		print(node.value)


def postorderWalkLoop(node):
	"""
	记住第一种。这种的方法与前面先序和中序的非递归形式是一致的。
	:param node:
	:return:
	"""
	nodeStack = []
	preVisited = None

	while node or nodeStack:
		while node:  # 注意是 while 并且与最外层while循环顺序的对应
			nodeStack.append(node)
			node = node.left

		if nodeStack:  # 注意是 if 并且与最外层while循环顺序的对应
			node = nodeStack[-1]
			# 当前节点的右孩子如果为空或者已经被访问，则访问当前节点
			if node.right is None or node.right == preVisited:
				print(node.value)
				preVisited = node
				node = None  # 注意， 设置为 None， 找栈顶元素
				nodeStack.pop()
			else:
				node = node.right


if __name__ == "__main__":
	a1 = TreeNode(1)
	a2 = TreeNode(2)
	a3 = TreeNode(3)
	a4 = TreeNode(4)
	a5 = TreeNode(5)

	a1.left = a2
	a1.right = a3
	a2.left = a4
	a2.right = a5

	# preorderWalk(a1)
	# preorderWalkLoop(a1)

	# inorderWalk(a1)
	# inorderWalkLoop(a1)

	postorderWalk(a1)
	postorderWalkLoop(a1)
