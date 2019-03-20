#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.34%)
# Total Accepted:    99.4K
# Total Submissions: 298.1K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=None
        currentNode=None
        carry =0
        isFirst = True
        while(l1 or l2 or carry!=0):
            val1=0
            val2=0
            if l1:
                val1=l1.val
                l1=l1.next
            if l2:
                val2=l2.val
                l2=l2.next
            sum=val1+val2+carry
            if sum>=10:
                carry=1
                sum=sum%10
            else:
                carry=0
            node = ListNode(sum)
            if isFirst:
                currentNode=node
                head = currentNode
                isFirst=False
            else:
                currentNode.next=node
                currentNode=currentNode.next
        return head
