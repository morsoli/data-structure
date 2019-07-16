#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        count=0
        if root:
            level=[root]
            while level:
                count+=len(level)
                level=[kid for node in level for kid in (node.left,node.right) if kid]
        return count

