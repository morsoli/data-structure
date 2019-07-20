#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[True] + [False] * m]
        for i in range(n):
            dp.append([False]*(m+1))
        for i in range(1, n + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, m+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[n][m]
