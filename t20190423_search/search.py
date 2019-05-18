#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/4/23 11:56
@url： https://leetcode-cn.com/problems/next-permutation/
@desc:
    33. 搜索旋转排序数组
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。

    示例 1:
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
    示例 2:
        输入: nums = [4,5,6,7,0,1,2], target = 3
        输出: -1
'''

import math

class Solution:
    def __init__(self):
        pass

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
            # 我的二分法如果未找到target返回的是0，而且ans是累加出来的，所以需要先判断第0位就是target的情况。
        if nums[0] == target:
            return 0

        ans = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[l] <= nums[mid] and nums[mid + 1] <= nums[r]:
                ans += self.Bisectionmethod(nums, target, l, mid)
                ans += self.Bisectionmethod(nums, target, mid + 1, r)
                break
            elif nums[l] <= nums[mid]:
                ans += self.Bisectionmethod(nums, target, l, mid)
                l = mid + 1
            else:
                ans += self.Bisectionmethod(nums, target, mid + 1, r)
                r = mid
        if ans:
            return ans
        else:
            return -1

    def Bisectionmethod(self, nums, target, l, r):
        mid = l + (r - l) // 2
        while l <= r:
            mid = l + (r - l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        if nums[mid] == target:
            return mid
        else:
            return 0

    def print_fun(self,name,val):
        print("{0}:{1}".format(name,val))


if __name__ == "__main__":
    arrs1=[4,5,6,7,0,1,2]
    arrs2=[7,8,1,2,3,4,5,6]
    arrs3=[4,5,6,7,0,1,2]
    arrs4=[1]
    arrs5=[1,3,5]
    target = 1
    solution = Solution()
    res = solution.search(arrs2,target)
    solution.print_fun("res",res)


