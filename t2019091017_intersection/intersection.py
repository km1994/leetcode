#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/17
@url：https://leetcode-cn.com/problems/intersection-of-two-arrays/
@desc:
    
    349. 两个数组的交集

    给定两个数组，编写一个函数来计算它们的交集。

    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [9,4]
    说明:

    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。

'''
import math
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        new_nums = []

        for num1 in nums1:
            if num1 in nums2:
                new_nums.append(num1)
        return new_nums

            
if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    res=solution.intersection(nums1,nums2)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    res=solution.intersection(nums1,nums2)
    print("res:{0}".format(res))

    

    