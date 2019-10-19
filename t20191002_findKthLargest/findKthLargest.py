#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/10/02
@url：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
@desc:
    
    215. 数组中的第K个最大元素

    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:

    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4

'''
'''
    先建立初始堆，然后进行k-1次排序
    （堆顶元素与最后元素交换，并调整剩余堆结构），
    最后返回堆顶元素即可。
'''
import math
class Solution:
    def findKthLargest(self, nums,k):
        res = self.heapsort(nums,len(nums),k)
        return res
    def adjust(self,nums,i,n):
        x = nums[i]
        k = 2*i+1
        while k<=n:
            if k<n and nums[k+1]>nums[k]:
                k += 1
            if x > nums[k]:
                break
            nums[(k+1)//2-1] = nums[k]
            k = 2*k+1
        nums[(k+1)//2-1] = x
    def heapsort(self,nums,n,k):
        for i in range(n//2-1,-1,-1):
            self.adjust(nums,i,n-1)
        for i in range(n-1,n-k,-1):
            nums[i],nums[0] = nums[0],nums[i]
            self.adjust(nums,0,i-1)
        return nums[0]

if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 =  [3,2,1,5,6,4] 
    k = 2
    res=solution.findKthLargest(nums1,k)
    print("res:{0}".format(res))
