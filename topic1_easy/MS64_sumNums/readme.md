# 面试题64. 求1+2+…+n

## 题目描述

    求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

## 示例:
```
   示例 1：

    输入: n = 3
    输出: 6
    示例 2：

    输入: n = 9
    输出: 45
```

## 思路介绍

### 方法一：递归法

#### 题目解析

这道题因为不能使用 乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C），所以难度加大

#### 思路

1.利用递归，然后 将 $n==1$ 的判断 转化为 $n>1 and self.sumNums(n-1)$ 即可。

#### 代码

```python
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        n>1 and self.sumNums(n-1)
        self.res = self.res + n
        return self.res
```
   
#### 复杂度计算

> 时间复杂度：O(n)
>  
> 空间复杂度：O(n)

