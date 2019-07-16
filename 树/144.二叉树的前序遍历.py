#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret=[]
        if root==None:
            return ret
        stack=[]
        curr=root
        while curr or stack:
            if curr:
                ret.append(curr.val)
                stack.append(curr.right)
                curr=curr.left
            else:
                curr=stack.pop()
        return ret
