#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: sortList.py
@time: 2019/8/13 
@url：https://leetcode-cn.com/problems/power-of-two/
@desc:
231. 2的幂
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

    示例 1:
        输入: 1
        输出: true
        解释: 20 = 1
    示例 2:
        输入: 16
        输出: true
        解释: 24 = 16
    示例 3:
        输入: 218
        输出: false



'''

class Solution:
    def __init__(self):
        pass
    
    def isPowerOfTwo(self, n):
        return n>0 and not n & (n-1)

    def isPowerOfTwo1(self, n):
        if n == 0:
            return True
        while n%2 == 0:
            n = n/2
        if n == 1:
            return True
        return False

    # 不断除 2
    def isPowerOfTwo1(self, n):
        if n == 0:
            return True
        while n%2 == 0:
            n = n/2
        if n == 1:
            return True
        return False

if __name__ == "__main__":

    print("--------1-------")
    nums=1
    solution = Solution()
    res=solution.isPowerOfTwo(nums)
    print("res:{0}".format(res))

    print("--------2-------")
    nums=16
    solution = Solution()
    res=solution.isPowerOfTwo(nums)
    print("res:{0}".format(res))

    print("--------3-------")
    nums=218
    solution = Solution()
    res=solution.isPowerOfTwo(nums)
    print("res:{0}".format(res))
