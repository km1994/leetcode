#  560. 和为K的子数组

## 题目描述

   给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

## 示例:

    示例 1 :

    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :

    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

## 思路介绍

### 方法: 哈希表法

#### 题目解析

#### 思路

定义 $\textit{pre}[i]$ 为 $[0..i]$ 里所有数的和，则 $\textit{pre}[i]$ 可以由 $\textit{pre}[i-1]$ 递推而来，即：

$$p r e[i]=p r e[i-1]+n u m s[i]$$

那么「$[j..i]$ 这个子数组和为 k 」这个条件我们可以转化为
   
$$\operatorname{pre}[i]-\operatorname{pre}[j-1]==k$$

简单移项可得符合条件的下标 j 需要满足

$$\operatorname{pre}[j-1]==\operatorname{pre}[i]-k$$

所以我们考虑以 i 结尾的和为 k 的连续子数组个数时只要统计有多少个前缀和为 $\textit{pre}[i]-k$ 的 $\textit{pre}[j]$ 即可。我们建立哈希表 $\textit{mp}$，以和为键，出现次数为对应的值，记录 $\textit{pre}[i]$ 出现的次数，从左往右边更新 $\textit{mp}$ 边计算答案，那么以 $i$ 结尾的答案 $$\textit{mp}[\textit{pre}[i]-k] 即可在 O(1) 时间内得到。最后的答案即为所有下标结尾的和为 k 的子数组个数之和。

需要注意的是，从左往右边更新边计算的时候已经保证了$\textit{mp}[\textit{pre}[i]-k]$ 里记录的 $\textit{pre}[j]$ 的下标范围是 $0\leq j\leq i $。同时，由于$\textit{pre}[i]$ 的计算只与前一项的答案有关，因此我们可以不用建立 $\textit{pre}$ 数组，直接用 $\textit{pre}$ 变量来记录 $pre[i-1]$ 的答案即可。


#### 复杂度计算

时间复杂度：O(N)
空间复杂度：O(N)

## 参考

1. [前缀和 + 哈希表优化](https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/)
