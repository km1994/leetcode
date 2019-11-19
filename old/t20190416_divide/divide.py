#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: divide.py
@time: 2019/4/16 11:56
@desc:
    22. 括号生成
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

    返回被除数 dividend 除以除数 divisor 得到的商。

    示例 1:
        输入: dividend = 10, divisor = 3
        输出: 3
    示例 2:
        输入: dividend = 7, divisor = -3
        输出: -2
    说明:
        被除数和除数均为 32 位有符号整数。
        除数不为 0。
        假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
        本题中，如果除法结果溢出，则返回 2^31 − 1。
'''

import math
class Solution:
    def __init__(self):
        self.MIN_VALUE =  - math.pow(2,31)
        self.MAX_VALUE =  math.pow(2,31)-1

    def divide(self, dividend, divisor):
        sym_flag = 1
        if divisor == 0:
            return 0
        if dividend < 0 and divisor > 0:
            sym_flag = -1
            dividend = -1 * dividend
        elif dividend > 0 and divisor < 0:
            sym_flag = -1
            divisor = -1 * divisor
        elif dividend < 0 and divisor < 0:
            dividend = -1 * dividend
            divisor = -1 * divisor

        result = 0
        for i in range(31,-1 ,-1):
            if (dividend>>i) >= divisor:
                result = result + (1<<i)
                dividend = dividend - (divisor<<i)

        result = sym_flag * result

        if result < - math.pow(2, 31) or result > math.pow(2, 31) - 1:
            result = math.pow(2, 31) - 1
        return int(result)


    def divide1(self, dividend, divisor):
        sym_flag = 1
        if divisor == 0:
            return 0
        if dividend<0  and  divisor>0:
            sym_flag = -1
            dividend = -1 * dividend
        elif dividend>0  and  divisor<0:
            sym_flag = -1
            divisor = -1 * divisor
        elif dividend<0  and  divisor<0:
            dividend = -1 * dividend
            divisor = -1 * divisor

        quotient = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            quotient = quotient + 1

        quotient = sym_flag * quotient

        if quotient < - math.pow(2,31) or  quotient > math.pow(2,31)-1:
            quotient = math.pow(2,31)-1
        return quotient



if __name__ == "__main__":
    solution=Solution()
    res = solution.divide(-2147483648,-1)
    print("res:{0}".format(res))


