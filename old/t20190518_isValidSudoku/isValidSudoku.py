#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: search.py
@time: 2019/5/18
@rel： https://leetcode-cn.com/problems/valid-sudoku/
@url： https://mp.weixin.qq.com/s?__biz=MzAxMTU5Njg4NQ==&mid=100001874&idx=3&sn=8aac86e18cac062ce2edfe15c66fb669
@desc:
    36. 有效的数独
    判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
        1、数字 1-9 在每一行只能出现一次。
        2、数字 1-9 在每一列只能出现一次。
        3、数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    示例 1:
        输入:
        [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        输出: true
    示例 2:
        输入:
        [
          ["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        输出: false

    解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
'''


class Solution:
    def __init__(self):
        pass

    def isValidSudoku(self, board):
        # numberList = []  # 用于存储 每一行、每一列、每一3x3 宫内出现的数字

        row = 0
        col = 0
        # 对行进行判断有效性
        for row in board:
            numberList = []
            for col in row:
                if col != ".":
                    if col not in numberList:
                        numberList.append(col)
                    else:
                        return False
        print("row is Valid!!!")

        # 对列进行判断有效性
        for col in range(0,len(board[0])):
            numberList = []
            for row in range(0,len(board)):
                if board[row][col] != ".":
                    if board[row][col] not in numberList:
                        numberList.append(board[row][col])
                    else:
                        print("col is not Valid!!!")
                        return False
        print("col is Valid!!!")

        # 对小方格进行判断有效性
        for extRow in range(0,3):
            for extCol in range(0, 3):
                numberList = []
                for intRow in range(0,3):
                    for intCol in range(0, 3):
                        if board[extRow*3 + intRow][extCol*3 + intCol] != ".":
                            if board[extRow*3 + intRow][extCol*3 + intCol] not in numberList:
                                numberList.append(board[extRow*3 + intRow][extCol*3 + intCol])
                            else:
                                print("small square is not Valid!!!")
                                return False
        print("small square is Valid!!!")
        return True



if __name__ == "__main__":
    board1 = [
              ["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ]

    board2 = [
              ["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ]
    solution = Solution()
    res1 = solution.isValidSudoku(board1)
    print("res1:{0}".format(res1))

    res2 = solution.isValidSudoku(board2)
    print("res2:{0}".format(res2))


