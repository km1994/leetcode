#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: myPow.py
@time: 2019/7/09
@rel： https://leetcode-cn.com/problems/first-missing-positive/
@url：
@desc:
    41. 缺失的第一个正数
    给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

    示例 1:
        输入: [1,2,0]
        输出: 3

    示例 2:
        输入: [3,4,-1,1]
        输出: 2

    示例 3:
        输入: [7,8,9,11,12]
        输出: 1


'''


class Solution:
    def __init__(self):
        pass

    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1

        max_val = max(nums)

        for i in range(1, max_val + 2):
            if i not in nums:
                return i
        return 1

    def max(self,nums):
        max = 0
        for num in  nums:
            if max < num:
                max = num
        return max


if __name__ == "__main__":
    nums1 = [1,2,0]
    nums2 = [3,4,-1,1]
    nums3 = [7,8,9,11,12]
    nums4 = []
    solution = Solution()
    res1 = solution.firstMissingPositive(nums1)
    print("res1:{0}".format(res1))

    res2 = solution.firstMissingPositive(nums2)
    print("res2:{0}".format(res2))

    res3 = solution.firstMissingPositive(nums3)
    print("res3:{0}".format(res3))

    res4 = solution.firstMissingPositive(nums4)
    print("res4:{0}".format(res4))


    

