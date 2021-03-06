# 62. 不同路径

## 题目描述

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

![](img/p1.png)

例如，上图是一个7 x 3 的网格。有多少可能的路径？


## 示例:
```
    示例 1:
		输入: m = 3, n = 2
		输出: 3
		解释:
		从左上角开始，总共有 3 条路径可以到达右下角。
		1. 向右 -> 向右 -> 向下
		2. 向右 -> 向下 -> 向右
		3. 向下 -> 向右 -> 向右
	示例 2:
		输入: m = 7, n = 3
		输出: 28

```

## 思路介绍

### 方法一：动态规划法

#### 题目解析

1. 因为机器人 每次 只能 向下或者向右移动一步，所以 当前 位置 的 方法数 只要来源于 上边空格 和 左边空格 的 方法数 之和

#### 思路

1. 由 前面问题解析，可以知道，当前 位置 的 方法数 只要来源于 上边空格 和 左边空格 的 方法数 之和，即 可以知道状态方程：

```
	dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

2. 有两个个问题：
   1. 对于 第一行 ，它只能 从 第一行前一列 移动过来，所以 它 的方法数只能为 1；
   2. 对于 第一列 ，它只能 从 第一列前一行 移动过来，所以 它 的方法数只能为 1；
	因此，对应 的 初始状态方程为:

```
	dp[0][j] = dp[i][0] = 1 , i in [0,m] , j in [0,n]
```

#### 复杂度计算

> 时间复杂度： O(m*n)
> 
> 空间复杂度： O(m*n)

### 方法二：动态规划 优化

#### 题目解析

1. 这道题的关键 是要 保留 上一行 和 同一行上一列元素 信息

#### 思路
1. 定义 一个 数组 col[n] 用于保存 上一行元素 和 同一行上一列元素；
2. 然后 循环遍历 ，当前 元素的 值 
```
	col[i] = col[i] + col[i-1]
```

#### 复杂度计算

> 时间复杂度： O(m*n)
> 
> 空间复杂度： O(n)

