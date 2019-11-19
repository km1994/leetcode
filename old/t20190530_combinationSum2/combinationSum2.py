#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/5/20
@rel： https://leetcode-cn.com/problems/combination-sum/
@url：
@desc:
    40. 组合总和 II
    给定一个无重复元素的数组 candidates 和一个目标数 target ，
    找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。

    说明：
        所有数字（包括 target）都是正整数。
        解集不能包含重复的组合。

    示例 1:
        输入: candidates = [10,1,2,7,6,1,5], target = 8,
        所求解集为:
        [
          [1, 7],
          [1, 2, 5],
          [2, 6],
          [1, 1, 6]
        ]
    示例 2:
        输入: candidates = [2,5,2,1,2], target = 5,
        所求解集为:
        [
          [1,2,2],
          [5]
        ]
'''


class Solution:
    def __init__(self):
        pass

    def  combinationSum2(self, candidates, target):
        def dfs(candidates,target,index,path,res):
           if target == 0 and path not in res:
               res.append(path)
               return

           # 剪枝，当 target 值小于 min(candidates)，可以不需要继续遍历
           if candidates[index:len(candidates)]:
               if target < min(candidates[index:len(candidates)]):
                   return

           for i in range(index,len(candidates)):
               new_target = target - candidates[i]
               if new_target >= 0:
                   dfs(candidates,new_target,i+1,path+[candidates[i]],res)

        res = []
        candidates = sorted(candidates)
        dfs(candidates,target,0,[],res)
        return res



if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    solution = Solution()
    res = solution.combinationSum2(candidates,target)
    print("res:{0}".format(res))

