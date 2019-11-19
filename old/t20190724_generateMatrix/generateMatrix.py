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


'''
class Solution:
    def __init__(self):
        pass

    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for i in range(n)]
        r=0
        i=0
        j=0
        num = 1
        while r <= n-1:
            if j <= n-1-r:
                print("--1--")
                j = r
                while j <= n-1-r:
                    matrix[i][j] = num
                    num = num + 1
                    j = j + 1
                j = j - 1
            else:
                return matrix

            if i <= n-1-r:
                print("--2--")
                i = r + 1
                while i <= n-1-r:
                    matrix[i][j] = num
                    num = num + 1
                    i = i + 1
                i = i - 1
            else:
                return matrix

            if j >= r:
                print("--3--")
                j = j - 1
                while j >= r:
                    matrix[i][j] = num
                    num = num + 1
                    j= j - 1
                j = j + 1
            else:
                return matrix

            if i >= r+1:
                print("--4--")
                i = i - 1
                while i >= r+1:
                    matrix[i][j] = num
                    num = num + 1
                    i = i - 1
                i = i + 1
            else:
                return matrix



            r = r + 1
        return matrix


if __name__ == "__main__":

    solution = Solution()

    n = 3
    res1 = solution.generateMatrix(n)
    print("res1:{0}".format(res1))






    

