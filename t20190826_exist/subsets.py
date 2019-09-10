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
    78. 子集
    
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

    说明：解集不能包含重复的子集。

    示例:

    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

'''

class Solution:

    # 方法一：回溯法：仍然是那颗状态树，不过不再走遍所有的节点，
    # 而是通过回溯，跳过一些节点。前面那种标准的二叉树中序遍历，
    # 虽然更容易理解，其实实用性有限，非常不利于剪枝。
    def subsets(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return []
        res=[]
        self._dfs(nums,0,[],res)
        res.append([])
        return res
    
    def _dfs(self,nums,i,sub,res):
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            sub.append(nums[j])
            res.append(sub[:])
            self._dfs(nums,j+1,sub,res)
            sub.pop(-1)

if __name__ == "__main__":

    print("--------1-------")
    nums = [1,2,3]
    solution = Solution()
    res=solution.subsets(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums = []
    solution = Solution()
    res=solution.subsets(nums)
    print("res:{0}".format(res))

    