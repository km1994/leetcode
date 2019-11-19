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
    35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

    你可以假设数组中无重复元素。

    示例 1:
        输入: [1,3,5,6], 5
        输出: 2
    示例 2:
        输入: [1,3,5,6], 2
        输出: 1
    示例 3:
        输入: [1,3,5,6], 7
        输出: 4
    示例 4:
        输入: [1,3,5,6], 0
        输出: 0


'''

class Solution:
    def __init__(self):
        pass

    def searchInsert1(self, nums, target):
        nums_len = len(nums)
        if nums_len == 0:
            return 0

        for i in range(0, nums_len):
            if target <= nums[i]:
                return i
        return nums_len

if __name__ == "__main__":
    nums1 = [1,3,5,6]
    target1 = 5
    nums2 = [1,3,5,6]
    target2 = 2
    nums3 = [1,3,5,6]
    target3 = 7
    nums4 = [1,3,5,6]
    target4 = 0
    solution = Solution()
    res1 = solution.searchInsert(nums1,target1)
    print("res1:{0}".format(res1))

    res2 = solution.searchInsert(nums2,target2)
    print("res2:{0}".format(res2))

    res3 = solution.searchInsert(nums3,target3)
    print("res3:{0}".format(res3))

    res4 = solution.searchInsert(nums4,target4)
    print("res4:{0}".format(res4))


    

