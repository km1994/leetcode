#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@time: 2019/8/16 
@url：https://leetcode-cn.com/problems/search-a-2d-matrix/
@desc:
    74. 搜索二维矩阵
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:
    输入:
        matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
        target = 3
    输出: true

    示例 2:
    输入:
        matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
        target = 13
    输出: false

'''

class Solution:
    def __init__(self):
        pass
    
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        target_row = -1
        
        for i in range(row):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                target_row = i
        
        if target_row == -1:
            return False
        
        left = 0
        right = col-1
        while left <= right:
            mid = int((left+right)/2)
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                right = mid - 1
            elif matrix[target_row][mid] < target:
                left = mid + 1

        return False
   

if __name__ == "__main__":

    print("--------1-------")
    matrix= [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
    target = 3
    solution = Solution()
    res=solution.searchMatrix(matrix,target)
    print("res:{0}".format(res))

    print("--------2-------")
    matrix= [
            [1]
        ]
    target = 1
    solution = Solution()
    res=solution.searchMatrix(matrix,target)
    print("res:{0}".format(res))

    