#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder==[]:
            return None
        # 找到根节点在中序遍历中的位置(索引)
        index=inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        # 递归调用
        root.left=self.buildTree(preorder[1:index+1],inorder[0:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
