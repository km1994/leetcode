# 70. 爬楼梯

## 题目描述

    

    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

    注意：给定 n 是一个正整数。

## 示例:
```
   示例 1：

    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶
    示例 2：

    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶
```

## 思路介绍

### 方法一：动态规划

#### 题目解析

$$f(0)=1,f(1)=1$$
$$f(n)=f(n-1)+f(n-2)$$

#### 思路



   
#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(1)

