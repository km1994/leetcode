#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: myPow.py
@time: 2019/7/09
@rel： https://leetcode-cn.com/problems/powx-n/
@url：
@desc:
    50. Pow(x, n)
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。

    分治，x 的 n 次方，
        n是偶数-计算 y=x^(n/2)，然后计算y的平方
        n是奇数-y = y * y * x
        O(logn)
'''


class Solution:

    def myPow(self,x,n):
        if not n:   # x 的 0 次方
            return 1

        if n < 0: # 如果 n 小于 0 ，这个时候采用的方法是，计算 x^n 的值，然后在取倒数
            return 1/self.myPow(x,-n)
        if n % 2 == 1:  # 如果 n 为奇数，需要 换成 x 的 奇数幂 除以 x
            return x * self.myPow(x,n-1)
        # 若 n 为 偶数，那么只需要 计算 （x*x）^ (n/2)
        return self.myPow(x*x,n/2)



if __name__ == "__main__":
    x = 0.00001
    n = 2147483647


    solution = Solution()
    res = solution.myPow(x,n)
    print("res:{0}".format(res))


    

