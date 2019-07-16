#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output=[]
        self.inOrder(root,output)
        for i in range(1,len(output)):
            if output[i-1]>=output[i]:
                return False
        return True
    def inOrder(self,root,output):
        if root==None:
            return
        # 利用中序遍历，自下而上升序排列
        self.inOrder(root.left,output)
        output.append(root.val)
        self.inOrder(root.right,output)

