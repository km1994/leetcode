# 217. 存在重复元素

## 题目描述
    
    给定一个整数数组，判断是否存在重复元素。

    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

  
## 示例:
```
    示例 1:

    输入: [1,2,3,1]
    输出: true
    示例 2:

    输入: [1,2,3,4]
    输出: false
    示例 3:

    输入: [1,1,1,3,3,4,3,2,4,2]
    输出: true
```

## 思路介绍

### 方法

#### 题目关键点

1. 记录出现 过 的 数值

#### 思路

1. 利用 字典 存储 出现的词；
2. 每一次 存储到 字典 之前需要 查看 是否 存在，若 是 ，则 表示 该 数值 存在重复 元素

   
#### 复杂度计算

> 时间复杂度：O(n)  

> 空间复杂度：O(n)  

