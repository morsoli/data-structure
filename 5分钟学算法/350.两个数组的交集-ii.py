#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        num_dict={}
        for num in nums1:
            if num not in num_dict:
                num_dict[num]=1
            else:
                num_dict[num]+=1
        for num in nums2:
            if num in num_dict and num_dict[num]>0:
                num_dict[num]-=1
                res.append(num)
        return res

