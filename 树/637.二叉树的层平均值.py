#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        average=[]
        if root:
            level=[root]
            while level:
                average.append(sum(i.val for i in level)/len(level))
                level=[kid for node in level for kid in (node.left,node.right) if kid]
        return average
