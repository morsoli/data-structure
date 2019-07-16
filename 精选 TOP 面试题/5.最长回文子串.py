#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        maxstr=0
        for i in range(len(s)):
            if i-maxstr>=1 and s[i-maxstr-1:i+1]==s[i-maxstr-1:i+1][::-1]:
                start = i-maxstr-1
                maxstr+=2
                continue
            if  i-maxstr>=0 and s[i-maxstr:i+1]==s[i-maxstr:i+1][::-1]:
                start = i-maxstr
                maxstr+=1
        return s[start:start+maxstr]
       