'''
    221. 最大正方形
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

    示例:

    输入: 

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    输出: 4

'''
import copy
# from T_HeapSort.Heap import MaxHeap,MinHeap
class Solution:
    # 动态规划法
    def maximalSquare(self, matrix):
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        dp = [[0 for j in range(col)] for i in range(row)]
        max_val = 0

        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == "1":
                    if i==0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    if max_val < dp[i][j]:
                        max_val = dp[i][j]
        # print(dp)
        return max_val*max_val

if __name__ == "__main__":
    
    solution = Solution()
    while 1:
        str1 = input()
        if str1 != "" :
            matrix = [[c for c in s.split(",")] for s in str1.split(";")]
            print(f"board:{matrix}")

            res = solution.maximalSquare(matrix)
            print(res)
        else:
            break

