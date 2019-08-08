#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        chars={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in chars:
                stack.append(i)
            else:
                if not stack or chars[stack.pop()]!=i:
                    return False
        return not stack
