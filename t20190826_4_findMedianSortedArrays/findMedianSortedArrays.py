#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/26
@url：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
@desc:
    4. 寻找两个有序数组的中位数
    
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:

        nums1 = [1, 3]
        nums2 = [2]

        则中位数是 2.0
    示例 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        则中位数是 (2 + 3)/2 = 2.5


'''
import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len == 0:
            if nums2_len%2 == 0:
                return (nums2[int(nums2_len/2)]+nums2[int(nums2_len/2-1)])/2
            else:
                return nums2[int(nums2_len/2)]
        if nums2_len == 0:
            if nums1_len%2 == 0:
                return (nums1[int(nums1_len/2)]+nums1[int(nums1_len/2-1)])/2
            else:
                return nums1[int(nums1_len/2)]
        
        pre = 0
        new = nums1[start1] if nums1[start1]<nums2[start2] else nums2[start2]
        start1 = 0
        start2 = 0
        count = 0
        median_pos = int((nums1_len+nums2_len)/2)
        while count < median_pos and start1 < nums1_len and start2 < nums2_len:
            if nums1[start1]<nums2[start2]:
                pre = new
                new = nums1[start1]
                start1 = start1 + 1
            else:
                pre = new
                new = nums2[start2]
                start2 = start2 + 1

if __name__ == "__main__":

    print("--------1-------")
    nums1 = [1,4,8]
    nums2 = []
    solution = Solution()
    res=solution.findMedianSortedArrays(nums1,nums2)
    print("res:{0}".format(res))

    
    print("--------2-------")
    nums1 = []
    nums2 = [1,2,5,8]
    solution = Solution()
    res=solution.findMedianSortedArrays(nums1,nums2)
    print("res:{0}".format(res))
    sys.exit(0)

    print("--------3-------")
    nums1 = [1,4,8]
    nums2 = [1,2,5]
    solution = Solution()
    res=solution.findMedianSortedArrays(nums1,nums2)
    print("res:{0}".format(res))

    