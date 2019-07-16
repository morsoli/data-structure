#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_depth(root):
            if root==None:
                return 0
            left_depth=check_depth(root.left)
            right_depth=check_depth(root.right)
            return max(left_depth,right_depth)+1
        if root==None:
            return True
        return abs(check_depth(root.left)-check_depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
