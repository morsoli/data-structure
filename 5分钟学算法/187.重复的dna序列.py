#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=dict()
        for i in range(len(s)-9):
            res[s[i:i+10]]=res.get(s[i:i+10],0)+1
        return [k for k,v in res.items() if v>=2]

