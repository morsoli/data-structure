#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (45.34%)
# Total Accepted:    287.1K
# Total Submissions: 633.3K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        demo_dict = dict((num,i)for i,num in enumerate(nums))
        for i,num in enumerate(nums):
            #get() 方法和 [key] 方法的主要区别在于，[key] 在遇到不存在的 key 时会抛出 KeyError 错
            j=demo_dict.get(target-num)
            if j and i!=j:
                return [i,j]
