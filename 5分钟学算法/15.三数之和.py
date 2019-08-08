#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=list()
        N=len(nums)
        for i in range(N):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=nums[i]*(-1)
            left_p=i+1
            right_p=N-1
            while left_p<right_p:
                if nums[left_p]+nums[right_p]==target:
                    res.append([-target,nums[left_p],nums[right_p]])
                    left_p+=1
                    while left_p<right_p and nums[left_p]==nums[left_p-1]:
                        left_p+=1
                if nums[left_p]+nums[right_p]<target:
                    left_p+=1
                else:
                    right_p-=1
        return res

