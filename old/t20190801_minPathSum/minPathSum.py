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
    64. 最小路径和

    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。

    示例:
        输入:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        输出: 7
        解释: 因为路径 1→3→1→1→1 的总和最小。



'''
class Solution:
    def __init__(self):
        pass

    # 自底向上
    def minPathSum(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        dp = [[0]*col for _ in range(row)]
        dp[0][0] = grid[0][0]

        # 第一行
        for j in range(1,col):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # 第一列
        for i in range(1,row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]



if __name__ == "__main__":

    solution = Solution()

    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]

    res1 = solution.minPathSum(grid)
    print("res1:{0}".format(res1))

    grid = [
        [1,4,8,6,2,2,1,7],
        [4,7,3,1,4,5,5,1],
        [8,8,2,1,1,8,0,1],
        [8,9,2,9,8,0,8,9],
        [5,7,5,7,1,8,5,5],
        [7,0,9,4,5,6,5,6],
        [4,9,9,7,9,1,9,0]
    ]

    res1 = solution.minPathSum(grid)
    print("res1:{0}".format(res1))


