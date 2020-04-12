# 347. 前 K 个高频元素

## 题目描述

    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

## 示例:
```
   示例 1:

    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]
    示例 2:

    输入: nums = [1], k = 1
    输出: [1]
    说明：

    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
```

## 思路介绍

### 方法一：堆

#### 题目解析



#### 思路

1. 首先 对 列表 进行 计数；
2. 利用 堆 找到 前 k 大 的 元素


#### 复杂度计算

> 时间复杂度： O(N\log(k))
> 
> 空间复杂度： O(N) 


## 参考

1. [heapq](https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l203)
2. [方法 1：堆](https://leetcode-cn.com/problems/top-k-frequent-elements/solution/qian-k-ge-gao-pin-yuan-su-by-leetcode/)
