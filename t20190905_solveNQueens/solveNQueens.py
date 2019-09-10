#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/9/04
@url：https://leetcode-cn.com/problems/n-queens/
@desc:
    
    51. N皇后

    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
    并且使皇后彼此之间不能相互攻击。

    上图为 8 皇后问题的一种解法。

    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    示例:

    输入: 4
    输出: [
            [".Q..",  // 解法 1
              "...Q",
              "Q...",
              "..Q."],

            ["..Q.",  // 解法 2
              "Q...",
              "...Q",
              ".Q.."]
          ]
    解释: 4 皇后问题存在两个不同的解法。


'''
class Solution:


  def solveNQueens(self, n):
    res = []
    chess_list = [[0 for i in range(n)] for i in range(n)]
    self._dfs(chess_list,n,0,res)
    chess_list = self.draw(n,res)
    return chess_list

  def _dfs(self,chess_list,n,i,res):
    if i == n:
      r = [chess[:] for chess in chess_list]
      res.append(r[:])
    else:
      for j in range(n):
        if chess_list[i][j] == 0:
          if self.check(chess_list,n,i,j):
            chess_list[i][j] = 1
            self._dfs(chess_list,n,i+1,res)
            chess_list[i][j] = 0
          
  # 检测当前位置所对应的行列是否满足要求
  def check(self,chess_list,n,i,j):
    for a in range(n):
      if chess_list[a][j] != 0:
        return False

    for a in range(n):
      if chess_list[i][a] != 0:
        return False

    # 往上正对角线
    a = i-1 
    b = j-1
    while a > -1 and b > -1:
      if chess_list[a][b] != 0:
        return False
      a = a-1
      b = b-1

    # 往下正对角线
    a = i 
    b = j
    while a < n and b < n:
      if chess_list[a][b] != 0:
        return False
      a = a+1
      b = b+1

    # 往上负对角线
    a = i-1 
    b = j+1
    while a > -1 and b < n:
      if chess_list[a][b] != 0:
        return False
      a = a-1
      b = b+1
        
    # 往下负对角线
    a = i + 1
    b = j - 1
    while a < n and b > -1:
      if chess_list[a][b] != 0:
        return False
      a = a+1
      b = b-1

    return True


  def draw(self,n,res):
    chess_list = []
    for r in res:
      chess = []
      for i in range(0,n):
        s = ''
        for j in range(0,n):
          if r[i][j] == 1:
            s = s + 'Q'
          else:
            s = s + '.' 
        chess.append(s)
      chess_list.append(chess)
    return chess_list



  

if __name__ == "__main__":

    print("--------1-------")

    nums = 4
    solution = Solution()
    res=solution.solveNQueens(nums)
    print("res:{0}".format(res))

    