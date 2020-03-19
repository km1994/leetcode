#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: strStr.py
@time: 2019/6/26
@rel： https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/
@url：
@desc:
    46. 全排列

'''


class Solution:
    
    def permute(self,nums):
        res = []
        def backtrack(nums,temp):
            if not nums:
                res.append(temp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],temp+[nums[i]])

        backtrack(nums,[])
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    solution = Solution()
    res = solution.permute(nums)
    print("res:{0}".format(res))


    

