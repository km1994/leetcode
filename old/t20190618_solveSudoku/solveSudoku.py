#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: solveSudoku.py
@time: 2019/6/18
@rel： https://leetcode-cn.com/problems/sudoku-solver/
@url：
@desc:
    37. 解数独
    编写一个程序，通过已填充的空格来解决数独问题。

    一个数独的解法需遵循如下规则：

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    空白格用 '.' 表示。

'''


class Solution:
    def __init__(self):
        pass

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 把所有没填数字的位置找到
        all_points = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    all_points.append([i, j])

        # check函数是为了检查是否在point位置k是合适的
        def check(point, k):
            row_i = point[0]
            col_j = point[1]
            for i in  range(9):
                # 检查 行
                if i != row_i and board[i][col_j] == k:
                    return False
                # 检查 列
                if i != col_j and board[row_i][i] == k:
                    return False
            # 检查块
            for i in range(row_i//3*3 , row_i//3*3+3):
                for j in range(col_j//3*3, col_j//3*3+3):
                    if i != row_i and j != col_j and board[i][j] == k:
                        return False

            return True

        def backtrack(i):
            # 回溯终止条件
            if i == len(all_points):
                return True
            for j in range(1, 10):
                # 检查是否合适
                if check(all_points[i],str(j)):
                    # 合适就把位置改过来
                    board[all_points[i][0]][all_points[i][1]] = str(j)
                    if backtrack(i+1): # 回溯下一个点
                        return True
                    board[all_points[i][0]][all_points[i][1]] = "."# 不成功把原来改回来
            return False

        backtrack(0)
        print("board:{0}".format(board))


if __name__ == "__main__":
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    solution.solveSudoku(board1)
    

