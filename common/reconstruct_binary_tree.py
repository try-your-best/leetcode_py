# -*- coding: utf-8 -*-


"""
剑指offer第6题
https://github.com/L1nwatch/interview_collect/tree/master/%E5%89%91%E6%8C%87%20Offer%20%E7%BC%96%E7%A8%8B%E9%A2%98/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91

能重构的场景： 前序+中序， 后序+中序。 因为中序能提供左右孩子的数目。
"""

from traverse_binary_tree import TreeNode, preorderWalk, inorderWalk


def reconstructBinaryTree(preorder, inorder):
	if not preorder or not inorder:
		return None
	root = TreeNode(preorder[0])
	rootPos = inorder.index(root.value)

	leftLen = rootPos
	rightLen = len(inorder) - rootPos - 1

	# 比该索引值小的为左子树
	if leftLen > 0:
		root.left = reconstructBinaryTree(preorder[1:leftLen+1], inorder[:leftLen])

	if rightLen > 0:
		root.right = reconstructBinaryTree(preorder[leftLen+1:], inorder[leftLen+1:])

	return root

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

	preorder = [1, 2, 4, 5, 3]
	inorder = [4, 2, 5, 1, 3]
	tree = reconstructBinaryTree(preorder, inorder)
	preorderWalk(tree)
	inorderWalk(tree)

