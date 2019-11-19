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

    def groupAnagrams(self, strs):
        res=[]
        sort_dict = {}
        for str in strs:
            sorded_str = ''.join(sorted(str))
            if sorded_str not in sort_dict:
                sort_dict[sorded_str] =[]
                sort_dict[sorded_str].append(str)
            else:
                sort_dict[sorded_str].append(str)
        #print(sort_dict)
        for (key,val) in sort_dict.items():
            res.append(val)
        return res


if __name__ == "__main__":
    nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(nums)
    print("res:{0}".format(res))


    

