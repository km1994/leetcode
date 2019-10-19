#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/17
@url：https://leetcode-cn.com/problems/maximum-product-subarray/
@desc:
    
    152. 乘积最大子序列

    给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

    示例 1:
        输入: [2,3,-2,4]
        输出: 6
        解释: 子数组 [2,3] 有最大乘积 6。
    示例 2:
        输入: [-2,0,-1]
        输出: 0
        解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

'''
import math
class Solution:
    def maxProduct(self, nums):
        max_val = -9999
        imax = 1
        imin = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])

            max_val = max(max_val,imax)
        return max_val
            
if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = [2,3,-2,4]
    res=solution.maxProduct(nums1)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = [-2,3,-4]
    res=solution.maxProduct(nums1)
    print("res:{0}".format(res))

    print("--------3-------")
    nums1 = [-4,-3]
    res=solution.maxProduct(nums1)
    print("res:{0}".format(res))

    print("--------4-------")
    nums1 = [-2]
    res=solution.maxProduct(nums1)
    print("res:{0}".format(res))

    