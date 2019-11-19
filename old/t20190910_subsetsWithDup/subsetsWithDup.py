#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/10
@url：https://leetcode-cn.com/problems/subsets-ii/
@desc:
    
    90. 子集 II

    给定一个可能包含重复元素的整数数组 nums，
    返回该数组所有可能的子集（幂集）。

    说明：解集不能包含重复的子集。

    示例:

    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]


'''

class Solution:

  # 方法一
  def subsetsWithDup1(self, nums):
    if not nums:
      return [] 
    res = []
    temp = []
    nums.sort()
    self.help(nums, 0, temp, res)
    return res
    
  def help(self, nums, index, temp, res):
    res.append(temp.copy())
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue 
        temp.append(nums[i])
        self.help(nums, i+1, temp, res)
        temp.pop(-1)

  # 方法二
  def subsetsWithDup(self, nums):
    nums_len = len(nums)
    if nums_len == 0:
      return []
    
    res_list = [[]]
    nums = sorted(nums)
    res = []
    def _dfs(nums,start,res,res_list):
      if res not in res_list:
        res_list.append(res[:])
        
      
      for i in range(start,nums_len):
        res.append(nums[i])
        _dfs(nums,i+1,res,res_list)
        res.pop(-1)
      
    _dfs(nums,0,res,res_list)

    return res_list

    

if __name__ == "__main__":

    solution = Solution()
    print("--------1-------")
    nums1 = [1,2,2]
    res=solution.subsetsWithDup(nums1)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = [4,4,4,1,4]
    res=solution.subsetsWithDup(nums1)
    print("res:{0}".format(res))

   