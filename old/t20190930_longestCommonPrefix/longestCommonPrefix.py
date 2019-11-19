#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/30
@url：https://leetcode-cn.com/problems/longest-common-prefix/
@desc:
    
    14. 最长公共前缀

    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

'''
import math
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ""

        ans = strs[0]

        for i in range(1,strs_len):
            j = 0
            while j<len(ans) and j<len(strs[i]):
                if ans[j] != strs[i][j]:
                    break
                j = j + 1
            ans = ans[0:j]
            if ans == "":
                return ans
        return ans

if __name__ == "__main__":

    solution = Solution()

    print("--------1-------")
    nums1 = ["flower","flow","flight"]
    res=solution.longestCommonPrefix(nums1)
    print("res:{0}".format(res))

    print("--------2-------")
    nums1 = ["dog","racecar","car"]
    res=solution.longestCommonPrefix(nums1)
    print("res:{0}".format(res))


    

    