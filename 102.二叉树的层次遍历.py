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
        if root is None:
            return []
        res=[]
        cur_codes=[root]
        next_nodes=[]
        res.append([i.val for i in cur_codes])
        while cur_codes or next_nodes:
            for node in cur_codes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                res.append([i.val for i in next_nodes])
            cur_codes=next_nodes
            next_nodes=[]
        return res
