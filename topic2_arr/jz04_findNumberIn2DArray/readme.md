# 剑指 Offer 04. 二维数组中的查找

## 题目描述

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。



## 思路介绍

### 方法一：双指针

#### 题目解析


1. 因为对于 n * m 的二维数组中：
   1. 每一行都按照从左到右递增的顺序排序；
   2. 每一列都按照从上到下递增的顺序排序；
2. 所以，从左下角看：
   1. 上面的元素比他小；
   2. 左边的元素比他大；

                

#### 思路

1. 从左下角开始遍历数组，做一下三种判断：
   1. 当前值 比 target 大，那么往上移动；
   2. 当前值 比 target 小，那么往右移动；
   3. 当前值 比 target 一样，返回 True；
2. 越界？返回 False


#### 代码

```python
    class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
            方法：双指针法
            解析：
                因为对于 n * m 的二维数组中：
                    每一行都按照从左到右递增的顺序排序；
                    每一列都按照从上到下递增的顺序排序；
                所以，从左下角看：
                    上面的元素比他小；
                    左边的元素比他大；
            方法：
                从左下角开始遍历数组，做一下三种判断：
                    当前值 比 target 大，那么往上移动；
                    当前值 比 target 小，那么往右移动；
                    当前值 比 target 一样，返回 True；
                越界？返回 False
            复杂度：
                时间：O(n*m)
                空间：O(1)
        '''
        row = len(matrix)
        if row==0:
            return False
        col = len(matrix[0])
        t = row-1
        r = 0
        while t>-1 and r<col:
            if target>matrix[t][r]:
                r = r+1
            elif target<matrix[t][r]:
                t = t-1
            else:
                return True 
        return False
        
```

#### 复杂度计算

> 时间复杂度：O(n*m)
>  
> 空间复杂度：O(1)

