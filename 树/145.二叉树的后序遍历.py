#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ret=[]
        if root==None:
            return ret
        stack=[]
        curr=root
        while curr or stack:
            if curr:
                ret.append(curr.val)
                stack.append(curr.left)
                curr=curr.right
            else:
                curr=stack.pop()
        return ret[::-1]
