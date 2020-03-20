# 88. 合并两个有序数组

## 题目描述

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

    说明:

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

## 示例:
```
    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]
```

## 思路介绍

### 方法一：三指针法

#### 题目解析

1. 数组 nums1 和 nums2 有序；
2. 数组 nums1 有足够空间容纳 所有元素；
3. 数组 nums1 未填充元素 值为 0 

## 解法

1. 定义一个指针 final_pos，指向 nums1 最后面的位置，然后逐个将 nums1 和 nums2 最大的插入 nums1 后面，并向前移动 final_pos、m、n

#### 思路

1. 定义三个指针
   1. final_pos 指向 nums1 最后一个位置索引；
   2. m  指向 nums1 最后一个位置不等于 0 索引；
   3. n  指向 nums2 最后一个位置不等于 0 索引；
2. 逐个 比较 nums1[m] 和 nums[n]，直到 m < 0 或 n < 0:
   1. 若 nums1[m] > nums[n]，则将 nums1[m] 的插到 nums1[final_pos] 位置，两个指针 final_pos 和 m 左移；
   2. 若 nums1[m] 《= nums[n]，则将 nums2[n] 的插到 nums1[final_pos] 位置，两个指针 final_pos 和 n 左移；
3. nums2 剩余  的 插入 num1;

   
#### 复杂度计算

> 时间复杂度：O(n+m)  

> 空间复杂度：O(1)  

