#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
class Solution:
    def numTrees(self, n: int) -> int:
        # n=0,n=1的情况
        g=[1,1]
        for i in range(2,n+1):
            f=0
            for j in range(1,i+1):
                #若n为4：g[0]*g[3]+g[1]*g[2]+g[2]*g[1]+g[3]*g[0]
                f+=g[j-1]*g[i-j]
            g.append(f)
        return g[-1]

