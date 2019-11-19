#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: generateMatrix.py
@time: 2019/7/24
@rel： https://leetcode-cn.com/problems/spiral-matrix-ii/
@url：
@desc:
    70. 爬楼梯

    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。

    示例 1：
        输入： 2
        输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶

    示例 2：
        输入： 3
        输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶



'''
class Solution:
    def __init__(self):
        pass


    # 方法一：递归
    def climbStairs1(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 方法二：动态规划（兔子繁殖问题）（斐波那契数列）
    # 这个问题可以被分解为一些包含最优子结构的子问题，
    # 即它的最优解可以从其子问题的最优解来有效地构建，
    # 我们可以使用动态规划来解决这一问题。
    # 因为第 i 阶可通过以下两种方式计算：
    # 1、在第（i-1）阶后向上爬一步；
    # 2、在第（i-2）阶后向上爬两步
    # 因此，第 i 阶的方法总数可由 第（i-1）阶和第（i-2）阶的方法求和得到。
    # 假设，stairs[i] 为第 i 阶的方法数，那么他的计算公式：
    # stairs[i] = stairs[i-1] + stairs[i-2]
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        stairs = [0] * n  #

        stairs[0] = 1 # 第一阶只有一种可能
        stairs[1] = 2 # 第二阶只有两种可能

        for i in range(2,n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[-1]



if __name__ == "__main__":

    solution = Solution()

    m = 2
    res1 = solution.climbStairs(m)
    print("res1:{0}".format(res1))

    m = 3
    res2 = solution.climbStairs(m)
    print("res2:{0}".format(res2))
    #
    m = 35
    res3 = solution.climbStairs(m)
    print("res3:{0}".format(res3))
