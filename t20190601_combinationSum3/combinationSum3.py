#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/6/01
@rel： https://leetcode-cn.com/problems/combination-sum-iii/
@url：
@desc:
    216. 组合总和 III
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

    说明：
        所有数字（包括 target）都是正整数。
        解集不能包含重复的组合。

    示例 1:
        输入: k = 3, n = 7
        输出: [[1,2,4]]
    示例 2:
        输入: k = 3, n = 9
        输出: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution:
    def __init__(self):
        pass

    def combinationSum3(self, k, n):
        def dfs(n,k,target,index,path,res):
            if index > 10:
                return

            if target == 0 and path not in res and len(path)==k:
                res.append(path)
                return

            if target < index:
                return

            for i in range(index,min(10,n)):
                new_target = target - i
                if new_target >= 0 and len(path) < k:
                    dfs(n,k,new_target,i+1,path+[i],res)

        res = []
        dfs(n,k,n,1,[],res)
        return res



if __name__ == "__main__":
    k = 3
    n = 7
    solution = Solution()
    res = solution.combinationSum3(k,n)
    print("res:{0}".format(res))

