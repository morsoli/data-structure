#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter=0
        def get_diamater(root):
            if root==None:
                return 0
            left=get_diamater(root.left)
            right=get_diamater(root.right)
            self.diameter=max(self.diameter,left+right)
            return max(left,right)+1
        get_diamater(root)
        return self.diameter

