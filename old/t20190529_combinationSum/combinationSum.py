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
    39. 组合总和
    给定一个无重复元素的数组 candidates 和一个目标数 target ，
    找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。

    说明：
        所有数字（包括 target）都是正整数。
        解集不能包含重复的组合。

    示例 1:
        输入: candidates = [2,3,6,7], target = 7,
        所求解集为:
        [
          [7],
          [2,2,3]
        ]
    示例 2:
        输入: candidates = [2,3,5], target = 8,
        所求解集为:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]
'''


class Solution:
    def __init__(self):
        pass

    def  combinationSum(self, candidates, target):
        def find(output,target):
            if target == 0 and sorted(output) not in res:
                res.append(sorted(output))
                return

            # 剪枝，当 target 值小于 min(candidates)，可以不需要继续遍历
            if target<min(candidates):
                return

            for candidate in candidates:
                new_target = target - candidate
                if new_target >= 0 :
                    find(output+[candidate],new_target)

        res = []
        find([],target)
        return res



if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    res = solution.combinationSum(candidates,target)
    print("res:{0}".format(res))

