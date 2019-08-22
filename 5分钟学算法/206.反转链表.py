#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        # 不断取出和向后移动头节点,并将头节点连接到新头节点后面
        while head:
            next_node=head.next
            head.next=pre
            pre=head
            head=next_node
        return pre


