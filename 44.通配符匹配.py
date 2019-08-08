#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return re.match('^'+p+'$',s)!=None

