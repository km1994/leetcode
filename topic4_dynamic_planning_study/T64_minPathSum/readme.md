# 64. 最小路径和

## 题目描述

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7

![](img/minpath.jpg)

解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

## 思路介绍

### 方法 1：动态规划  O(N^2)

#### 题目解析

#### 思路

- 状态方程

```s
    sum_grid[i][j] = min(sum_grid[i-1][j]+grid[i][j],sum_grid[i][j-1]+grid[i][j])
```

#### 代码

```s
class Solution(object):
    def minPathSum(self, grid):
        """方法 1：动态规划 
            复杂度： 时间：O(N^2)   空间：O(N^2)
        """
        # step 1：判空
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])
        if col==0: return sum(grid)
        # step 2: 初始化 数组
        sum_grid = [[9999 for j in range(col)] for i in range(row)]
        sum_grid[0][0] = grid[0][0]
        # step 3: 初始化 第一列
        for i in range(1,row):  
            sum_grid[i][0] = sum_grid[i-1][0]+grid[i][0]
        # step 4：初始化 第一行
        for i in range(1,col):   
            sum_grid[0][i] = sum_grid[0][i-1]+grid[0][i]
        # step 5：动态规划 
        '''
            状态方程：sum_grid[i][j] = min(sum_grid[i-1][j]+grid[i][j],sum_grid[i][j-1]+grid[i][j])
        '''
        for i in range(1,row):
            for j in range(1,col):
                sum_grid[i][j] = min(
                    sum_grid[i-1][j]+grid[i][j],
                    sum_grid[i][j-1]+grid[i][j]
                )
        return sum_grid[-1][-1]
```

#### 复杂度计算

> 时间复杂度：O(N^2)
>  
> 空间复杂度：O(N^2)

### 方法 2：动态规划  O(N)

#### 题目解析

#### 思路

- 状态方程

```s
    sum_grid[j+1] = min(sum_grid[j]+grid[i][j],sum_grid[j+1]+grid[i][j])
```
#### 代码

```s
class Solution(object):
    def minPathSum(self, grid):
        """方法 1：动态规划 
            复杂度： 时间：O(N^2)   空间：O(N)
        """
        # step 1：判空
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])
        if col==0: return sum(grid)
        # step 2: 初始化 数组
        sum_grid = [999 for j in range(col+1)] 
        sum_grid[1] = 0
        # step 3：动态规划
        '''状态方程：sum_grid[j+1] = min(sum_grid[j]+grid[i][j],sum_grid[j+1]+grid[i][j])'''
        for i in range(row):
            for j in range(col):
                sum_grid[j+1] = min(sum_grid[j]+grid[i][j],sum_grid[j+1]+grid[i][j])
        return sum_grid[-1]
```

#### 复杂度计算

> 时间复杂度：O(N^2)
>  
> 空间复杂度：O(N)