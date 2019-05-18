#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/4/23 11:56
@url： https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
@desc:
    34. 在排序数组中查找元素的第一个和最后一个位置
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:
        输入: nums = [5,7,7,8,8,10], target = 8
        输出: [3,4]
    示例 2:
        输入: nums = [5,7,7,8,8,10], target = 6
        输出: [-1,-1]
'''


class Solution:
    def __init__(self):
        pass

    def searchRange(self, nums, target):
        l_flag=0
        r_flag = 0
        l = 0
        r = len(nums)-1
        while l <= r and (l_flag == 0 or r_flag==0):
            if nums[l] == target:
                l_flag = 1
            else:
                l=l+1

            if nums[r] == target:
                r_flag=1
            else:
                r = r - 1

        if l_flag == 0 and r_flag==0:
            res = [-1,-1]
        else:
            res=[l,r]
        return res

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    solution = Solution()
    res = solution.searchRange(nums,target)
    print("res:{0}".format(res))


