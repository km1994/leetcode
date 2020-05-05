# 3. 无重复字符的最长子串

## 题目描述

    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
   
## 示例:
```
    示例 1:

    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

## 思路介绍

### 方法一：滑动窗口法
#### 题目解析

#### 思路

1. 定义 集合 diff_dict 存储 极大长度字符串
2. 定义 左右指针 指向 两边
3. 遍历 字符串：
   1. 左指针 过滤掉 重复字符，也就是不重复子字符串 的 左边界；
   2. 右指针 不断 往 右移；
   3. 记录 目前的最大 长度

#### 复杂度计算

> 时间复杂度：O(N)

> 空间复杂度：O(N)
