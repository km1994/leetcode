# 763. 划分字母区间

## 题目描述

    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

    示例 1：

        输入：S = "ababcbacadefegdehijhklij"
        输出：[9,7,8]
        解释：
        划分结果为 "ababcbaca", "defegde", "hijhklij"。
        每个字母最多出现在一个片段中。
        像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

## 思路介绍

### 方法一：贪心算法 + 双指针

#### 题目解析


#### 思路：
1. 利用 字典 记录 每个 字符 最后一次出现的下标位置；
2. 定义 start 和 end 用于维护 当前片段区间，定义 char_max_pos 用于记录 最远位置；
3. 遍历字符串：
    3.1 比较当前字符 最后一次出现位置 和 最远距离 char_max_pos 的大小，将最大的赋予 char_max_pos；
    3.2 若 end 和 char_max_pos 相等，则表示以 start 和 end 为边界的 切片 包含前面出现过的所有字符的最远位置：
        3.2.1 记录，并 切片；
        3.2.2 新片 从 上一次切片 的 下一个位置开始；
#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(n)
