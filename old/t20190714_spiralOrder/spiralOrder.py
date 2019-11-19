#!/usr/bin/env python
# encoding: utf-8
'''
@author: KM
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangkm601@gmail.com
@software: garner
@file: myPow.py
@time: 2019/7/09
@rel： https://leetcode-cn.com/problems/first-missing-positive/
@url：
@desc:
    54. 螺旋矩阵
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    示例 1:
        输入:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        输出: [1,2,3,6,9,8,7,4,5]
    示例 2:
        输入:
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        输出: [1,2,3,4,8,12,11,10,9,5,6,7]



'''

class Solution:
    def __init__(self):
        pass

    def spiralOrder(self, matrix):

        if not len(matrix):
            return []

        new_matrix = []

        rate = 0
        len_i = len(matrix)
        len_j = len(matrix[0])
        i = rate
        j = rate
        while True:
            if rate > len_j - 1 - rate:
                break
            else:
                while j <= len_j - 1 - rate:
                    print("matrix[{0}][{1}]:{2}".format(i,j,matrix[i][j]))
                    new_matrix.append(matrix[i][j])
                    j = j+1
            j = j - 1
            i = i + 1
            if rate == len_i - 1 -  rate:
                break
            else:
                while i <= len_i - 1 - rate:
                    print("matrix[{0}][{1}]:{2}".format(i, j, matrix[i][j]))
                    new_matrix.append(matrix[i][j])
                    i=i+1
            i = i - 1
            j = j - 1
            if len_j - 1 - rate == rate:
                break
            else:
                while j >= rate:
                    print("matrix[{0}][{1}]:{2}".format(i, j, matrix[i][j]))
                    new_matrix.append(matrix[i][j])
                    j = j -1
            j = j + 1
            i = i - 1
            if len_i - 1 - rate == rate + 1:
                break
            else:
                while i >= rate + 1:
                    print("matrix[{0}][{1}]:{2}".format(i, j, matrix[i][j]))
                    new_matrix.append(matrix[i][j])
                    i = i - 1
            i = i + 1
            j = j + 1
            rate = rate + 1

        return new_matrix

if __name__ == "__main__":
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13,14,15,16]]
    matrix4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # nums3 = [1,3,5,6]
    # target3 = 7
    # nums4 = [1,3,5,6]
    # target4 = 0
    solution = Solution()
    res1 = solution.spiralOrder(matrix1)
    print("res1:{0}".format(res1))

    res2 = solution.spiralOrder(matrix2)
    print("res2:{0}".format(res2))

    res3 = solution.spiralOrder(matrix3)
    print("res3:{0}".format(res3))

    res4 = solution.spiralOrder(matrix4)
    print("res4:{0}".format(res4))
    #
    # res3 = solution.searchInsert(nums3,target3)
    # print("res3:{0}".format(res3))
    #
    # res4 = solution.searchInsert(nums4,target4)
    # print("res4:{0}".format(res4))


    

