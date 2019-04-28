#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root=ListNode(None)
        cur=root
        while l1 and l2:
            if l1.val<l2.val:
                node=ListNode(l1.val)
                l1=l1.next
            else:
                node=ListNode(l2.val)
                l2=l2.next
            cur.next=node
            cur=node
        cur.next=l1 or l2
        return root.next

