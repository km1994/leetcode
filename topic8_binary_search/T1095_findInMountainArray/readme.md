#  1095. 山脉数组中查找目标值

## 题目描述

    （这是一个 交互式问题 ）

    给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

    如果不存在这样的下标 index，就请返回 -1。

    何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

    首先，A.length >= 3

    其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

    A[0] < A[1] < ... A[i-1] < A[i]
    A[i] > A[i+1] > ... > A[A.length - 1]
     

    你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

    MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
    MountainArray.length() - 会返回该数组的长度
     
    注意：

    对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

    为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

## 示例:
```
   示例 1：

    输入：array = [1,2,3,4,5,3,1], target = 3
    输出：2
    解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
    示例 2：

    输入：array = [0,1,2,4,2,1], target = 3
    输出：-1
    解释：3 在数组中没有出现，返回 -1。
     
    提示：

    3 <= mountain_arr.length() <= 10000
    0 <= target <= 10^9
    0 <= mountain_arr.get(index) <= 10^9
```

## 思路介绍

### 方法一：二分查找法

#### 题目解析

1. 由于山脉数组存在一个下标 i ， 使得 i 元素将数组分为两部分，i 之前的所有元素单调递增， i 之后的所有元素单调递减，故称为山脉数组
2. 即 下标为 i 的元素是山脉数组的峰值

#### 思路

1. 利用二分查找，找到数组中的 i ，判断元素 i 是否小于 target，若元素 i 小于 target，则直接返回-1
2. 先判断首个元素值是否大于 target ，若大于则说明 target 不在递增区间内。否则对 i 之前的元素做二分查找，找到 target 直接返回
3. 先判断最后一个元素是否大于 target ，若大于则说明 target 不在递减区间内。否则对 i 之后的元素做二分查找，找到 target 直接返回
4. 执行到这一步，说明上面两步都没有找到 target ，则返回-1
下面用 mid 表示 i(峰值)
用 m 表示 target(目标值) 的下标

   
#### 复杂度计算

> 时间复杂度： O(logn)
> 
> 空间复杂度： O(1)

