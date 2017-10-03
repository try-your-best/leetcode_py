# -*- coding: utf-8 -*-

from common.utils import TreeNode
from common.traverse_binary_tree import inorderWalk


def mirrorRecurse(pNode):
	if pNode is None:
		return

	if pNode.left is None and pNode.right is None:
		return

	pNode.left, pNode.right = pNode.right, pNode.left

	if pNode.left is not None:
		mirrorRecurse(pNode.left)

	if pNode.right is not None:
		mirrorRecurse(pNode.right)

"""
由于递归的本质是编译器生成了一个函数调用的栈，因此用循环来完成同样任务时最简单的办法就是
用一个辅助栈来模拟递归。首先我们把树的头结点放入栈中。在循环中，只要栈不为空，弹出栈的栈
顶结点，交换它的左右子树。如果它有左子树，把它的左子树压入栈中；如果它有右子树，把它的右
子树压入栈中。这样在下次循环中就能交换它儿子结点的左右子树了。参考代码如下：
"""

def mirrorLoop(pNode):
	if pNode is None:
		return
	stack = [pNode]

	while stack:
		pCur = stack.pop()
		pCur.left, pCur.right = pCur.right, pCur.left

		# 注意先右后左， 因为栈是先入后出
		if pCur.right is not None:
			stack.append(pCur.right)

		if pCur.left is not None:
			stack.append(pCur.left)


if __name__ == "__main__":
	def createTree():
		a1 = TreeNode(1)
		a2 = TreeNode(2)
		a3 = TreeNode(3)
		a4 = TreeNode(4)
		a5 = TreeNode(5)

		a1.left = a2
		a1.right = a3
		a2.left = a4
		a2.right = a5
		return a1

	# a1 = createTree()
	# inorderWalk(a1)
	# mirrorRecurse(a1)
	# inorderWalk(a1)

	a1 = createTree()
	inorderWalk(a1)
	mirrorLoop(a1)
	inorderWalk(a1)

