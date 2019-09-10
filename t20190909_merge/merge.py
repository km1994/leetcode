#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/09
@url：https://leetcode-cn.com/problems/merge-sorted-array/
@desc:
    
    88. 合并两个有序数组

    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

    说明:
      初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
      你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    
    示例:

      输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

      输出: [1,2,2,3,5,6]

'''

class Solution:
  def merge(self, nums1, m, nums2, n):
    if n != 0:
      if m == 0:
        for i in range(n):
          nums1[i] = nums2[i]
        m = n
      else:
        for i in range(n):
          l = i 
          print(l)
          r = m-1
          while l <= r:
            mid = int((l+r)/2)
            if nums1[mid] > nums2[i]:
              r = mid - 1
            else:
              l = mid + 1
        
          m = m + 1
          for j in range(m-1,l,-1):
            nums1[j] = nums1[j-1]
        
          nums1[l] = nums2[i]

if __name__ == "__main__":

    solution = Solution()
    print("--------1-------")
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    res=solution.merge(nums1, m, nums2, n)
    print("res:{0}".format(res))

   