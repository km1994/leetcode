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
    60. 第k个排列

    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？

    例如，上图是一个7 x 3 的网格。有多少可能的路径？
    说明：m 和 n 的值均不超过 100。

    示例 1:
        输入: m = 3, n = 2
        输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右

    示例 2:
        输入: m = 7, n = 3
        输出: 28

'''
class Solution:
    def __init__(self):
        pass


    # 方法三：动态规划
    def uniquePaths(self, m, n):
        a = min(m,n)
        b = max(m,n)
        count = b + a - 1
        target = [0 for i in range(a)]
        target[0] = 1
        for i in range(count-1):
            for j in range(a-1,0,-1):
                target[j] = target[j] + target[j-1]
        return target[-1]



    # 方法二：排列组合
    # 因为机器到底右下角，向下几步，向右几步都是固定的，
    # 比如，m = 3, n = 2，我们只要向下1步，向右2步就一定能到达终点。
    # 所以，C(m-1,m-n-2)
    def uniquePaths2(self, m, n):
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))


    # 方法一：递归 begin (时间太长)
    def uniquePaths1(self, m, n):
        # 空情况
        if m == 0 or n == 0:
            return 0

        def __dfs(r, b, fr, fb):
            # 到达目的地
            if r == fr and fb == b:
                return 1

            # 某个方向已经走到尽头，接下去只要一直往另一个走即可。
            if r == fr or fb == b:
                return 1

            return __dfs(r + 1, b, fr, fb) + __dfs(r, b + 1, fr, fb)

        return __dfs(0,0,m-1,n-1)

    # 方法二：递归 end




if __name__ == "__main__":

    solution = Solution()

    # m = 3
    # n = 2
    # res1 = solution.uniquePaths(m, n)
    # print("res1:{0}".format(res1))

    m = 4
    n = 3
    res2 = solution.uniquePaths(m, n)
    print("res2:{0}".format(res2))
    #
    # m = 0
    # n = 3
    # res3 = solution.uniquePaths(m, n)
    # print("res3:{0}".format(res3))
    #
    # m = 3
    # n = 0
    # res4 = solution.uniquePaths(m, n)
    # print("res4:{0}".format(res4))
    #
    # m = 1
    # n = 3
    # res5 = solution.uniquePaths(m, n)
    # print("res5:{0}".format(res5))
    #
    # m = 3
    # n = 1
    # res6 = solution.uniquePaths(m, n)
    # print("res6:{0}".format(res6))

    m = 23
    n = 12
    res7 = solution.uniquePaths(m, n)
    print("res7:{0}".format(res7))


