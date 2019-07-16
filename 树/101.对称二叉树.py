#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(l,r):
            if not l and not r:
                return True
            if l and r and l.val==r.val:
                return isSym(l.left,r.right) and isSym(l.right,r.left)
            return False
        return isSym(root,root)
