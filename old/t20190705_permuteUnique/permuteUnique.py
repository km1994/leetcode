#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: strStr.py
@time: 2019/7/06
@rel： https://leetcode-cn.com/problems/permutations-ii/
@url：
@desc:
    47. 全排列 II

'''


class Solution:
    def __init__(self):
        pass

    def permuteUnique(self, nums):
        res = []
        def backtrack(nums, temp):
            if not nums:
                if temp not in res:
                    res.append(temp)
                    return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], temp + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == "__main__":
    nums = [1,1,3]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print("res:{0}".format(res))


    

