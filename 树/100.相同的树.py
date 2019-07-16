#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            # p,q 不为空且值相等，递归比较子节点
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q
