#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level=[root]
        ret=[]
        if root==None:
            return []
        while level:
            ret.append([i.val for i in level])
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return ret

