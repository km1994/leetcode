# 73. 矩阵置零

## 题目描述

    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

    示例 1:

    输入: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    示例 2:

    输入: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    输出: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

## 思路介绍

1. 定义 集合 zerosCol、zerosRow 存储 matrix 值为零 的 行和列
2. 遍历 matrix：如果 matrix[i][j]==0，则 zerosCol.add(j)，zerosRow.add(i)
3. 分别 对 zerosCol、zerosRow，将对应行或列置零

## 代码

```python
    class Solution:
        def setZeroes(self, matrix):
            print(f"matrix:{matrix}")
            zerosCol = set()
            zerosRow = set()
            rowLen = len(matrix)
            if rowLen>0:
                colLen = len(matrix[0])
            for i in range(0,rowLen):
                for j in range(0,colLen):
                    print(f"matrix[{i}][{j}]:{matrix[i][j]}")
                    if matrix[i][j] == 0:
                        zerosCol.add(j)
                        zerosRow.add(i)

            print(f"zerosRow:{zerosRow}")
            print(f"zerosCol:{zerosCol}")
            for row in zerosRow:
                for j in range(0,colLen):
                    matrix[row][j] = 0
            for col in zerosCol:
                for i in range(0,rowLen):
                    matrix[i][col] = 0
            return matrix

    if __name__ == "__main__":
        
        solution = Solution()
        while 1:
            str1 = input()
            if str1 != "":
                arr = [[int(c) for c in s.split(",")] for s in str1.split(";")]

                res = solution.setZeroes(arr)
                print(res)
            else:
                break

```

## 复杂度

> 时间复杂度：O(n^2
> )
> 空间复杂度：O(n)