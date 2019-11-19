#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/11
@url：https://leetcode-cn.com/problems/contains-duplicate/
@desc:
    
    217. 存在重复元素

    给定一个整数数组，判断是否存在重复元素。

    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

    示例 1:
      输入: [1,2,3,1]
      输出: true
    示例 2:
      输入: [1,2,3,4]
      输出: false
    示例 3:
      输入: [1,1,1,3,3,4,3,2,4,2]
      输出: true

'''

class Solution:
  # 利用字典
  def containsDuplicate(self, nums):
    nums1_dict = {}
    for num in nums:
      if num not in nums1_dict:
        nums1_dict[num]=1
      else:
        return True
    return False
   

if __name__ == "__main__":
    solution = Solution()
    print("--------1-------")
    nums1 = [1,2,3,1]
    res=solution.containsDuplicate(nums1)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = [1,2,3,4]
    res=solution.containsDuplicate(nums1)
    print("res:{0}".format(res))

    print("--------3-------")
    nums1 = [1,1,1,3,3,4,3,2,4,2]
    res=solution.containsDuplicate(nums1)
    print("res:{0}".format(res))

   