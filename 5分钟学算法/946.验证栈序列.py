#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tmp=[]
        while pushed:
            tmp.append(pushed.pop(0))
            while tmp and tmp[-1]==popped[0]:
                popped.pop(0)
                tmp.pop()
        return not tmp

