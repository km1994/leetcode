#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/30
@url：https://leetcode-cn.com/problems/word-search/
@desc:
    79. 单词搜索
    
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

    示例:

    board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.

'''

class Solution:

    def exist(self, board, word):
        if len(word) == 0:
            return True
        board_row = len(board)
        board_col = len(board[0])
        board_flag = [[False for j in range(0,board_col)] for i in range(0,board_row)]
        #print(board_flag)
        res = False
        for i in range(0,board_row):
            for j in range(0,board_col):
                if board[i][j] == word[0]:
                    board_flag[i][j] = True
                    res = self._dfs(board,word[1:],board_flag,board_row,board_col,i,j,res)
                    board_flag[i][j] = False
        return res

    
    def _dfs(self,board,word,board_flag,board_row,board_col,i,j,res):
        if len(word) == 0:
            return True
        if res:
            return res

        if i > 0 and not board_flag[i-1][j] and word[0] == board[i-1][j]:
            board_flag[i-1][j] = True
            res = self._dfs(board,word[1:],board_flag,board_row,board_col,i-1,j,res)
            board_flag[i-1][j] = False
        
        if i < board_row-1 and not board_flag[i+1][j] and word[0] == board[i+1][j]:
            board_flag[i+1][j] = True
            res = self._dfs(board,word[1:],board_flag,board_row,board_col,i+1,j,res)
            board_flag[i+1][j] = False

        if j > 0 and not board_flag[i][j-1] and word[0] == board[i][j-1]:
            board_flag[i][j-1] = True
            res = self._dfs(board,word[1:],board_flag,board_row,board_col,i,j-1,res)
            board_flag[i][j-1] = False

        if j < board_col-1 and not board_flag[i][j+1] and word[0] == board[i][j+1]:
            board_flag[i][j+1] = True
            res = self._dfs(board,word[1:],board_flag,board_row,board_col,i,j+1,res)
            board_flag[i][j+1] = False
        
        return res


if __name__ == "__main__":

    print("--------1-------")
    board =[["a","a"]]
    word = "aaa"
    solution = Solution()
    res=solution.exist(board, word)
    print("res:{0}".format(res))

    print("--------2-------")
    board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "ABCB"
    solution = Solution()
    res=solution.exist(board, word)
    print("res:{0}".format(res))

    print("--------3-------")
    board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "SEE"
    solution = Solution()
    res=solution.exist(board, word)
    print("res:{0}".format(res))

    