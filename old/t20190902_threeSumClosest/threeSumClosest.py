#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/31
@url：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
@desc:
    16. 最接近的三数之和
    
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。

    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

'''
import math

class Solution:

    def threeSumClosest(self, nums, target):
        nums.sort()
        closeSum = nums[0] + nums[1] +nums[2]
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] +nums[r]
                if math.fabs(target - s) < math.fabs(target - closeSum):
                    closeSum = s
                elif s > target:
                    r -=1
                elif s < target:
                    l +=1
                else:
                    return closeSum
        return closeSum



if __name__ == "__main__":

    print("--------1-------")
    nums = [-1,2,1,-4]
    target = 1
    solution = Solution()
    res=solution.threeSumClosest(nums, target)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = [1,1,1,0]
    target = -100
    solution = Solution()
    res=solution.threeSumClosest(nums, target)
    print("res:{0}".format(res))


    print("--------3-------")
    nums = [0,2,1,-3]
    target = 1
    solution = Solution()
    res=solution.threeSumClosest(nums, target)
    print("res:{0}".format(res))

    