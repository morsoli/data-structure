#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict=dict((num,i) for i,num in enumerate(nums))
        for i,num in enumerate(nums):
            j=num_dict.get(target-num)
            if j and i!=j:
                return [i,j]

