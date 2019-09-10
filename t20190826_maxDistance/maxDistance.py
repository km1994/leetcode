#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/26
@url：https://leetcode-cn.com/problems/subsets/
@desc:
    78. 已知三个升序整数数组a[l], b[m]和c[n]。
    请在三个数组中各找一个元素，使得组成的三元组距离最小。
    三元组的距离定义是：假设a[i]、b[j]和c[k]是一个三元组，那么距离为:
    Distance = max(|a[ I ] – b[ j ]|, |a[ I ] – c[ k ]|, |b[ j ] – c[ k ]|)
    请设计一个求最小三元组距离的最优算法，并分析时间复杂度。

'''
import math
class Solution:
    def maxDistance(self, nums1,nums2,nums3):
        max_distance = 0
        i = 0 
        j = 0
        k = 0
        while i < len(nums1) and j < len(nums2) and k < len(nums3):
            max_distance = max(max_distance,self.cal_max_distance(nums1[i],nums2[j],nums3[k]))
            min_pos = 0
            if nums1[i] > nums2[j]:
                if nums2[j] > nums3[k]:
                    min_pos = 2
                else:
                    min_pos = 1
            else:
                if nums1[i] > nums3[k]:
                    min_pos = 2
                else:
                    min_pos = 0
            if min_pos == 0:
                i = i + 1
            elif min_pos == 1:
                j = j + 1
            elif min_pos == 2:
                k = k + 1
        return max_distance

    def cal_max_distance(self,a,b,c):
        max_distance = math.fabs(a-b)
        if max_distance < math.fabs(c-b):
            max_distance = math.fabs(c-b)
        if max_distance < math.fabs(c-a):
            max_distance = math.fabs(c-a)

        return max_distance

        
if __name__ == "__main__":

    print("--------1-------")
    nums1 = [1,2,7]
    nums2 = [3,4,6,10]
    nums3 = [1,5,11,13]
    solution = Solution()
    res=solution.maxDistance(nums1,nums2,nums3)
    print("res:{0}".format(res))

    # print("--------2-------")
    # nums = []
    # solution = Solution()
    # res=solution.subsets(nums)
    # print("res:{0}".format(res))

    