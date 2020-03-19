'''
    74. 搜索二维矩阵
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:

    输入:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 3
    输出: true
    示例 2:

    输入:
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 13
    输出: false
'''
import math
class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        left = 0
        right = row*col-1
        mid = 0
        mid_val = 0
        while left <= right:
            mid = math.floor((left+right)/2) 
            mid_val = matrix[math.floor(mid/col)][mid%col]
            if target == mid_val:
                return True
            elif target<mid_val:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == "__main__":
    
    solution = Solution()
    matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
    ]
    target = 50
    res = solution.searchMatrix(matrix,target)
    print(res)





        


  