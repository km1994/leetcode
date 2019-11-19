#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: nextPermutation.py
@time: 2019/4/19 11:56
@url： https://leetcode-cn.com/problems/next-permutation/
@desc:
    31. 下一个排列
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

    必须原地修改，只允许使用额外常数空间。

    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
'''

import math

class Solution:
    def __init__(self):
        pass

    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print("origin nums:{0}".format(nums))
        n = len(nums)
        max_num = nums[-1]
        sign = True
        for i in range(2, n + 1):
            if nums[-i] < nums[-i + 1]:
                sign = False
                j = -i + 1
                while j < 0:
                    if nums[j] <= nums[-i]:
                        break
                    j += 1
                break
        if sign:
            nums.reverse()
            print("nums1:{0}".format(nums))
        else:
            nums[-i], nums[j - 1] = nums[j - 1], nums[-i]
            nums[-i + 1:] = nums[-i + 1:][::-1]
            print("nums2:{0}".format(nums))

    def nextPermutation1(self, nums):
        print("nums:{0}".format(nums))
        numsLen = len(nums)
        flag=0
        j=0
        if numsLen < 2:
            return nums
        for i in range(numsLen-1,0,-1):
            if nums[i-1] < nums[i]:
                flag = 1
                #print("nums[i-1]:{0}".format(nums[i-1]))
                for j in range(i,numsLen-1):
                    # 正常操作
                    # nums2:[1,5,8,4,7,6,5,3,1] -> [1, 5, 8, 5, 1, 3, 4, 6, 7]
                    if nums[i-1] > nums[j]:
                        #print("{0} {1}".format(nums[i-1],nums[j-1]))
                        temp = nums[i-1]
                        nums[i-1] = nums[j-1]
                        nums[j-1] = temp

                        nums[i:numsLen] =self.reserve(nums[i:numsLen])
                        print("nums2:{0}".format(nums))
                        flag=2
                        break

                # nums:[1, 2, 3]->nums1:[1, 3, 2]
                # nums:[1, 1, 5]->nums1:[1, 5, 1]
                # nums:[1, 3, 2]->nums1:[1, 2, 3]
                if flag == 1:
                    print("i:{0}  j:{1}".format(i,j))
                    temp = nums[i - 1]
                    nums[i - 1] = nums[j + 1]
                    nums[j + 1] = temp
                    nums[i:numsLen] = self.reserve(nums[i:numsLen])
                    print("nums1:{0}".format(nums))
                    flag = 1
                    break
                if flag == 2:
                    break

        # nums:[3, 2, 1] -> nums0:[1, 2, 3]
        if flag == 0 :
            nums[0:numsLen] = self.reserve(nums[0:numsLen])
            print("nums0:{0}".format(nums))

    def nextPermutation(self, nums):
        print("nums:{0}".format(nums))
        numsLen = len(nums)
        if numsLen < 2:
            return nums
        for i in range(numsLen-1,0,-1):
            if nums[i-1] < nums[i]:
                #print("nums[i-1]:{0}".format(nums[i-1]))
                for j in range(i,numsLen-1):
                    if nums[i-1] > nums[j]:
                        #print("{0} {1}".format(nums[i-1],nums[j-1]))
                        temp = nums[i-1]
                        nums[i-1] = nums[j-1]
                        nums[j-1] = temp

                        nums[i:numsLen] =self.reserve(nums[i:numsLen])
                        return nums

                nums[i:numsLen] = self.reserve(nums[i:numsLen])
                return nums

        nums[0:numsLen] = self.reserve(nums[0:numsLen])
        #print("nums:{0}".format(nums))
        return nums

    def reserve(self,nums):
        l = 0
        r = len(nums)-1
        while l<r:
            temp = nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l=l+1
            r=r-1
        return nums

if __name__ == "__main__":
    arrs1=[1,5,8,4,7,6,5,3,1]
    arrs2 = [1,2,3]         # 1,3,2
    arrs3 = [3,2,1]         # 1,2,3
    arrs4 = [1, 1, 5]       # 1,5,1
    arrs5=[]
    arrs6 = [1, 2]
    arrs7 = [1]
    arrs8= [1,3,2]          # [2,1,3]
    solution = Solution()
    solution.nextPermutation2(arrs8)


