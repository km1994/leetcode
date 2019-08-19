#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/15 
@url：https://leetcode-cn.com/problems/maximum-subarray/
@desc:
    53. 最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:

    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''

class Solution:
    def __init__(self):
        pass
    
    def maxSubArray1(self, nums):
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i]>nums[i]:
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_

    def maxSubArray(self, nums):
        '''
        思路：
        最大连续子序列一定是以某个元素结尾的，那么我们就思考以nums中每个元素结尾的
        连续子序列其最大和是多少。
        status数组存以nums[i]结尾的子序列的最大和，那么当思考nums[i+1]结尾的子序列
        的最大和时，显然只要考虑两种情况，（1）是与以nums[i]结尾的最大子序列结合？
        （2）还是以自己nums[i+1]为子序列？
        '''
        status = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]+status[i-1] > nums[i]:
                status.append(nums[i]+status[i-1])
            else:
                status.append(nums[i])
        return max(status)


       

if __name__ == "__main__":

    print("--------1-------")
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    res=solution.maxSubArray(nums)
    print("res:{0}".format(res))

    