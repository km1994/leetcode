'''
    240. 搜索二维矩阵 II
    编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
    示例:

    现有矩阵 matrix 如下：

    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    给定 target = 5，返回 true。

    给定 target = 20，返回 false。
'''
import math
class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix) 
        if row == 0:
            return False
        col = len(matrix[0]) 
        if col == 0:
            return False

        row_pos = 0
        col_pos = col - 1
        while row_pos>=0 and col_pos>=0 and  row_pos<row and col_pos<col:
            if target == matrix[row_pos][col_pos]:
                return True
            elif target > matrix[row_pos][col_pos]:
                row_pos = row_pos + 1
            else:
                col_pos = col_pos - 1

        return False


if __name__ == "__main__":
    
    solution = Solution()
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    res = solution.searchMatrix(matrix,target)
    print(res)

    matrix = [
        []
    ]
    target = 5
    res = solution.searchMatrix(matrix,target)
    print(res)





        


  